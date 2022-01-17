#This python file grabs text from a pdf and stores it into a text PdfFileReader
from PyPDF2 import PdfFileReader, PdfFileWriter
text = ""
with open('audit2.txt', 'r') as f:
    for line in f:
            text += line

import re
#It then uses the regular expression library to find the courses which a student has taken or is taking
#And makes a list of each one.
#It then removes any duplicates from the list since the audit does mention each one twice
courses_taken = re.findall('[+][A-E][.][0-9]', text)
courses_extra = re.findall('[+][*][*].+[A-E][0-9][.]', text)
courses_progress = re.findall('IP[A-Za-z -]+[ABCDE][.][0-9]', text)
#|[A-Z]{4}-[0-5][.][A-F].[A-Za-z +]+[ABCDE][.][0-9]
ge_courses =  courses_taken + courses_progress

for i in range(len(ge_courses)):
    ge_courses[i] = ge_courses[i][-3:]
for i in range(len(courses_extra)):
    courses_extra[i] = "C.1 or C.2"
ge_courses += courses_extra
#print(ge_courses)
