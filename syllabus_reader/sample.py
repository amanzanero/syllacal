# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('example.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(2)

# extracting text from page
page_str = pageObj.extractText()
page_str = page_str.split(" ")
for string in page_str:
    string = string.strip('\n')
print(repr(page_str))
print(type(pageObj.extractText()))

# closing the pdf file object
pdfFileObj.close()