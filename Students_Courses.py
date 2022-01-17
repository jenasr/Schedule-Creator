from ReadAudit_TK import all_courses
from ReadAudit_GE import ge_courses
from JSON_Handling import data, plan_data
from Stud_Cour_Class import StudentCourse
import json
#Creates our list of classes taken from the information we pulled from the audit
#Uses a class for each Class taken to store the information
def createTakenLegend(mycourses):
    for course in all_courses:
        course_term = course[0:4]
        if len(course) == 17:
            course_name = course[4:12]
            course_units = float(course[12:15])
            course_grade = course[15:]
        else:
            course_name = course[4:13]
            course_units = float(course[13:16])
            course_grade = course[16:]
        this_course = StudentCourse(course_name, course_term, course_units, course_grade)
        mycourses.append(this_course)
    return mycourses
#Removes any characters coming after a letter grade which are not -,+,C[R],I[P]
def removeChar(my_courses):
    for course in my_courses:
        if not(course.grade[-1] == '+' or course.grade[-1] == '-' or (course.grade[-2] == 'C' and course.grade[-1] == 'R') or (course.grade[-2] == 'I' and course.grade[-1] == 'P')):
            course.grade = course.grade.replace(course.grade[-1], '')
    return my_courses
#Using JSON and the courses taken I have add to each course what requirement the meet
#GE Courses are generalized for now
def add_Requirements(legend):
    legend_no_ge = legend
    i = 0
    for completed_course in legend:
        for course in data["courses"]:
            if completed_course.name == course["id"]:
                completed_course.req = course["requirement_type"]
            elif "CPSC-223" in completed_course.name:
                completed_course.req = "Lower Division"
        #print("{0}: {1}, {2}".format(completed_course.name, completed_course.req, completed_course.grade))
    return legend;
#We want to remove GE courses from our legend because we are going to handle them in another manner
def remove_GE(legend):
    for course in list(legend):
        if  course.req == "General Education":
            legend.remove(course)
    return legend
#From our JSON, delete any completed CS Upper or Lower Div taken
def deleteCSTaken(legend):
    for course in legend:
        for i in range(len(plan_data['courses'])):
            if plan_data['courses'][i]['id'] in course.name:
                #print(plan_data['courses'][i]['id'] + " = " + course.name)
                plan_data['courses'].pop(i)
                break
    #print(plan_data)
#From our JSON, delete any GE courses taken
def deleteGETaken(legend):
    for course in ge_courses:
        for i in range(len(plan_data['courses'])):
            if course in plan_data['courses'][i]['course_name']:
                #print(plan_data['courses'][i]['course_name'] + " = " + course)
                plan_data['courses'].pop(i)
                break
#From our JSON, delete any Science and Math Electives Taken
def deleteSMTaken(legend):
    i = 1
    sci_math = []

    for course in list(legend):
        if course.req != "Science and Mathematics Electives":
            legend.remove(course)
        '''if course.name == "GEOL-101":
            legend.remove(course)'''
        #print("{0} {1}".format(course.name, course.units))
    for j in range(len(legend)):
        '''if legend[j].name == "BIOL-101L":
            legend[j].units = 0.0
            legend[j].grade = "IP"'''
        if legend[j].grade == "IP" and legend[j].units == 0.0:
            for c in data["courses"]:
                if legend[j].name == c['id']:
                    legend[j].units = c['units']


    copy_legend = legend

    for course in list(legend):
            if course.units != 4.0:
                for others in list(legend):
                    if ((course.name in others.name and others.name[-1] == "L") or (course.name[:8] in others.name and course.name[-1] == "L")) and course.name != others.name:
                        course_name = "SME-{0}".format(i)
                        course_units = course.units + others.units
                        my_course = StudentCourse(course_name, "NULL", course_units, "NULL")
                        sci_math.append(my_course)
                        i += 1
                        legend.remove(course)
                        legend.remove(others)
                        break
            else:
                course_name = "SME-{0}".format(i)
                course_units = 4.0
                my_course = StudentCourse(course_name, "NULL", course_units, "NULL")
                sci_math.append(my_course)
                i += 1
                legend.remove(course)

    for course in legend:
        if course.name[-1] == "L":
            course_name = "{0}".format(course.name[:8])
            course_units = 4.0 - course.units
            my_course = StudentCourse(course_name, "NULL", course_units, "NULL")
            sci_math.append(my_course)
        else:
            course_name = "{0}L".format(course.name)
            course_units = 4.0 - course.units
            my_course = StudentCourse(course_name, "NULL", course_units, "NULL")
            sci_math.append(my_course)
    #for course in sci_math:
        #print("{0} {1}".format(course.name, course.units))

    for course in list(sci_math):
        for j in range(len(plan_data['courses'])):
            if  plan_data["courses"][j]['id'] == course.name and course.units == 4.0:
                plan_data['courses'].pop(j)
                sci_math.remove(course)
                break
    for course in sci_math:
        for j in range(len(plan_data['courses'])):
            if plan_data['courses'][j]['id'] == "SME-{0}".format(i):
                plan_data['courses'][j]['id'] = course.name
                plan_data['courses'][j]['units'] = course.units
                i += 1
#Delete the Computer Science Electives taken
def deleteCETaken(legend):
    for course in list(legend):
        if course.req != "CPSC Elective":
            legend.remove(course)
    cse_legend = []
    for i in range(len(legend)):
        cse = "CSE-{0}".format(i+1)
        #print(cse)
        cse_legend.append(cse)
    for cse_course in cse_legend:
        for i in range(len(plan_data['courses'])):
            if cse_course == plan_data['courses'][i]['id']:
                plan_data['courses'].pop(i)
                break
        #for i in range(len(plan_data['courses'])):

    #printLegend(legend)
#Delete the Z elective because it is a special case that cannot be handled like other GE's
def deleteZ():
    i = 0
    for i in range(len(plan_data['courses'])):
        if plan_data['courses'][i]['id'] == "GE-Z":
            plan_data['courses'].pop(i)
            break


#Find the the max number of rows of classes left.
def findMaxRowNumber(my_row):
    for i in range(len(plan_data['courses'])):
        if my_row < plan_data['courses'][i]['row']:
            my_row = plan_data['courses'][i]['row']
    return my_row
#In the course plan JSON each class is assigned a row it belongs. I want to pull one course from each row
# A course roadmap is written in rows and columns
def makeSchedule(plan_data):
    new_data = []
    j = 1
    max_row = findMaxRowNumber(plan_data['courses'][0]['row'])
    while (j <= max_row):
        row_seen = False
        for i in range(len(plan_data['courses'])):
            if j == plan_data['courses'][i]['row']:
                new_data.append(plan_data['courses'][i])
                j += 1
                break
    return new_data
#used to give an output to the terminal.
def printCoursesLeft(plan):
    for course in plan:
        print(course)
#Calls functions above to form the schedule
def main():
    mycourses = []
    legend = createTakenLegend(mycourses)
    legend = removeChar(legend)
    legend = add_Requirements(legend)
    legend = remove_GE(legend)
    deleteCSTaken(list(legend))
    deleteGETaken(list(legend))
    deleteSMTaken(list(legend))
    deleteCETaken(list(legend))
    deleteZ();
    new_plan = makeSchedule(plan_data)
    schedule = json.dumps(new_plan, indent=2)
    #After a lot of editing, create a json file and store our schedule in it
    with open("schedule.json", "w") as f:
        f.write(schedule)
    printCoursesLeft(new_plan)


if __name__ == "__main__":
  main()
