from person import Person

class Professor(Person):

    def __init__(self, name, gender, subjects, contact=None):
        super().__init__(name, gender, contact) # calls the Person class constructor
        '''
            Person.__init__(self, name, gender)
        '''
        self.subjects = subjects

    # forced to override the @abstractmethod
    def giveAttendance(self):
        print('Attendance given by logging into the web portal')
