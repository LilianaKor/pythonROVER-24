# //  HW_5_Liliana_Pyclasses.swift
# //    Created by Liliana Koretska on 2/22/24.

class Professional:
    country = 'USA'

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

#     @property
#     def email(self):
#         return f'{self.fname}.{self.lname}@gmail.com'

    def greetings(self):
         return f'{self.fname} {self.lname} says greetings'

#     def research(self):
#         return 'I\'m researching'
#
#     @classmethod
#     def change_country(cls, new_country):
#         cls.country = new_country
#         print(cls.country)
#
#     @staticmethod
#     def is_adult(age):
#         return age > 21
class Doctor(Professional):
     def __init__(self, fname, lname, degree, job_title, implanting):
        super().__init__(fname, lname,)
        self.degree = degree
        self.job_title = job_title
        self.implanting_device = implanting
#        self.__salary = salary

     def implanting(self):
        return f'I\'m doing surgery with {self.implanting_device}'

#    def get_salary(self):
#        return self.__salary
#
#     def set_salary(self, new_salary):
#         self.__salary = new_salary
#
#     def learn(self):
#         return f'I\'m learning coding'
#
class chiefortho(Professional):
    def __init__(self, fname, lname, domain, job_title, implanting):
        super().__init__(fname, lname,)
        self.domain = domain
        self.job_title = job_title
        self.implanting_device = implanting
    def implanting(self):
        return f'I\'m consult surgery with {self.implanting_device}'

Doctor = Professional('Alex', 'Mez')
print(Doctor.fname)
print(Doctor.lname)
print(Doctor.__dict__)
print(Doctor.greetings())
print(Doctor.country)
#
# Designer = Professional('Lera', 'Star')
# print(Designer.fname)
# print(Designer.lname)
# print(Designer.__dict__)
# print(Designer.greetings())

ortho = Doctor('Dany','Royan','PhD','Ortho Assist','stryker')
print(ortho.fname)
print(ortho.lname)
print(ortho.degree)
print(ortho.job_title)
print(ortho.implanting())
print(ortho.country)

chiefortho1 = chiefortho('luis', 'Pennot', 'joint replacement','chief', 'stryker_spine')
print(chiefortho1.fname)
print(chiefortho1.lname)
print(chiefortho1.domain)
print(chiefortho1.job_title)
print(chiefortho1.implanting())
print(chiefortho1.country)





# //skills_area.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
# //    - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
# //    нужно использовать методы get и set
# //skills_area.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий
