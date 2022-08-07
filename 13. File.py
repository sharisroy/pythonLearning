# file = open("File/myfile.txt", "r")
#
# print(file.readable())
# text = file.read()
# print(text)
# print("Line: ", len(text))
# file.close()


# Working with PFD file
import PyPDF2

pdfFileObj = open('File/p.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
pdfFileObj.close()