# from datetime import date
# test

class Person:
    def __init__(self, name, dob, gender, address):
        self.name = name
        self.dob = dob  # date(1980, 5, 26)
        self.gender = gender
        self.address = address

    def firstname(name):
        return(name.split()[0])

    def surname(name):
        return(name.split()[1])
    '''
    def age(dob):
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    '''
    def __str__(self):
        return "\nName: {}\nAddress: {}\ntelephone: {}\nEmail: {}\nMail: {}\nNumber: {}".\
                    format(self.get_name(), self.get_address(),
                           self.get_telephone(), self.get_email())


class Student(Person):
    def __init__(self, days, times, courses, languages, exams, skills):
        self.days = days
        self.times = times
        self.courses = courses
        self.languages = languages
        self.exams = exams
        self.skills = skills


class Teacher():
    pass


if __name__ == '__main__':
    person = Person(name="Jane Doe", dob=(1992, 3, 12), gender=0, address='Street')

    print(person.firstname())
    print(person.surname)
    # print(person.age())
