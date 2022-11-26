"""其他功能"""
import configparser
import multiprocessing

import psutil
import handright
from qt_material import apply_stylesheet
from PIL import ImageFont, UnidentifiedImageError
from PySide6.QtCore import Signal, QThread
from PySide6.QtWidgets import QMessageBox, QFileDialog
from docx.opc.exceptions import PackageNotFoundError
from pdfminer.pdfdocument import PDFPasswordIncorrect, PDFSyntaxError

from config import *
from imageHandler import *
from documentManipulation import *


def choose_file(window, message, target=None, file_type=None, file=True, line_edit=None) -> None:
    """选择文件或文件夹
    :param window: 窗口对象
    :param message: 标题
    :param target: 起始目录
    :param file_type: 选择类型过滤项
    :param file: 是否是文件的标志   True表示文件   False 表示文件夹
    :param line_edit: QLineEdit对象
    """
    # 检查文件夹是否存在
    check_extra_dir()

    if not file:
        file_path = QFileDialog.getExistingDirectory(window, message)
    else:
        file_path = QFileDialog.getOpenFileName(window, message, target, file_type)[0]

    if line_edit is not None and file_path:
        line_edit.setText(file_path)


def change_theme(window, theme) -> None:
    """更改主题"""
    apply_stylesheet(window, theme)
    style_file = "resource/handwriting.qss"
    if window.__class__.__name__ == "ChildSetWindow":
        style_file = "resource/set_win.qss"
    try:
        with open(style_file) as file:
            window.setStyleSheet(window.styleSheet() + file.read())
    except FileNotFoundError:
        QMessageBox.critical(window, "文件丢失", "样式文件缺失！")


def set_theme(window) -> str:
    """读取配置文件，设置主题"""
    try:
        config = configparser.ConfigParser()
        config.read(SET_FILE_PATH, encoding="utf-8")
        theme = config.get(OTHER, THEME)
        theme_name = DIC_THEMES[theme]
    except (KeyError,
            configparser.NoSectionError,
            configparser.NoOptionError,
            configparser.ParsingError):
        theme = DEFAULT_THEME
        theme_name = DIC_THEMES[theme]

    change_theme(window, theme_name)
    return theme


def check_extra_dir() -> None:
    """检查extra文件夹是否存在"""
    if not os.path.exists(EXTRA_PATH):
        os.mkdir(EXTRA_DIR)
    if not os.path.exists(EXTRA_PATH + "字体"):
        os.mkdir(EXTRA_PATH + "字体")
    if not os.path.exists(EXTRA_PATH + "背景"):
        os.mkdir(EXTRA_PATH + "背景")
    if not os.path.exists(EXTRA_PATH + "预设"):
        os.mkdir(EXTRA_PATH + "预设")


def close_child_process() -> None:
    """关闭子进程"""
    for child in psutil.Process().children(recursive=True):
        if child.is_running():
            try:
                child.terminate()
            except psutil.NoSuchProcess:
                continue


