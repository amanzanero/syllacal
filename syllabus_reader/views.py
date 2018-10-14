from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect
from .forms import UploadFileForm, handle_uploaded_file
import PyPDF2


# Create your views here.
def index(request):
    return render(request, 'syllabus_reader/index.html')


def index_example(request):
    # creating a pdf file object
    pdfFileObj = open('/Users/amanzanero/Dropbox/Python_Projects/django_apps/'
                      'syllacal/syllabus_reader/example.pdf', 'rb')

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

    for new_string in page_str:
        print(new_string)

    # closing the pdf file object
    pdfFileObj.close()
    return render(request, 'syllabus_reader/index.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f_name = handle_uploaded_file(request.FILES['file'])
            pdf_processor(f_name)
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form})


def pdf_processor(pdf):
    pdf_reader = PyPDF2.PdfFileReader(pdf)
    page_obj = pdf_reader.getPage(0)
    info = page_obj.extractText()
    print(info)
