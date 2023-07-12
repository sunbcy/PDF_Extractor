import PyPDF2
import re
from collections import Counter


# 1. 读取上传的pdf文档，将其中的字符以UTF-8的格式保存为txt
def extract_text_from_pdf(pdf_path, txt_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
            text += '\n\n=== Page Separator ===\n\n'  # 插入分隔符
        # text = re.sub(r'\s+', ' ', text)  # 去除多余的空白字符
            with open(txt_path, 'w', encoding='utf-8') as output_file:
                output_file.write(text)
        print("PDF文档中的文本已保存为txt文件。")


# 2. 统计文档的词频，判断主题并概括
def analyze_document(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()
        pages = re.split('\n\n=== Page Separator ===\n\n', text)  # 分割成页
        page_num = 1
        for page in pages:
            words = re.findall(r'\b\w+\b', page.lower())  # 提取单词并转换为小写
            word_counts = Counter(words)
            top_words = word_counts.most_common(10)  # 获取频率最高的前10个单词
            print(f"Page {page_num}:")
            print("频率最高的单词:")
            for word, count in top_words:
                print(f"{word}: {count}次")
            print('\n---\n')
            page_num += 1
        # 在此处添加根据词频判断主题的逻辑，以及相应的概括输出


# 调用函数进行处理
pdf_path = 'The_Economist_20230311.pdf'  # '渗透测试实践指南_sample.pdf'  # 'Company_of_One.pdf'  # 替换为实际的PDF文件路径
txt_path = 'The_Economist_20230311.txt'  # 替换为保存输出文本的路径

extract_text_from_pdf(pdf_path, txt_path)
analyze_document(txt_path)
