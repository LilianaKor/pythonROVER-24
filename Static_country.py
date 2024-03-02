class Professional:
    country = 'USA'

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def greetings(self):
        return f'{self.fname} {self.lname} says greetings'

    def learn(self):
        return 'I\'m learning'

class Doctor(Professional):
    def __init__(self, fname, lname, degree, job_title, implanting, salary):
        super().__init__(fname, lname)
        self.degree = degree
        self._job_title = job_title
        self.surgery_device = implanting
        self.__salary = salary
        self.country = 'USA'


    def implanting(self):
        return f'I\'m doing surgery with {self.surgery_device}'

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def learn(self):
        return f'I\'m learning surgery'


class Junior(Doctor):
    def __init__(self, fname, lname, degree, job_title, implanting, salary, age):
        super().__init__(fname, lname, degree, job_title, implanting, salary)
        self.age = age

class chiefortho(Professional):
    def __init__(self, fname, lname, domain, job_title, implanting):
        super().__init__(fname, lname,)
        self.domain = domain
        self.job_title = job_title
        self.implanting_device = implanting

    def implanting(self):
        return f'I\'m consult surgery with {self.implanting_device}'

class NURS(Doctor, chiefortho):
    def __init__(self, fname, lname, degree, job_title, implanting, salary):
        super().__init__(fname, lname, degree, job_title, implanting, salary)

    def build_appro(self):
        return "I'm build replace approach"

    def learn(self):
        return f'I\'m learning consult'

Doc = Professional('Alex', 'Mez')
print(Doc.fname)
print(Doc.lname)
Doc.fname = 'Alexey'
print(Doc.__dict__)
print(Doc.greetings())
print(Doc.country)
print(Doc.fname)
print(Doc.__dict__)
print(Doc.learn())

ortho = Doctor('Dany', 'Royan', 'PhD', 'Ortho Assist', 'stryker', 10000)
print(ortho.fname)
print(ortho.lname)
print(ortho.degree)
print(ortho.job_title)
print(ortho.implanting())
print(ortho.country)
print(ortho.get_salary())
print(ortho.set__salary(20000))
print(ortho.get_salary())
print(ortho._Doctor__salary)   #acsess to privat method
print(ortho._job_title)        #not recomend
print(ortho.learn())

chiefortho1 = chiefortho('luis', 'Pennot', 'joint replacement','chief', 'stryker_spine')
print(chiefortho1.fname)
print(chiefortho1.lname)
print(chiefortho1.domain)
print(chiefortho1.job_title)
print(chiefortho1.implanting())
print(chiefortho1.country)
print(ortho.learn())

nurs = NURS('Sem', 'Mars', 'MD', 'assist','stryker',)

print(nurs.domain())

