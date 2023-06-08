from pypdf import PdfMerger
import os
current_dir = os.getcwd()
pdf_list = []
os.chdir(f'{current_dir}\\pdfs')
files = os.listdir()
for file in files:
    if file.split('.')[1]=='pdf':
        pdf_list.append(file)
merger = PdfMerger()
for pdf in pdf_list:
    merger.append(pdf)
split_dir = current_dir.split('\\')
os.chdir(f'{current_dir}')
merger.write("result.pdf")
merger.close()