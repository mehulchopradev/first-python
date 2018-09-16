from contact import Contact
from abc import abstractmethod, ABC

class Person(ABC):

    def __init__(self, name, gender, contact=None):
        self.name = name
        self.gender = gender

        if contact:
            if isinstance(contact, Contact):
                self.contact = contact # has-a contact (composition)
            else:
                self.contact = None
        else:
            self.contact = contact

    def getPrettyDetails(self):
        str1 = 'Name: {0}\nGender: {1}'.format(self.name, self.gender)
        str2 = ''
        if self.contact:
            str2 += '\nEmail: {0}\nMobile: {1}'.format(self.contact.email, self.contact.mobile)

        return str1 + str2

    def getEmail(self):
        if self.contact and self.contact.email:
            return self.contact.email
        return 'NA'

    def getMobile(self):
        if self.contact and self.contact.mobile:
            return self.contact.mobile
        return 'NA'

    @abstractmethod
    def giveAttendance(self):
        pass
