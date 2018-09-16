'''
getPrettyDetails
	- name
	- roll
	- gender
	- marks
returns
Name : name
Roll : roll
Gender : gender
Marks : marks
'''
def getPrettyDetails(name, roll, gender, marks):
	return 'Name : ' + name + '\nRoll : ' + str(roll) + '\nGender : ' + gender \
		+ '\nMarks : ' + str(marks)



'''
getGrade
	- marks
return grade (grade chart)
'''

def getGrade(marks):
	if marks > 100 or marks < 0:
		return 'I'
	elif marks >= 70:
		return 'A'
	elif marks >= 60:
		return 'B'
	elif marks >= 40:
		return 'C'
	else:
		return 'F'
