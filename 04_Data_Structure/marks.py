"""
Dictionary
----------

Louise has given his exams and recieved marks. Let's check
out how he fare.

Dictionary makes it easy to have key-value pairs.

Info:
-----
Lookups are very fast
"""

from re import sub


marks = {
    "Maths": 80,
    "Science": 82,
    "History": 78,
    "English": 35,
    "Python": 98,
    "Physics": 63
}

print(f"Makrs: {marks}")

#------------------------------------------------
# Louis want to check out all the subjects (keys)
#------------------------------------------------

for key in marks.keys():
    print(key)

#------------------------------------------------
# Louis want to check out all the score (values)
#------------------------------------------------

for value in marks.values():
    print(value)

#-------------------------------------------------------------
# Louis wants to check out all the subjects and makes together
#-------------------------------------------------------------

for subjects in marks.keys():
    print(f"{subjects} : {marks[subjects]}")

#----------------------------------------------------------------------
# Louis wants to check if he passed all of the subject, Passing mark 50
#----------------------------------------------------------------------

for subjects, score in marks.items():
    passed: str = ""
    if score > 50:
        passed = "Passed"
    else:
        passed = "Failed"
        
    print(f"{subjects} : {score} : {passed}")

#------------------------------------------------------------------------
# Louis requests reevaluation or his Enlgish paper, there was a totaling
# mistake and the right marks are 70
#------------------------------------------------------------------------
marks['English'] = 70
print(marks)

#----------------------------------------
# Louis also took Geography and scored 78
#----------------------------------------

marks['Geography']  = 78
print(marks)
