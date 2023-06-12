from tkinter import *
from tkinter import filedialog
from pypdf import PdfMerger
import os

def select_files():
    global merger
    files = filedialog.askopenfilenames()
    merger = PdfMerger()
    for file in files:
        try:
            if file.split('.')[1]=='pdf':
                merger.append(file)
        except:
            ...
def merging():
    path = filedialog.asksaveasfilename(filetypes=(('PDF File', '*.pdf'), ('All files', '*.*')))
    path_split = path.split('/')
    filename = path_split[-1]
    path_split.pop(-1)
    new_path = '/'.join(path_split)
    os.chdir(new_path)
    merger.write(f'{filename}.pdf')
    merger.close()

root = Tk()
root.title('PDF Merger')
root.geometry('300x200')
root.resizable(height=False, width=False)

browse_files_label = Label(text='Select the files in the merge order')
browse_files_label.place(x=10, y=5)
browse_files_button = Button(text = 'Add files for merge', command=select_files)
browse_files_button.place(y=38, relx=0.5, anchor=CENTER)
merging_label = Label(text='If you already choose files for merging - "merge it!"')
merging_label.place(x = 10, y = 50)
merging_button = Button(text='Merge', command=merging)
merging_button.place(relx=0.5, y= 100, anchor=CENTER, height=50, width=70)

root.mainloop()