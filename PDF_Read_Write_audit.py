from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
#Create pdf file reader object
pdf = PdfFileReader("audit_2021-2.pdf")

#TWO Steps to extract text
#Step 1: Grab the page(s)
page_1_object = pdf.getPage(7)
print(page_1_object)
#Step 2: Extract Text
page_1_text = page_1_object.extractText()
print(page_1_text)

#combine the text from all the pages and save as a txt file_path
with Path("audit2.txt").open(mode='w') as of:
    text = ''
    for page in pdf.pages:
        text += page.extractText() + "\n\n"
    of.write(text)
