#This project is for merging two PDF together
import PyPDF2
import sys 

#sys to get the arguements
inputs = sys.argv[1:]

def pdf_merger(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write("combined.pdf")

pdf_merger(inputs)