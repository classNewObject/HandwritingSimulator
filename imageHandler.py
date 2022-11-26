"""处理图片"""
from numpy import asarray
from PIL import Image, ImageFilter
from cv2 import medianBlur, cvtColor, COLOR_RGB2BGR, COLOR_BGR2RGB


def gaussian_blur(image: Image.Image, radius: float) -> Image.Image:
    """图片高斯模糊"""
    # 应用高斯模糊滤波器
    gauss_image = image.filter(ImageFilter.GaussianBlur(radius))
    return gauss_image


def beautify(image_pil: Image) -> Image.Image:
    """美化图片"""
    # pil转cv2格式
    img_bgr = cvtColor(asarray(image_pil), COLOR_RGB2BGR)

    # 抗锯齿
    img_bgr = medianBlur(img_bgr, 3)

    # cv2转pil格式
    image_pil = Image.fromarray(cvtColor(img_bgr, COLOR_BGR2RGB))

    # 添加滤镜
    image_pil = image_pil.filter(ImageFilter.SHARPEN)  # 锐化滤镜
    image_pil = image_pil.filter(ImageFilter.SMOOTH)  # 平滑滤镜

    return image_pil
