Joseph Nasr
This is designed to explain to you the purpose of each file in this submission is for.
To run the program, ensure everything is in the same directory and then enter 'python3 Students_Courses.py'  in the command line
File Purposes:

PDF_Read_Write_audit.py uses a pdf python library to extract information from the pdf and store it into a audit2.txt

Using this audit2.txt file:
ReadAudit_TK pulls all courses taken by the student from the audit. These also include courses that are in progress. The program assumes the student will pass the in progress courses.
ReadAudit_GE pulls the GE courses which the student has received credit for and is currently taking. GE's are treated differently from the other courses, due to how they are written in the audit.

Stud_Cour_Class creates a class for us to some up information on each course a student needs to take.

CPSC_catalog.json is a json I created by hand as a list of CPSC classes that a CS student can take with regards to their major.
course_plan.json is a json I created to represent the Roadmap that students are given for their major.
JSON Handling.py uses these json's to create json objects for future use.

Pulling this information together:
Students_Courses.py creates a schedule stored in schedule.json - see this file for more in-depth comments

For the purposes of privacy, I have removed audits.