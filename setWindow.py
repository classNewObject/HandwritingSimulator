"""设置子窗口"""
from PySide6.QtCore import Slot, Qt, QSize, QEvent, QPoint
from PySide6.QtGui import QPixmap, QScreen
from PySide6.QtWidgets import QApplication, QWidget

from ui_set import Ui_Form as SetWindow
from func import *


class ChildSetWindow(QWidget):
    """创建子窗口类"""

    showed_info = False  # 显示radioButton按钮被按下的提示信息
    theme = DEFAULT_THEME  # 记录主题
    previous_preset_file = None  # 之前的预设文件
    change_theme_signal = Signal(str)  # 改变主题信号
    change_out_path_signal = Signal(str)  # 改变输出路径信号
    change_preset_path_signal = Signal(str)  # 改变预设路径信号

    def __init__(self):
        super(ChildSetWindow, self).__init__()
        # 初始化界面
        self.ui = SetWindow()
        self.ui.setupUi(self)

        # comboBox里添加主题数据
        self.ui.comboBox.addItems(THEMES)

        # 当子窗口打开时主窗口设置为禁用状态
        self.setWindowModality(Qt.ApplicationModal)

        # 窗口设置
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗体无边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

        # 创建配置文件操作对象
        self.config = configparser.ConfigParser()

        # 加载配置文件
        self.load()

        # 添加事件过滤器实现窗口的拖动
        self.ui.titleWidget.installEventFilter(self)  # 标题栏添加事件过滤器
        self.ui.titleWidget.setMouseTracking(True)  # 设置标题栏鼠标跟踪

        # 初始化点击坐标
        self.clickPos = QPoint()

        # 设置图标和大小
        self.ui.closeButton.setIconSize(QSize(20, 20))
        self.ui.closeButton.setIcon(QPixmap("./icons/close.png"))

        # 刷新滑条的值
        self.show_value()

        # 绑定对应事件
        self.signal_solt_connection()

    def signal_solt_connection(self):
        """绑定事件"""

        @Slot()
        def show_info():
            """提示是否启用"""
            if self.ui.radioButton.isChecked() and not self.showed_info:
                QMessageBox.warning(self, "警告", ACCELERATE_MESSAGE)
                self.ui.radioButton.setChecked(True)
                self.showed_info = True

        self.ui.closeButton.clicked.connect(self.hide_windows)
        self.ui.horizontalSlider.valueChanged.connect(self.show_value)

        self.ui.chooseFileButton.clicked.connect(self.set_preset_path)
        self.ui.chooseDirButton.clicked.connect(lambda: choose_file(
            self, "选择文件夹", file=False, line_edit=self.ui.chooseDirLineEdit
        ))

        self.ui.comboBox.currentIndexChanged.connect(self.change_theme)
        self.ui.radioButton.toggled.connect(show_info)

    def show_value(self):
        """设置滑条的值的显示处理"""
        value = self.ui.horizontalSlider.value() / 10  # 读取当前滑动条值
        self.ui.label_6.setText(str(value))  # 显示在label里

    def load(self):
        """加载配置文件"""
        # 判断文件是否存在，存在则继续执行
        if os.path.exists(SET_FILE_PATH):
            try:
                # 读取文件
                self.config.read(SET_FILE_PATH, encoding="utf-8")

                # 设置内容
                preset_file = self.config.get(PRESET, PATH)
                self.ui.chooseDirLineEdit.setText(self.config.get(OUT, PATH))
                self.ui.chooseFileLineEdit.setText(preset_file)
                self.ui.saveCheckBox.setChecked(self.config.getboolean(OTHER, SAVE))
                self.ui.radioButton.setChecked(self.config.getboolean(OTHER, ACCELERATE))
                self.ui.horizontalSlider.setValue(self.config.getfloat(OTHER, FUZZINESS))

                # 保存刚开始的预设文件路径
                self.previous_preset_file = preset_file
            except (ValueError, configparser.NoSectionError, configparser.NoOptionError, configparser.ParsingError):
                pass

        # 设置主题，并设置显示主题名称
        self.theme = set_theme(self)
        self.ui.comboBox.setCurrentText(self.theme)

        # 判断是否需要提示
        if self.ui.radioButton.isChecked():
            self.showed_info = True

    def save(self):
        """保存配置文件"""
        # 如果文件夹不存在则创建文件夹
        if not os.path.exists(CONFIG_DIR):
            os.makedirs(CONFIG_DIR)

        # 如果预设文件不存在则清空预设路径
        if not os.path.exists(self.ui.chooseFileLineEdit.text()):
            self.ui.chooseFileLineEdit.clear()

        # 创建配置
        self.config[OUT] = {
            PATH: self.ui.chooseDirLineEdit.text()
        }
        self.config[PRESET] = {
            PATH: self.ui.chooseFileLineEdit.text()
        }
        self.config[OTHER] = {
            FUZZINESS: self.ui.horizontalSlider.value(),
            THEME: self.theme,
            ACCELERATE: self.ui.radioButton.isChecked(),
            SAVE: self.ui.saveCheckBox.isChecked()
        }

        # 写入数据
        with open(SET_FILE_PATH, 'w', encoding="utf-8") as cf:
            self.config.write(cf)

    def eventFilter(self, watched, event):
        """重写方法实现窗口的拖动"""
        # 监听标题栏，并做窗口拖动处理
        if event.type() == QEvent.MouseButtonPress:
            self.clickPos = event.globalPosition() - self.pos()
        if event.type() == QEvent.MouseMove:
            if event.buttons() == Qt.LeftButton and self.clickPos:
                self.move(event.globalPosition().toPoint() - self.clickPos.toPoint())
        if event.type() == QEvent.MouseButtonRelease:
            self.clickPos = QPoint()

        return QWidget.eventFilter(self, watched, event)

    def showEvent(self, event):
        """重写显示事件实现居中显示"""
        # 居中显示
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    @Slot()
    def set_preset_path(self):
        """设置并显示预设路径"""
        previous_content = self.ui.chooseFileLineEdit.text()  # 之前的文本内容
        choose_file(
            self, "选择预设文件", EXTRA_PATH + "/预设", "预设文件 (*.%s);;所有文件 (*)" % SUFFIX,
            line_edit=self.ui.chooseFileLineEdit
        )

        # 如果更之前的文本内容不等于更改过的文本内容则执行
        if previous_content != (current_content := self.ui.chooseFileLineEdit.text()):
            self.previous_preset_file = current_content
            self.change_preset_path_signal.emit(current_content)  # 发射改变预设路径信号到主窗口

    @Slot()
    def change_theme(self):
        """改变主题，并向主窗口发射主题样式"""
        self.theme = self.ui.comboBox.currentText()
        change_theme(self, DIC_THEMES[self.ui.comboBox.currentText()])
        self.change_theme_signal.emit(self.theme)

    @Slot()
    def hide_windows(self):
        """隐藏窗口并保存配置"""
        # 导出路径
        out_path = self.ui.chooseDirLineEdit.text()
        out_path_content = out_path.replace(' ', '')

        # 判断导出路径是否存在，如果不存在并有内容，则退出关闭事件
        if not os.path.exists(out_path) and out_path_content:
            QMessageBox.warning(self, "警告", "导出路径不存在！\n请重新输入导出路径。")
            return

        # 将改变预设路径的信号发给主窗口
        if self.previous_preset_file != (preset_path := self.ui.chooseFileLineEdit.text()):
            # 判断是文本输入框里是否内容，如果有内容 ，则报错  和  判断是否存在，如果不存在，则报错
            if preset_path.replace(' ', '') and not os.path.exists(preset_path):
                QMessageBox.warning(self, "警告", "预设文件路径异常。\n请检查路径后重试！")
                return
            # 发送改变预设的消息
            self.previous_preset_file = preset_path
            self.change_preset_path_signal.emit(preset_path)

        # 将改变输出路径的信号发给主窗口
        self.change_out_path_signal.emit(out_path_content)

        # 保存配置文件
        self.save()

        # 隐藏窗口
        self.hide()


if __name__ == '__main__':
    app = QApplication([])
    main_window = ChildSetWindow()
    main_window.show()
    app.exec()
