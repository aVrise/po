import PyPDF2
import os
import re


def main():
    # find all the pdf files in current directory.
    # mypath = os.getcwd()
    # pattern = r"\.pdf$"
    # file_names_lst = [f for f in os.listdir(mypath) if re.search(pattern, f, re.IGNORECASE) 
    # and not re.search(r'Merged.pdf',f)]

    # merge the file.
    pdfFM = PyPDF2.PdfFileMerger()
    for kkk in range(1,327):
        pdfFM.append(open(str(kkk)+".pdf",'rb'))
    # pdfFM = PyPDF2.PdfFileMerger()
    # for file in opened_file:
    #     pdfFM.append(file)

    # output the file.
    with open("./Merged.pdf", 'wb') as write_out_file:
        pdfFM.write(write_out_file)

    # close all the input files.
    for file in opened_file:
        file.close()

if __name__ == '__main__':
    main()