class FontHandlerThread(QThread):
    """用于根据文本生成字体融合背景的线程"""

    signal = Signal(list)
    ui = None
    text = None
    window = None
    bg_path = None
    font_path = None

    def __init__(self):
        super().__init__()

    def beautify_image(self, image: Image.Image) -> Image.Image:
        """按照要求美化图片"""
        # 判断选型，处理图片
        if self.ui.optimizeCheckBox.isChecked():
            image = beautify(image)  # 图片美化
        if self.ui.vagueCheckBox.isChecked():
            image = gaussian_blur(image, self.window.set_window.ui.horizontalSlider.value() / 10)  # 高斯模糊

        return image

    def font_handler(self, template, mapper=None) -> list:
        """字体处理"""
        images_list = []
        try:
            # 断言template属于Template
            assert isinstance(template, handright.Template)

            # 判断处理方式
            if mapper is None:
                images = handright.handwrite(self.text, template)
            else:
                images = handright.handwrite(self.text, template, mapper=mapper)

            for i, im in enumerate(images):
                im = im.convert("RGBA")
                images_list.append(self.beautify_image(im))
        except handright.LayoutError as k:
            return [ERROR_MSG[str(k)], Image.open(self.bg_path).size]
        except AssertionError:
            return [template]

        return images_list

    def run(self):
        images = None
        font_size = self.ui.sizeSpinBox.value()
        line_spacing = self.ui.verticalSpinBox.value()
        left_margin = int(self.ui.leftLineEdit.text())
        top_margin = int(self.ui.upLineEdit.text())
        right_margin = int(self.ui.rightLineEdit.text())
        bottom_margin = int(self.ui.downLineEdit.text())
        word_spacing = self.ui.horizontalSpinBox.value()
        line_spacing_sigma = self.ui.verDoubleSpinBox.value()
        font_size_sigma = self.ui.sizeDoubleSpinBox.value()
        word_spacing_sigma = self.ui.horDoubleSpinBox.value()
        perturb_x_sigma = self.ui.rHorDoubleSpinBox.value()
        perturb_y_sigma = self.ui.rVerDoubleSpinBox.value()
        perturb_theta_sigma = self.ui.rRotatedoubleSpinBox.value()

        # 按照需求改变字体
        try:
            template = handright.Template(
                background=Image.open(self.bg_path),
                font=ImageFont.truetype(self.font_path, size=font_size),
                line_spacing=line_spacing + font_size,
                fill=self.window.color,
                left_margin=left_margin,
                top_margin=top_margin,
                right_margin=(right_margin - word_spacing) * 2,
                bottom_margin=bottom_margin,
                word_spacing=word_spacing,
                line_spacing_sigma=line_spacing_sigma,  # 行间距随机扰动
                font_size_sigma=font_size_sigma,  # 字体大小随机扰动
                word_spacing_sigma=word_spacing_sigma,  # 字间距随机扰动
                end_chars="，。",  # 防止特定字符因排版算法的自动换行而出现在行首
                perturb_x_sigma=perturb_x_sigma,  # 笔画横向偏移随机扰动
                perturb_y_sigma=perturb_y_sigma,  # 笔画纵向偏移随机扰动
                perturb_theta_sigma=perturb_theta_sigma,  # 笔画旋转偏移随机扰动
            )
        except PermissionError:
            template = "程序没有权限访问字体或背景文件，\n请检查权限后重试！"
        except UnidentifiedImageError:
            template = "无法识别此类型的图片或图片已损坏。\n请检查背景图片文件！"
        except OSError:
            template = "不支持此类型的字体文件或文件已损坏。\n请检查字体文件！"

        # 清理进程
        close_child_process()

        # 判断是否用多核处理
        if self.window.set_window.ui.radioButton.isChecked():
            free_percent = float((mem := psutil.virtual_memory()).free) / float(mem.total)  # 计算空闲内存占比
            product = font_size * len(self.text) // 100
            if any([
                free_percent > 0.28 and product >= 938,
                free_percent > 0.35 and product >= 800,
                free_percent > 0.40 and product >= 720,
                free_percent > 0.50 and product >= 500
            ]):
                with multiprocessing.Pool() as p:
                    images = self.font_handler(template, p.map)

        # 普通处理
        if images is None:
            images = self.font_handler(template)

        self.signal.emit(images)


class GetContentThread(QThread):
    """用于获取文件内容的子线程"""

    signal = Signal(str)
    error_signal = Signal(str, str, bool)
    is_size_error = False
    window = None

    def __init__(self):
        super().__init__()

    def run(self):
        def determine_file_size(size):
            """判断文件大小"""
            if os.stat(path).st_size > size:
                self.error_signal.emit("提示", "文件内容过大（>{}KB），无法加载！".format(size >> 10), True)
                self.is_size_error = True
                return self.is_size_error

        # 判断文件是否存在，不存在则报错
        path = self.window.ui.fileLineEdit.text()
        if not os.path.exists(path):
            self.error_signal.emit("错误", "文件不存在！", False)
            return

        # 判断文件类型和文件大小，不符合条件则跳出
        content = ''
        self.is_size_error = False
        suffix = os.path.splitext(path)[-1]
        try:
            if "txt" in suffix and not determine_file_size(9 << 10):
                with open(path, 'r', encoding="utf-8") as f:  # 获取txt文件内容
                    content = f.read()
            elif "pdf" in suffix and not determine_file_size(800 << 10):
                content = extract_pdf_content(path)  # 获取PDF文件内容
            elif "docx" in suffix and not determine_file_size(100 << 10):
                content = extract_docx_content(path)  # 获取docx文件内容
        except PDFSyntaxError:
            self.error_signal.emit("错误", "文件已损坏，无法正常读取内容！", False)
            return
        except PDFPasswordIncorrect:
            self.error_signal.emit("错误", "PDF文件有密码保护，无法读取内容！", False)
            return
        except PackageNotFoundError:
            msg = "无法正常获取docx文件内容，原因如下：\n" \
                  "1、文档内容损坏\n2、文档有密码保护\n" \
                  "3、文档里没有内容\n4、程序没有访问该文件的权限" \
                  "\n5、通过改后缀的方式将.doc或其他文件的后缀改成了.docx\n......\n" \
                  "\n解决方法：\n1、更改文档名字\n2、取消文档密码\n3、将要转换的内容直接复制到文本框中\n......"
            self.error_signal.emit("错误", msg, False)
            return
        except UnicodeDecodeError:
            self.error_signal.emit("错误", "文件内容异常无法读取文件。", False)
            return

        if not self.is_size_error:
            self.signal.emit(content)
