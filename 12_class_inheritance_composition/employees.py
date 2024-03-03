import itertools
from abc import ABC, abstractmethod
from hr import SalaryPolicy, CommissionPolicy, HourlyPolicy
from productivity import ManagerRole, SecretaryRole, SalesRole, FactoryRole

## Old Employee Class

# class Employee:
#     ID_OBJ = itertools.count(1)

#     def __init__(self, name, salary):
#         self.id = next(Employee.ID_OBJ)
#         self.name = name
#         self.salary = salary

#     @classmethod
#     def create_employee(cls, name, salary):
#         # name = input("Enter the name of the employee: ")
#         # salary = int(input("Enter the salary of the employee: "))
#         return cls(name, salary)

#     def calculate_payroll(self):
#         return f"R${self.salary},00"

#     def __repr__(self):
#         return f"<Employee({self.id}, {self.name}, {self.salary})>"


## Structure with error in inheritance implementation
# class Employee(ABC):
#     """
#     properties: id, name

#     Abstract base classes and abstract methods: ABC only stops the creation of objects
#     if the abstract method is defined and vice-versa.

#     Employee is an ABC and the other classes are concrete classes: it makes no sense to
#     be used alone. It must always be derived.
#     """

#     ID_OBJ = itertools.count(1)

#     def __init__(self, name):
#         self.id = next(Employee.ID_OBJ)
#         self.name = name

#     @abstractmethod
#     def calculate_payroll(self):
#         pass


# class SalaryEmployee(Employee):
#     """
#     properties: id, name, weekly_salary
#     """

#     def __init__(self, name, weekly_salary):
#         super().__init__(name)
#         self.weekly_salary = weekly_salary

#     def calculate_payroll(self):
#         return self.weekly_salary

#     def __repr__(self):
#         return f"<SalaryEmployee({self.id}, {self.name}, {self.weekly_salary})>"


# class HourlyEmployee(Employee):
#     """
#     properties: id, name, hours_worked, hourly_rate
#     """

#     def __init__(self, name, hours_worked, hourly_rate):
#         super().__init__(name)
#         self.hours_worked = hours_worked
#         self.hourly_rate = hourly_rate

#     def calculate_payroll(self):
#         return self.hours_worked * self.hourly_rate

#     def __repr__(self):
#         return f"<HourlyEmployee({self.id}, {self.name}, {self.hours_worked}, {self.hourly_rate})>"


# class CommissionEmployee(SalaryEmployee):
#     """
#     properties: id, name, weekly_salary, comission
#     """

#     def __init__(self, name, weekly_salary, commission):
#         super().__init__(name, weekly_salary)
#         self.commission = commission

#     def calculate_payroll(self):
#         fixed = super().calculate_payroll()
#         return fixed + self.commission
#         # same
#         # return self.weekly_salary + self.commission

#     def __repr__(self):
#         return f"<CommissionEmployee({self.id}, {self.name}, {self.weekly_salary}, {self.commission})>"


# class Manager(SalaryEmployee):
#     def work(self, hours):
#         print(f"{self.name} screams and yells for {hours} hours.")


# class Secretary(SalaryEmployee):
#     """
#     Derives from Salary Employee
#     properties: id, name, weekly_salary
#     """

#     def work(self, hours):
#         print(f"{self.name} expends {hours} hours doing office paperwork.")


# class SalesPerson(CommissionEmployee):
#     def work(self, hours):
#         print(f"{self.name} expends {hours} hours on the phone.")


# class FactoryWorker(HourlyEmployee):
#     def work(self, hours):
#         print(f"{self.name} manufactures gadgets for {hours} hours.")


# class TemporarySecretary(Secretary, HourlyEmployee):
#     # def __init__(self, name, hours_worked, hourly_rate):
#     #     super().__init__(name, hours_worked, hourly_rate)

#     def __init__(self, name, hours_worked, hourly_rate):
#         # passes the obj directly to force the MRO to work
#         HourlyEmployee.__init__(self, name, hours_worked, hourly_rate)

#     def calculate_payroll(self):
#         # does the same thing to calculate the payroll
#         return HourlyEmployee.calculate_payroll(self)


## Solution for multiple inheritance error
# Separate calculate hours and payroll methods
# now it's not necessary to specify the type of employee, only the employee roles
class Employee(ABC):
    ID_OBJ = itertools.count(1)

    def __init__(self, name):
        self.id = next(Employee.ID_OBJ)
        self.name = name


class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, name, weekly_salary):
        super().__init__(name)
        SalaryPolicy.__init__(self, weekly_salary)


class Secretary(Employee, SecretaryRole, SalaryPolicy):
    def __init__(self, name, weekly_salary):
        super().__init__(name)
        SalaryPolicy.__init__(self, weekly_salary)


class SalesPerson(Employee, SalesRole, CommissionPolicy):
    def __init__(self, name, weekly_salary, commission):
        super().__init__(name)
        CommissionPolicy.__init__(self, weekly_salary, commission)


class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        HourlyPolicy.__init__(self, hours_worked, hourly_rate)


class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        HourlyPolicy.__init__(self, hours_worked, hourly_rate)
