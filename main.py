"""主逻辑"""
import threading
import webbrowser
from time import sleep, localtime, strftime

from PIL import ImageQt
from PySide6.QtGui import QMovie, QTextCursor, QIntValidator, QAction
from PySide6.QtWidgets import QMainWindow, QMenu, QColorDialog, QLabel

from ui_handwriting import Ui_MainWindow
from setWindow import *


class MainWindow(QMainWindow):
    """主窗口"""

    sand_finish_sigal = Signal(list)  # 发送导出完成的信号
    color = (0, 0, 0)  # 字体颜色RGB
    images_list = list()  # 处理后的图片
    first_pixmap = None  # 处理后的图片的第一张像素图片
    out_path = DEFAULT_OUT_PATH  # 输出路径
    load_error_msg = None  # 加载错误的信息
    preview_finishing = False  # 预设完成标志
    asked_cancel = False  # 是否询问过标志

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()

        # 初始化界面
        self.ui.setupUi(self)

        # 创建子窗口
        self.set_window = ChildSetWindow()

        # 初始化点击坐标
        self.clickPos = QPoint()

        # 初始化线程
        self.get_content = GetContentThread()  # 创建一个获取文件内容的线程
        self.set_font = None  # 一个改变字体的线程

        # 添加事件过滤器实现窗口的拖动
        self.ui.titleWidget.installEventFilter(self)  # 标题栏添加事件过滤器
        self.ui.titleWidget.setMouseTracking(True)  # 设置标题栏鼠标跟踪

        # 设置窗口样式
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗体无边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景透明

        # 设置plainEdit中最大区块数
        self.ui.plainTextEdit.setMaximumBlockCount(PLAIN_TEXT_MAX_BLOCK)

        # 创建整数校验器
        int_validator = QIntValidator(self)
        int_validator.setRange(-999, 9999)

        # 添加校验器
        self.ui.upLineEdit.setValidator(int_validator)
        self.ui.downLineEdit.setValidator(int_validator)
        self.ui.leftLineEdit.setValidator(int_validator)
        self.ui.rightLineEdit.setValidator(int_validator)

        # 设置图标及图标大小
        self.ui.setPushButton.setIconSize(QSize(20, 20))
        self.ui.minPushButton.setIconSize(QSize(20, 20))
        self.ui.closePushButton.setIconSize(QSize(20, 20))
        self.ui.setPushButton.setIcon(QPixmap("./icons/set.png"))
        self.ui.maxPushButton.setIcon(QPixmap("./icons/max.png"))
        self.ui.minPushButton.setIcon(QPixmap("./icons/min.png"))
        self.ui.closePushButton.setIcon(QPixmap("./icons/close.png"))

        # 设置按键提示标题
        self.ui.setPushButton.setToolTip("设置")
        self.ui.maxPushButton.setToolTip("最大化")
        self.ui.minPushButton.setToolTip("最小化")
        self.ui.closePushButton.setToolTip("关闭")

        # 设置等待标签动画
        self.wait_label = QLabel(self)
        self.wait_label.setFixedSize(50, 50)
        self.wait_label.move((self.width() + self.ui.previewLabel.width()) // 2 + 125, self.height() // 2 - 35)
        self.movie = QMovie("./gif/loading.gif")  # 设置gif动画
        self.wait_label.setMovie(self.movie)
        self.wait_label.setScaledContents(True)  # 设置缩放内容
        self.movie.start()  # 开启动画
        self.wait_label.hide()  # 隐藏等待标签

        # 加载预设文件
        self.load_preset()

        # 绑定对应事件
        self.signal_solt_connection()

        # 设置主题
        set_theme(self)

        # 创建帮助菜单
        self.help_menu = QMenu(self)

        # 创建动作
        self.aboutAction = QAction(self)
        self.aboutAction.setText("关于作者(&A)...")
        self.aboutAction.setShortcut("Ctrl+Shift+A")  # 快捷键
        self.aboutAction.triggered.connect(self.about)

        self.methodAction_really = QAction(self)
        self.methodAction_really.setText("如何让图片更真实？")
        self.methodAction_really.triggered.connect(self.really)

        self.methodAction_use = QAction(self)
        self.methodAction_use.setText("如何使用该程序？")
        self.methodAction_use.triggered.connect(self.use)

        # 添加动作到菜单
        self.help_menu.addActions([
            self.methodAction_use,
            self.methodAction_really,
            self.help_menu.addSeparator(),
            self.aboutAction,
        ])
        self.ui.helpPushButton.setMenu(self.help_menu)  # 绑定菜单

    def signal_solt_connection(self):
        """绑定事件"""

        @Slot()
        def change_file_button():
            """改变按钮"""
            if not self.ui.fileLineEdit.text().replace(' ', ''):
                text = CHOOSE_TEXT
            else:
                text = EXTRACT_TEXT

            self.ui.filePushButton.setText(text)

        @Slot()
        def check_content_num():
            """检查输入内容的数量和行数"""
            if len(self.ui.plainTextEdit.toPlainText()) > PLAIN_TEXT_MAX_INPUT:
                self.ui.plainTextEdit.setPlainText(self.ui.plainTextEdit.toPlainText()[:PLAIN_TEXT_MAX_INPUT])
                self.ui.plainTextEdit.moveCursor(QTextCursor.End)  # 把光标移到最后
                QMessageBox.information(self, "提示", "最大只能输入%d个字符" % PLAIN_TEXT_MAX_INPUT)

        @Slot()
        def check_blockCount():
            """检查块数给予提示"""
            if all([
                self.ui.plainTextEdit.blockCount() == PLAIN_TEXT_MAX_BLOCK,
                len(self.ui.plainTextEdit.toPlainText()) <= PLAIN_TEXT_MAX_INPUT
            ]):
                QMessageBox.information(self, "提示", "最大换行次数为%d次" % PLAIN_TEXT_MAX_BLOCK)

        @Slot()
        def check_margin(line_edit):
            """检查边距输入，并替换为适合的格式"""
            line_edit.setText(str(int(line_edit.text())))

        @Slot()
        def asking_cancel(state):
            """询问是否取消美化"""
            # 判断状态和是否已经询问过
            if not state and not self.asked_cancel:
                self.ui.optimizeCheckBox.setChecked(True)
                content = "确定要关闭美化功能吗？\n" \
                          "该功能可以优化图片中字体和背景\n" \
                          "但处理过程会慢一些。"
                if self.info_msg(content):
                    self.asked_cancel = True
                    self.ui.optimizeCheckBox.setChecked(False)

        self.ui.optimizeCheckBox.toggled.connect(asking_cancel)

        self.ui.closePushButton.clicked.connect(self.close_event)
        self.ui.maxPushButton.clicked.connect(self.change_window)
        self.ui.minPushButton.clicked.connect(self.minimized)
        self.ui.setPushButton.clicked.connect(self.show_set_window)
        self.ui.colorPushButton.clicked.connect(self.choose_color)
        self.ui.previewPushButton.clicked.connect(self.preview_image)
        self.ui.outputPushButton.clicked.connect(self.output_image)
        self.ui.filePushButton.clicked.connect(self.file_button_clicked)

        self.ui.fileLineEdit.textChanged.connect(change_file_button)
        self.ui.plainTextEdit.textChanged.connect(check_content_num)
        self.ui.plainTextEdit.blockCountChanged.connect(check_blockCount)
        self.ui.upLineEdit.editingFinished.connect(lambda: check_margin(self.ui.upLineEdit))
        self.ui.leftLineEdit.editingFinished.connect(lambda: check_margin(self.ui.leftLineEdit))
        self.ui.downLineEdit.editingFinished.connect(lambda: check_margin(self.ui.downLineEdit))
        self.ui.rightLineEdit.editingFinished.connect(lambda: check_margin(self.ui.rightLineEdit))

        self.ui.bgPushButton.clicked.connect(lambda: choose_file(
            self, "选择图片", EXTRA_PATH + "/背景", "图片类型 (*.png *.jpg *.bmp *.jpeg);;所有文件 (*)",
            line_edit=self.ui.bgLineEdit
        ))
        self.ui.fontPushButton.clicked.connect(lambda: choose_file(
            self, "选择字体文件", EXTRA_PATH + "/字体", "文件类型 (*.ttf);;所有文件 (*)", line_edit=self.ui.fontLineEdit
        ))

    def load_preset(self, path=None):
        """加载预设"""

        def set_value():
            """ 设置文本框内容"""
            # path
            self.ui.bgLineEdit.setText(content[0])
            self.ui.fontLineEdit.setText(content[1])

            # font
            self.ui.sizeSpinBox.setValue(content[2])
            self.ui.horizontalSpinBox.setValue(content[3])
            self.ui.verticalSpinBox.setValue(content[4])
            self.ui.sizeDoubleSpinBox.setValue(content[5])
            self.ui.horDoubleSpinBox.setValue(content[6])
            self.ui.verDoubleSpinBox.setValue(content[7])
            self.ui.rHorDoubleSpinBox.setValue(content[8])
            self.ui.rVerDoubleSpinBox.setValue(content[9])
            self.ui.rRotatedoubleSpinBox.setValue(content[10])

            # background
            self.ui.upLineEdit.setText(content[11])  # 测试转int时会不会报错
            self.ui.downLineEdit.setText(content[12])
            self.ui.leftLineEdit.setText(content[13])
            self.ui.rightLineEdit.setText(content[14])

        # 加载错误的标记
        self.load_error_msg = None

        # 判断配置文件路径
        if path is None:
            try:
                # 读取配置文件
                (config := configparser.ConfigParser()).read(SET_FILE_PATH, encoding="utf-8")

                # 获取配置文件路径
                preset_path = config.get(PRESET, PATH)
            except (configparser.NoSectionError,
                    configparser.NoOptionError,
                    configparser.ParsingError):
                return
        else:
            preset_path = path

        # 判断路径是否为空，则退出
        if not preset_path:
            return

        # 设置内容
        content = self.get_preset_content(preset_path)  # 获取文件内容
        try:
            set_value()  # 设置内容
        except TypeError:
            pass

    def get_preset_content(self, preset_path):
        """读取预设文件"""
        try:
            # 读取文件，并设置内容
            with open(preset_path, 'r', encoding="utf-8") as file:
                # 读取文件
                content = [i.replace("\n", '') for i in file.readlines()]

                # 断言最后一行是'True'或'False'
                assert content[-1] in ["True", "False"]

                # 判断有自定义标志
                dirname = ''
                is_customize = True if content[-1] == "True" else False
                if not is_customize:
                    dirname = os.getcwd()  # 获取当前程序文件夹路径

                # path
                line1 = ''
                line2 = ''
                if content[0]:
                    line1 = ''.join([dirname, content[0]]).replace("\\", "/")
                if content[1]:
                    line2 = ''.join([dirname, content[1]]).replace("\\", "/")

                # font
                line3 = int(content[2])
                line4 = int(content[3])
                line5 = int(content[4])
                line6 = float(content[5])
                line7 = float(content[6])
                line8 = float(content[7])
                line9 = float(content[8])
                line10 = float(content[9])
                line11 = float(content[10])

                # background
                line12 = str(int(content[11]))  # 测试转int时会不会报错
                line13 = str(int(content[12]))
                line14 = str(int(content[13]))
                line15 = str(int(content[14]))

                return (
                    line1, line2, line3, line4, line5, line6, line7,
                    line8, line9, line10, line11, line12, line13, line14,
                    line15
                )
        except (PermissionError, FileNotFoundError):
            self.load_error_msg = "预设文件不存在或无法访问该文件！"
        except (IndexError, ValueError, AssertionError):
            self.load_error_msg = "预设文件异常，无法完整加载内容！"

    def check_error(self, window):
        """检查是否加载出错"""
        if self.load_error_msg is not None:
            msg = "请在 \"设置\"->\"预设\" 里修改预设文件路径"
            QMessageBox.warning(window, "警告", self.load_error_msg + "\n" + msg)

    def check_path_and_content(self):
        """检查背景/字体路径和输入的内容"""

        def show_warning(inform):
            """显示警告信息"""
            QMessageBox.warning(self, "警告", "%s路径有误！\n请检查路径后重试。" % inform)

        # 获取背景图片路径
        bg_path = self.ui.bgLineEdit.text()
        # 获取字体文件路径
        font_path = self.ui.fontLineEdit.text()

        # 判断文本框中所给路径是否存在
        if not os.path.exists(bg_path):
            show_warning("背景图片")
            return
        if not os.path.exists(font_path):
            show_warning("字体文件")
            return

        # 获取输入的文本，并判断文本内容
        text = self.ui.plainTextEdit.toPlainText()
        if not text.replace(' ', ''):
            QMessageBox.information(self, "提示", "文本框中没有文字！\n请输入文字后重试。")
            return

        # 判断边距输入内容
        self.check_margin_lineEdit(self.ui.upLineEdit)
        self.check_margin_lineEdit(self.ui.downLineEdit)
        self.check_margin_lineEdit(self.ui.leftLineEdit)
        self.check_margin_lineEdit(self.ui.rightLineEdit)

        return bg_path, font_path, text

    def info_msg(self, content, ok_mode=True):
        """自定义弹出显示"""
        inform = QMessageBox()
        inform.setWindowIcon(self.windowIcon())
        inform.setStyleSheet(self.styleSheet())
        inform.setWindowTitle("提示")
        inform.setIcon(QMessageBox.Information)
        inform.setText(content)
        inform.addButton("确认", QMessageBox.AcceptRole)  # 添加自定义按钮
        if ok_mode:
            inform.addButton(CANCEL, QMessageBox.RejectRole)
            ok_pressed = inform.exec()  # 返回选中按钮的值
            if ok_pressed == QMessageBox.AcceptRole:
                return True
            elif ok_pressed == QMessageBox.RejectRole:
                return False

        else:
            inform.setTextInteractionFlags(Qt.TextSelectableByMouse)  # 设置文本可被选中
            inform.exec()  # 阻塞主窗口并执行弹窗

    def font_handler(self, func):
        """处理文字并且融合背景"""
        # 获取数据
        bg_path, font_path, text = self.check_path_and_content()

        # 创建一个改变字体的线程
        self.set_font = FontHandlerThread()
        self.set_font.ui = self.ui
        self.set_font.window = self

        # 开启处理字体的线程
        self.set_font.signal.connect(func)
        self.set_font.text = text
        self.set_font.bg_path = bg_path
        self.set_font.font_path = font_path
        self.set_font.start()  # 启动线程

    def set_enable(self, is_enable=False, loading=False):
        """显示/隐藏 加载中图标，并 禁用/启用 部件"""
        # 禁用/启用 部件
        self.ui.setPushButton.setEnabled(is_enable)
        self.ui.vagueCheckBox.setEnabled(is_enable)
        self.ui.optimizeCheckBox.setEnabled(is_enable)
        self.ui.outputPushButton.setEnabled(is_enable)
        self.ui.previewPushButton.setEnabled(is_enable)

        # 根据状态判断是否显示加载图标和切换按钮文本
        if not is_enable and loading:
            self.wait_label.show()  # 显示加载中图标
            self.ui.outputPushButton.setText(CANCEL)  # 切换为取消按钮
        else:
            self.wait_label.hide()  # 隐藏加载中图标
            self.ui.outputPushButton.setText(OUT_TEXT)  # 切换为预设按钮

    def save_to_preset(self):
        """保存为预设"""

        def save():
            """保存文件"""
            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "保存文件",
                EXTRA_PATH + PREVIEW,
                "预设文件 (*.%s)" % SUFFIX
            )

            return file_path

        def write(path):
            """输出预设文件"""
            # 检查文件夹是否存在
            check_extra_dir()

            # 写入文件
            with open(path, 'w', encoding="utf-8") as f:
                content = ''

                # path
                if self.ui.bgLineEdit.text():
                    content += line1 + "\n"
                else:
                    content += "\n"
                if self.ui.bgLineEdit.text():
                    content += line2 + "\n"
                else:
                    content += "\n"

                # font
                content += str(line3) + "\n"
                content += str(line4) + "\n"
                content += str(line5) + "\n"
                content += str(line6) + "\n"
                content += str(line7) + "\n"
                content += str(line8) + "\n"
                content += str(line9) + "\n"
                content += str(line10) + "\n"
                content += str(line11) + "\n"

                # background
                content += line12 + "\n"
                content += line13 + "\n"
                content += line14 + "\n"
                content += line15 + "\n"

                # 自定义预设的标记
                content += "True" + "\n"

                f.write(content)

            self.info_msg("保存成功！\n保存至：\n%s" % path.replace('/', "\\"), False)

        def check_content():
            """检查预设文件内容和输入的内容是否相同"""
            # 如果预设文件输入框里内容为空或预设文件输入框里文件不存在，则返回false
            if not (path := self.set_window.ui.chooseFileLineEdit.text()) or not os.path.exists(path):
                return False

            # 读取预设文件内容并判断是否有报错
            self.load_error_msg = None
            content = self.get_preset_content(path)  # 获取预设文件内容
            if self.load_error_msg:
                return False

            # 判断是否可以匹配到所有的字符
            if (line1, line2, line3, line4, line5, line6, line7, line8, line9,
                    line10, line11, line12, line13, line14, line15) == content:
                return True

            return False

        # 判断边距输入内容
        self.check_margin_lineEdit(self.ui.upLineEdit)
        self.check_margin_lineEdit(self.ui.downLineEdit)
        self.check_margin_lineEdit(self.ui.leftLineEdit)
        self.check_margin_lineEdit(self.ui.rightLineEdit)

        # 获取文本中内容
        line1 = self.ui.bgLineEdit.text()
        line2 = self.ui.fontLineEdit.text()
        line3 = int(self.ui.sizeSpinBox.value())
        line4 = int(self.ui.horizontalSpinBox.value())
        line5 = int(self.ui.verticalSpinBox.value())
        line6 = float(self.ui.sizeDoubleSpinBox.value())
        line7 = float(self.ui.horDoubleSpinBox.value())
        line8 = float(self.ui.verDoubleSpinBox.value())
        line9 = float(self.ui.rHorDoubleSpinBox.value())
        line10 = float(self.ui.rVerDoubleSpinBox.value())
        line11 = float(self.ui.rRotatedoubleSpinBox.value())
        line12 = self.ui.upLineEdit.text()
        line13 = self.ui.downLineEdit.text()
        line14 = self.ui.leftLineEdit.text()
        line15 = self.ui.rightLineEdit.text()

        # 判断文本的内容和输入的内容是否相同
        if check_content():
            return

        # 询问是否保存
        if not self.info_msg("是否保存此设置为预设文件？"):
            return

        # 弹出保存窗口，并判断是否选择了文件
        if not (file := save()):
            return

        # 写入文件
        write(file)

    def eventFilter(self, watched, event):
        """重写方法实现窗口的拖动"""
        # 监听标题栏，并做窗口拖动处理
        if event.type() == QEvent.MouseButtonDblClick:
            # 如果鼠标双击，则改变窗口
            self.change_window()
        if event.type() == QEvent.MouseButtonPress:
            self.clickPos = event.globalPosition() - self.pos()
        if event.type() == QEvent.MouseMove:
            if event.buttons() == Qt.LeftButton and self.clickPos and not self.isMaximized():
                self.move(event.globalPosition().toPoint() - self.clickPos.toPoint())
            elif event.buttons() == Qt.LeftButton and self.clickPos and self.isMaximized():
                scale = self.clickPos.x() / self.width()
                self.change_window()
                scale -= 0.105 if scale > 0.75 else 0
                scale += 0.105 if 0.09 < scale < 0.25 else 0
                self.clickPos.setX(self.width() * scale)
                self.clickPos.setY(self.clickPos.y() + 8)
        if event.type() == QEvent.MouseButtonRelease:
            self.clickPos = QPoint()

        return QWidget.eventFilter(self, watched, event)

    def keyPressEvent(self, key_event):
        # 判断是否按下Ctrl+S
        if key_event.modifiers() == Qt.ControlModifier and key_event.key() == Qt.Key_S:
            self.save_to_preset()

    def closeEvent(self, event):
        """关闭事件"""
        # 判断是否有线程在执行
        if len(threading.enumerate()) - 1:
            if not self.info_msg("还有程序在后台运行中，可能正在写入图片\n确定要退出程序吗？"):
                event.ignore()
                return

        # 检查是否勾选提示并且回答为真
        if self.set_window.ui.saveCheckBox.isChecked():
            self.save_to_preset()  # 保存为预设

    @Slot()
    def output_image(self):
        """导出图片"""

        def out():
            """直接输出图片"""
            for i, image in enumerate(self.images_list):
                file_path = '/'.join([path, file + "(%d).png" % (i + 1)])
                image.save(file_path)

            # 发送完成消息
            self.sand_finish_sigal.emit(self.images_list)

        def out_finish(pictures):
            """导出完成"""
            file_msg = "<br>图片数：共%d张图片" % (picture_num := len(pictures))
            if picture_num == 1:
                file_msg = "<br>文件名：%s.png(1)" % file
            out_info = "导出成功！<br>保存至：%s%s%s<br><b>可以用鼠标选取文本</b>" % (path, file_msg, info)
            self.info_msg(out_info, False)
            self.set_enable(True)

            # 解除绑定
            try:
                self.sand_finish_sigal.disconnect(out_finish)
            except RuntimeError:
                pass

        @Slot(list)
        def font_finish(images: list):
            """字体处理完成"""

            def save(num):
                """保存图片"""
                sleep(num / 2)
                im.save("{}/{}({}).png".format(path, file, num + 1))

            for j, im in enumerate(images):
                threading.Thread(target=save, args=(j,)).start()  # 创建保存图片的线程，防止阻塞窗口
            out_finish(images)
            self.set_font.signal.disconnect(font_finish)  # 解除锁定

        # 判断预设按钮文本
        if self.ui.outputPushButton.text() == CANCEL and not self.preview_finishing:
            if self.set_font.isRunning():
                close_child_process()  # 清理子进程
                self.set_font.terminate()  # 停止线程
                del self.set_font
                self.set_enable(True)
                return

        info = ''
        # 判断导出路径是否有内容
        path = self.set_window.ui.chooseDirLineEdit.text().replace('\\', "/")
        if not path.replace(' ', ''):
            path = os.getcwd()
            info = "<br>小提示：可以在设置 \"设置\"->\"导出路径\" 里修改导出路径"
        else:
            # 判断输出路径是否存在
            if not os.path.exists(path):
                msg = "导出文件夹不存在！\n请修改路径后重试\n\"设置\"->\"导出路径\""
                QMessageBox.critical(self, "错误", msg)
                return

        # 拼装文件名
        file = strftime("手写模拟器_%Y%m%d%H%M%S", localtime())

        # 判断是否有预览图片
        if self.images_list:
            self.set_enable()  # 设置部件禁用
            self.sand_finish_sigal.connect(out_finish)
            threading.Thread(target=out).start()
            return
        else:
            if not self.info_msg("确定不先预览再导出吗"):
                return

        # 判断字体大小进行提示
        if self.ui.sizeSpinBox.value() > 350 and \
                self.info_msg("文字过大，350的字体大小已经足够了\n字体太大可能会导致处理缓慢\n是否将字体大小改为350"):
            self.ui.sizeSpinBox.setValue(350)

        # 检查是否可以正常获取并开启线程
        try:
            self.font_handler(font_finish)
        except TypeError:
            return

        # 禁用部件
        self.set_enable()

    @Slot()
    def preview_image(self):
        """预览图片"""

        def release():
            """等待0.7秒后释放取消按钮"""
            sleep(0.7)
            # 判断状态
            if (cancel_button := self.ui.outputPushButton).text() == CANCEL:
                cancel_button.setEnabled(True)  # 释放按钮

        @Slot()
        def finish(images):
            """处理完成"""
            self.preview_finishing = True

            # 判断images第一个元素是否为str类型，为str说明报错了
            if isinstance(images[0], str):
                if len(images) == 2:
                    bg_size = images[1]
                    msg = "请根据提示核对参数！\n提示：\n%s\n当前背景图片信息：高度:%d   宽度:%d" % (
                        images[0], bg_size[0], bg_size[1])
                    QMessageBox.critical(self, "布局错误", msg)
                elif len(images) == 1:
                    QMessageBox.critical(self, "错误", images[0])
                self.set_enable(True)
                return

            # 设置图片
            self.images_list = images
            self.first_pixmap = ImageQt.toqpixmap(images[0])

            # 饱和式填满图片
            self.ui.previewLabel.setPixmap(
                self.first_pixmap.scaled(self.ui.previewLabel.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            )

            # 判断图片数量，并给予提示
            if len(images) > 1:
                QMessageBox.information(self, "提示",
                                        "图片数量共有%d个\n无法预览所有图片，可以导出图片进行查看" % len(images))

            self.set_enable(True)

        # 检查是否可以正常获取内容并开启线程
        try:
            self.font_handler(finish)
        except TypeError:
            return

        # 完成标志为否
        self.preview_finishing = False

        # 释放取消按钮
        threading.Thread(target=release).start()

        # 禁用部件
        self.set_enable(loading=True)

    @Slot()
    def file_button_clicked(self):
        """filePushButton被点击，根据文本内容切换事件"""

        def disconnect_signal():
            """解除信号绑定和禁用的部件"""
            try:
                set_enable(True)
                self.get_content.signal.disconnect(change_text)
                self.get_content.error_signal.disconnect(show_message)
            except RuntimeError:
                pass

        def set_enable(is_enable=False):
            """禁用部件和释放部件"""
            self.ui.filePushButton.setEnabled(is_enable)
            if is_enable:
                self.ui.plainTextEdit.setStyleSheet('')
            else:
                self.ui.plainTextEdit.setStyleSheet("color:rgb(79,91,98)")

        @Slot()
        def change_text(file_content):
            """根据子线程发送的内容修改plainTextEdit里的内容"""
            self.ui.plainTextEdit.setPlainText(file_content)
            disconnect_signal()

        @Slot()
        def show_message(title, msg, is_warning):
            """根据子线程发送的内容启动不同的提示窗口"""
            if is_warning:
                QMessageBox.information(self, title, msg)
            else:
                QMessageBox.critical(self, title, msg)
            disconnect_signal()

        if self.ui.filePushButton.text() == CHOOSE_TEXT:
            choose_file(self, CHOOSE_TEXT, None, "*.txt  *.pdf  *.docx", line_edit=self.ui.fileLineEdit)
        elif self.ui.filePushButton.text() == EXTRACT_TEXT:
            set_enable()
            self.ui.fileLineEdit.setFocus()  # 防止文本关标跑入下一个控件
            self.get_content.signal.connect(change_text)
            self.get_content.error_signal.connect(show_message)
            self.get_content.window = self
            self.get_content.start()  # 启动线程

    @Slot()
    def show_set_window(self):
        """显示设置窗口"""

        @Slot()
        def set_out(path):
            """接受子窗口发出的更改输出路径信号"""
            if not path:
                self.out_path = None
            else:
                self.out_path = path
            self.set_window.change_out_path_signal.disconnect(set_out)  # 解除信号，防止信号递归调用

        @Slot()
        def preset_path(path):
            """接受子窗口发出的更改预设路径信号"""
            # 判断是否是文件，如果是文件则加载预设
            if os.path.isfile(path):
                self.load_preset(path)
                self.check_error(self.set_window)
            else:
                self.set_window.ui.chooseFileLineEdit.setText('')

        self.set_window.show()
        self.set_window.change_out_path_signal.connect(set_out)  # 连接更改输出路径信号
        self.set_window.change_preset_path_signal.connect(preset_path)  # 连接更改预设路径信号
        self.set_window.change_theme_signal.connect(lambda data: change_theme(self, DIC_THEMES[data]))  # 更改主题

    @Slot()
    def choose_color(self):
        """弹出颜色选择对话框，并设置文本内容"""
        col = QColorDialog().getColor()

        # 判断是否选择了颜色
        if not col.isValid():
            return

        col_name = col.name()  # 获取选中的颜色名称
        col_rgb = col.getRgb()[0:3]  # 字体rgb颜色

        # 判断颜色是否为白色
        if min(col_rgb) >= 225:
            QMessageBox.warning(self, "提示", "无法选择偏白色字体")
            return

        self.color = col_rgb
        self.ui.label.setText("字体")

        # 根据颜色显示不同样式
        if col_name == "#31363b":
            col_name = "#ffffff"
            self.ui.label.setText("字体->背景色")
        if col_name == "#000000":
            col_name = "#ffffff"
            self.ui.label.setText("字体->纯黑色")
        self.ui.label.setStyleSheet("color:%s" % col_name)  # 设置显示的字体颜色

    @Slot()
    def minimized(self):
        """最小化"""
        self.showMinimized()

    @Slot()
    def change_window(self):
        """最大化与复原"""
        if self.isMaximized():
            self.showNormal()
            self.ui.maxPushButton.setIcon(QPixmap("./icons/max.png"))
            self.ui.maxPushButton.setToolTip("最大化")
        else:
            self.showMaximized()
            self.ui.maxPushButton.setIcon(QPixmap("./icons/restore_down.png"))
            self.ui.maxPushButton.setToolTip("向下还原")

        # 等待图标的位置变化
        self.wait_label.move((self.width() + self.ui.previewLabel.width()) // 2 - 10, self.height() // 2 - 35)
        # 改变图片，不管窗口的放大缩小都保持饱满显示
        if self.images_list:
            self.ui.previewLabel.setPixmap(
                self.first_pixmap.scaled(self.ui.previewLabel.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            )

    @Slot()
    def close_event(self):
        """关闭程序"""
        self.close()

    @Slot()
    def about(self):
        """关于信息"""
        QMessageBox.about(self, "关于作者", ABOUT)

    @Slot()
    def really(self):
        """启动帮助视屏"""

        # 判断是否关闭美化功能
        if not (checkBox := self.ui.optimizeCheckBox).isChecked():
            if self.info_msg("是否开启美化功能？\n建议开启美化功能输出图片，效果更佳。"):
                checkBox.setChecked(True)

        # 打开本地视屏文件
        try:
            threading.Thread(target=lambda: os.startfile(HELP_PATH + "图片更真实.mp4")).start()
            sleep(0.6)
            QMessageBox.information(self, "提示", "启动成功！")
        except FileNotFoundError:
            QMessageBox.critical(self, "错误", "启动失败，文件不存在！")

    @Slot()
    def use(self):
        """启动帮助视屏"""
        webbrowser.open(URL)

    @staticmethod
    def check_margin_lineEdit(lineEdit):
        """检查并修改边框输入栏里的文本"""
        content = lineEdit.text()
        if not content:
            content = 0
        lineEdit.setText(str(int(content)))


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    main_window.check_error(main_window)
    app.exec()

    # 清理进程并关闭程序
    close_child_process()
    os._exit(0)
