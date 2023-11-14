# Class Method

class Employee:
    company = "Apple"

    def show(self):
        print(f"The company name is <<{self.company}>>")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.show()
print(Employee.company)

e1.changeCompany("Tesla")
e1.show()
print(Employee.company)
