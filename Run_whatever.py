class Professional:
    country = 'USA'

    def __init__(self, fname, lname, implanting):
        self.fname = fname
        self.lname = lname
        self.implanting = implanting

    def greetings(self):
        return f'{self.fname} {self.lname} says greetings'

    def learn(self):
        return 'I\'m learning'

    # def implanting(self):
    #     return f'{self.fname} {self.lname} doing surgery with {self.implanting}'
    #
    # def get_sur(self):
    #     return(self.implanting)

# p = Professional('Dany', 'Royan', 'implanting')
# print(p.get_sur())

class Doctor(Professional):
    def __init__(self, fname, lname, degree, job_title, salary, device_type):
        super().__init__(fname, lname, device_type)
        self.degree = degree
        self.job_title = job_title
        self.salary = salary

    def improve(self, value):
        return f"Doctor named {self.lname} improved life style with {value} {self.implanting}"


ortho = Doctor('Dany', 'Royan', 'PhD', 'Ortho Assist', 10000, 'stryker')
print(ortho.fname)
print(ortho.lname)
print(ortho.degree)
print(ortho.job_title)
print(ortho.salary)
print(ortho.implanting)
print(ortho.learn())
print(ortho.improve('surgery device'))

class chiefortho(Professional):
    def __init__(self, fname, lname, domain, job_title, device_type):
        super().__init__(fname, lname, device_type)
        self.domain = domain
        self.job_title = job_title
        self.implanting_device = device_type

    def perform(self, options):
        return f"Doctor named {self.lname} performs surgery with {options} {self.domain} of {self.implanting}"

chiefortho1 = chiefortho('luis', 'Pennot', 'joint replacement', 'chief', 'stryker_spine')
print(chiefortho1.lname)
print(chiefortho1.domain)
print(chiefortho1.implanting)
print(chiefortho1.perform('unique'))

#print(chiefortho1.country)
#print(chiefortho1.learn())
