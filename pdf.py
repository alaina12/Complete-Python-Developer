import PyPDF2

#to open the file
with open("dummy.pdf",'rb') as file:
	#pdfFileReader is a method under the module to read the file
	reader = PyPDF2.PdfFileReader(file)
	print(reader.numPages) #operations come under the module
	print(reader.getPage(0))
	# tp roatate the page we need the page 
	page = reader.getPage(0)
	print(page.rotateCounterClockwise(90))
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open("tilt.pdf",'wb') as new_file:
		writer.write(new_file)
