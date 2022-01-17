#This python file grabs text from a pdf and stores it into a text PdfFileReader
from PyPDF2 import PdfFileReader, PdfFileWriter
text = ""
with open('audit2.txt', 'r') as f:
    for line in f:
        if "(Excludes Remedial/Non-baccalaureate level courses)"  in line:
            text += line
            for line in f:
                text += line

import re
#It then uses the regular expression library to find the courses which a student has taken or is taking
#And makes a list of each one.
#It then removes any duplicates from the list since the audit does mention each one twice
courses_taken_fall = re.findall('FA[0-9][0-9][A-Z]{4}-[0-9]{3}[A-Z]{1}[0-9].[0-9][ABCDF]{1}.|FA[0-9][0-9][A-Z]{4}-[0-9]{3}[0-9].[0-9][ABCDF]{1}.', text)
courses_taken_spring = re.findall('SP[0-9][0-9][A-Z]{4}-[0-9]{3}[A-Z]{1}[0-9].[0-9][ABCDF]{1}.|SP[0-9][0-9][A-Z]{4}-[0-9]{3}[0-9].[0-9][ABCDF]{1}.', text)
courses_progress_fall = re.findall('FA[0-9][0-9][A-Z]{4}-[0-9]{3}[A-Z]{1}[0-9].[0-9]IP|FA[0-9][0-9][A-Z]{4}-[0-9]{3}[0-9].[0-9]IP', text)
courses_progress_spring = re.findall('SP[0-9][0-9][A-Z]{4}-[0-9]{3}[A-Z]{1}[0-9].[0-9]IP|SP[0-9][0-9][A-Z]{4}-[0-9]{3}[0-9].[0-9]IP', text)


all_courses = courses_taken_fall + courses_taken_spring + courses_progress_fall + courses_progress_spring
#print(all_courses)
