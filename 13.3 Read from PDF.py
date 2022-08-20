# Working with PFD file
import PyPDF2

pdfFileObj = open('File/p.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
print(len(pdfReader.pages))
# pageObj = pdfReader.getPage(0)
pageObj = pdfReader.pages[0]
print(pageObj.extractText())
pdfFileObj.close()