from person import Person

# class gives the data type to an object
# n objects can be created from a class
# Person -> super class/ parent class
# Student -> sub class/child class
class Student(Person):

	'''def __init__(self):
		# print(self) # refers to the current object for which __init__ is called
	'''

	def __init__(self, name='NA', roll=0, gender='NA', marks=0, contact=None):
		super().__init__(name, gender, contact)

		# constructor of the class
		self.roll = roll
		self.marks = marks

	# method overriding
	def getPrettyDetails(self):
		str1 = super().getPrettyDetails()
		str2 = '\nRoll: {0}\nMarks: {1}'.format(self.roll, self.marks)

		return str1 + str2

	def get_name_roll(self):
		return (self.name, self.roll)

	def getGrade(self):
		marks = self.marks
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

	def giveAttendance(self):
		print('Attendance given by finger print recognition')

if __name__ == '__main__':
	s = Student(contact='mehul@gmail.com')
	s3 = Student('jill', 20, marks=67, contact=Contact(email='jill@gmail.com', mobile='90687908790')) # keyword arguments
	#print(s3.getEmail())
	# print(s3.getMobile())

	'''
	1) Python reserves a area in the ram (567345)
	2) Student() -> Student.__init__(567345)
	3) s = store the address returned by __init__ (567345)
	'''

	s1 = Student('mehul', 10, 'm', 90, Contact()) # positional arguments
	# print(s1.getEmail())
	# print(s1.getMobile())
	'''
		1) Python reserve an area in the ram for the object (689567)
		2) Student('mehul', 10, 'm', 90) -> Student.__init__(689567, 'mehul', 10, 'm', 90)
	'''
	'''s1.name = 'mehul'
	s1.roll = 10
	s1.gender = 'm'
	s1.marks = 90'''

	# Student()  -> reserve a memory in the ram for that student (6754)
	# s1 = Student() -> s1 variable will store the address of that object (6754)
	s2 = Student('jane', 11, 'f', 56)
	# print(s2.get_name_roll())
	'''s2.name = 'jane'
	s2.roll = 11
	s2.gender = 'f'
	s2.marks = 100'''

	'''print(s1.name)
	print(s2.name)
	print(s1.marks)
	print(s2.marks)'''

	print(s1.getPrettyDetails())
	'''
		s1.getPrettyDetails() -> Student.getPrettyDetails(s1)
	'''


	print(s2.getPrettyDetails())
	'''
		s2.getPrettyDetails() -> Student.getPrettyDetails(s2)
	'''

	print(s3.getPrettyDetails())

	# print(s1.getGrade())
	# Student.getGrade(s1)

	# print(s2.getGrade())
	# Student.getGrade(s2)

	# print(type(s1))
	# print(type(s2))
