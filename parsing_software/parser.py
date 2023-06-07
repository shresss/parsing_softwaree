import PyPDF2
import tabula
""" import correct parsing software already integrated in python"""

pdf_file = open('PUT_FILENAME_HERE.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
""" load file with PyPDF2"""

text = ''
for page in range(pdf_reader.numPages):
    page_obj = pdf_reader.getPage(page)
    text += page_obj.extractText()
    """extracts text"""

tables = tabula.read_pdf('path/to/pdf_file.pdf', pages='all')
"""parses tabular data with tabula"""

for table in tables:
    print(table)
"""accesses parsed data , will print each as a Pandas data frame"""