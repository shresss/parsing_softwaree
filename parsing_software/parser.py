import pypdf
import tabula
""" import correct parsing software already integrated in python"""

pdf_file = open('Resume.pdf', 'rb')
pdf_reader = pypdf.PdfFileReader(pdf_file)
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
"""accesses parsed data , will print each as a Pandas data frame
Done By Shreyas V"""