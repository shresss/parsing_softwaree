from pypdf import PdfReader
import tabula
""" import correct parsing software already integrated in python"""

reader = PdfReader("example.pdf")
number_of_pages = len(reader.pages)
""" load file with PyPDF2"""

text = ''
for page in range(number_of_pages):
    page_obj = reader.pages[page]
    text += page_obj.extract_text()
    """extracts text"""

tables = tabula.read_pdf('path/to/pdf_file.pdf', pages='all')
"""parses tabular data with tabula"""
column_widths = [max(len(item) for item in column) for column in zip(*tables)]
formatted_table = ''
for row in tables:
    formatted_row = ' | '.join(f'{item:^{width}}' for item, width in zip(row, column_widths))
    formatted_table += f'{formatted_row}\n'
for table in tables:
    print(table)
"""accesses parsed data , will print each as a Pandas data frame
Done By Shreyas V"""