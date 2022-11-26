"""配置程序中用到的常量"""
import os
from qt_material import list_themes
from multiprocessing import cpu_count

# MainWindow
CANCEL = "取消"
PREVIEW = "预设"
OUT_TEXT = "导出"
CHOOSE_TEXT = "选择文件"
EXTRACT_TEXT = "提取内容"

CONFIG_DIR = "config"
SUFFIX = "swpst"
DEFAULT_OUT_PATH = "output"
EXTRA_DIR = "extra"
EXTRA_PATH = ''.join([os.getcwd(), "\\%s\\" % EXTRA_DIR])
HELP_PATH = ''.join([os.getcwd(), "\\%s\\" % "help"])

PLAIN_TEXT_MAX_BLOCK = 230
PLAIN_TEXT_MAX_INPUT = 5000

URL = "https://www.bilibili.com/video/BV1224y1C7pu/"

ACCELERATE_MESSAGE = """
开启后处理图片时会使用电脑中所有处理器<br>
从而加快处理速度，处理器越多效果越好<br>
但处理过程中可能会出现电脑卡顿的状况<br>
<b>推荐用于字体和文本需求量较大时使用</b><br>
检查到电脑中共有%d个处理器
""" % cpu_count()

DOCX_ERROR_MSG = "无法正常获取docx文件内容，原因如下：\n" \
                 "1、文档内容损坏\n2、文档有密码保护\n" \
                 "3、文档里没有内容\n4、程序没有访问该文件的权限" \
                 "\n5、通过改后缀的方式将.doc或其他文件的后缀改成了.docx\n......\n" \
                 "\n解决方法：\n1、更改文档名字\n2、取消文档密码\n3、将要转换的内容直接复制到文本框中\n......"

ABOUT = """
<b>版本V1.0</b>
<p>作者主页：</p>
csdn：<a href="https://blog.csdn.net/python_sy" style="color:#00ffff">https://blog.csdn.net/python_sy</a><p>
哔哩哔哩：
<a href="https://space.bilibili.com/1751814864" style="color:#00ffff">https://space.bilibili.com/1751814864</a></p>
<p><b>感谢大家支持！</b></p>
"""

# 错误信息的翻译
ERROR_MSG = {
    "for (font.size > line_spacing)": "字体大小 < 行间距",
    "for (word_spacing <= -font.size // 2)": "字间距 > -字体大小 // 2",
    "for (width < left_margin + font.size + right_margin)": "背景宽度 > 左边距+ 右边距 + 字体大小 ",
    "for (height < top_margin + line_spacing + bottom_margin)": "背景高度 > 上边距 + 下边距 + 行间距 "
}


# SetWindow
SET_FILE_NAME = "set.config"
SET_FILE_PATH = '/'.join([CONFIG_DIR, SET_FILE_NAME])

OUT = "OUT"
OTHER = "OTHER"
PRESET = "PRESET"

PATH = "path"
SAVE = "save"
THEME = "theme"
FUZZINESS = "fuzziness"
ACCELERATE = "accelerate"

THEMES = [
    "暗黑琥珀色（dark amber）", "暗黑蓝色（dark blue）",
    "暗黑蓝绿色（dark cyan）", "暗黑绿色（dark lightgreen）",
    "暗黑粉色（dark pink）", "暗黑紫色（dark purple）",
    "暗黑红色（dark red）", "暗黑青色（dark teal）",
    "暗黑黄色（dark yellow）"
]
DEFAULT_THEME = THEMES[1]
DIC_THEMES = dict(zip(THEMES, list_themes()))
