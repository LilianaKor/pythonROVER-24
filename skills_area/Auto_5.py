class Person:

    country: 'USA'

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

     def hello(self):
         return f'{self.fname} {self.lname} says hello'

class Programmer (Person):
    def __init__(self, fname, lname, language, job_title, salary):
        super().__init__(fname, lname)
        self.language = language
        self.job_title = job_title
        self.__salary = salary

    def set_salary(self):
        self.__salary = new_salary


class Tester(Person):
    def __init__(self, fname = 'Leo', lname, language, job_title):
        super().__init__(fname, lname)
        self.framework = framework
        self.job_title = job_title

    def testing(self):
        return f' I\'m testing with {self.framework}'

    def set_salary
        return f' I\'m testing with {self.framework}'

    def learn(self):
        return f' I\'m testing coding


person_1 = Person('Alex', 'Kim')
print(person_1.lname)
print(person_1,fname)
print(person_1.__dict__)
print(person_1.hello())


person_2 = Person('Eva', 'Smith')
print(person_2.lname)
print(person_2,fname)
print(person_2.__dict__)
print(person_2.hello())




coder_1 = Programmer('Ed', 'Kor', 'Python', 'QA')
print(coder_1.lname)
print(coder_1.language)
print(coder_1.coding())
print(coder_1.country)


tester_1 = Tester()
print(tester_1.lname)
print(tester_1,fname)
print(tester_1.framework)
print(tester_1.testing())
print(tester_1.country)
print()


sdet_1 = SDET('Sam', 'Luis', 'Python', 'Engineer', 50000, 'pytest')
print(sdet_1.testing())