# Instance variable vs Class variable
class Employee:
    # Class variable
    companyName = "Apple"

    def __init__(self, name):
        # Instance variable
        self.name = name

    def showDetails(self):
        print(
            f"The name of the Employee is {self.name} and he works in <<{self.companyName}>>.")


emp1 = Employee("Sachin")
emp1.showDetails()

emp2 = Employee("Rathore")
# Instance variable has more priority than Class variable.
emp2.companyName = "Tesla"
emp2.showDetails()
