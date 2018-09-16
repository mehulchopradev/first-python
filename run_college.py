from professor import Professor
from student import Student
from contact import Contact
from person import Person

# p = Person(name='mehul', gender='m') # cannot do that!

p1 = Professor(name='mehul chopra', gender='m', subjects=['Maths', 'Programming'],\
    contact=Contact(email='mehul@gmail.com', mobile='0987907907'))

'''
    1) RAM 90345
    2) Professor.__init__(90345, name, gender, subjects)
'''


s1 = Student(name='jane', gender='f', roll=10, marks=90)

s1.giveAttendance()
p1.giveAttendance()

'''print(p1.getEmail())
print(p1.getMobile())

print(s1.getEmail())'''

# print(s1.getPrettyDetails())
# print(p1.getPrettyDetails())
# print(p1.name)

'''Professor and Student objects belong to a common category of people in the college.
   They share common properties (name, gender)
'''
