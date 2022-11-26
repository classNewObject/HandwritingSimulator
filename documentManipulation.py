"""读取PDF和docx文档中所有的文字内容"""
import pdfplumber
from docx import Document


def extract_pdf_content(pdf_path: str) -> str:
    """提取PDF文本内容"""
    content = ''
    with pdfplumber.open(pdf_path) as pdf_file:
        # 逐页解析PDF文档
        for p in range(len(pdf_file.pages)):
            page_text = pdf_file.pages[p]
            page_content = page_text.extract_text()
            if page_content:
                content += page_content + "\n"

    return content


def extract_docx_content(docx_path: str) -> str:
    """提取docx文本内容"""
    content = ''
    doc = Document(docx_path)
    for p in doc.paragraphs:
        content += p.text + "\n"

    return content
