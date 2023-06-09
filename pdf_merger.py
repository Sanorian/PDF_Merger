# import of required modules
from pypdf import PdfMerger
import os
# get path to the directory with .py script
current_dir = os.getcwd()
# create an array for merging
merger = PdfMerger()
# changing directory to the directory where the PDF files are located
os.chdir(f'{current_dir}\\pdfs')
# get list of file names
files = os.listdir()
# check files for pdf ending
for file in files:
    try:
        if file.split('.')[1]=='pdf':
            merger.append(file)
    except:...
# return to the main directory
os.chdir(f'{current_dir}')
# merging to one file
merger.write("result.pdf")
# That's all!
merger.close()