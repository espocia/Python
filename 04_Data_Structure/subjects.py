"""
Tuple:
------

Time for Louis to go to school, and it's time for him to
choose subject, School doesn't want students to change
subjects after they are chosen, so they use Tuple.

Tuple is like a stricter brother of List. Once Tuple is
created, it cannot be edited.

Info:
-----
Tuple also starts from 0
"""

subjects: tuple[str,str,str]= ("Math", "Science", "Histroy",)

#---------------------------------------------------------
# Louis want to count his subjects
#---------------------------------------------------------

number_subjects = len(subjects)
print(f"number of subjects: {number_subjects}")

#---------------------------------------------------------
# Louis wants to signup for all subjects
#---------------------------------------------------------

for subject in subjects:
    print(f"Louis is signing up for {subject}")
    
    
#---------------------------------------------------------
# Louis wants to see his second subject
#---------------------------------------------------------

print(f"Louis second subject: {subjects[1]}")

#---------------------------------------------------------
# Louis wants to take 3 more subjects to get full credit
#---------------------------------------------------------

additional_subjects = ("English", "Python", "Physics")
total_subjects = additional_subjects + subjects
print(f"new subject: {additional_subjects}")
print(f"total subjects: {total_subjects}")

#-------------------------------------------------------------------
# Louis loves Python, and wants to see if it's there in his subjects
#-------------------------------------------------------------------

print(f"is Python in the list of subjects? : {'Python' in total_subjects}")
