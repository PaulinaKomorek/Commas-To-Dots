from tkinter import filedialog
import os.path
from os import path


def main():
    filetypes = [("Text files", "*.txt"), ("All files", "*.*")]
    filename = filedialog.askopenfilename(filetypes)
    if not path.exists(filename):
        return
    newfilename = filedialog.asksaveasfilename(filetypes)
    file = open(filename, "r")
    if len(newfilename) <= 0:
        return
    newfile = open(newfilename, "w")
    content = file.read()
    newcontent = content.replace(",", ".")
    newfile.write(newcontent)
    file.close()
    newfile.close()


if __name__ == "__main__":
    main()
