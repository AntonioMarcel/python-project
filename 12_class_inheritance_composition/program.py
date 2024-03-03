from hr import PayrollSystem
import disgruntled
from employees import Manager, Secretary, SalesPerson, FactoryWorker, TemporarySecretary
from productivity import ProductivitySystem


#### Class instantiations

### Original Employee Class

# emp1 = Employee.create_employee("claudinei", 123)
# emp2 = Employee.create_employee("marek", 4645)
# emp3 = Employee.create_employee("bruno", 9879)

# print(emp1)
# print(emp2)
# print(emp3)

# employees = (emp1, emp2, emp3)
# print(employees)
# ps = PayrollSystem()
# ps.calculate_payroll(employees)

### Employee Class being inherited

# emp1 = hr.SalaryEmployee("salaryMan", 65432)
# print(emp1.id)
# print(emp1.name)
# print(emp1.weekly_salary)
# print(emp1.calculate_payroll())
# print(emp1)

# emp2 = hr.HourlyEmployee("hourMan", 8, 75)
# print(emp2.id)
# print(emp2.name)
# print(emp2.hours_worked)
# print(emp2.hourly_rate)
# print(emp2.calculate_payroll())
# print(emp2)

# emp3 = hr.CommissionEmployee("comissionMan", 100, 20)
# print(emp3.id)
# print(emp3.name)
# print(emp3.weekly_salary)
# print(emp3.commission)
# print(emp3.calculate_payroll())
# print(emp3)

# employees = (emp1, emp2, emp3)
# print(employees)
# ps = hr.PayrollSystem()
# ps.calculate_payroll(employees)

### Employee without ABC and calculate_payroll method
# error: if there's no calculate_payroll in Employee

# employee = hr.Employee("Invalid")
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll([employee])

### Employee as an ABC class and with abstract method
# error: can't be instantiated: ABC class and abstract method

# employee = hr.Employee("Invalid")

### Right way to instantiate the new classes
# salary_employee = hr.SalaryEmployee("John Smith", 1500)
# hourly_employee = hr.HourlyEmployee("Jane Doe", 40, 15)
# commission_employee = hr.CommissionEmployee("Kevin Bacon", 1000, 250)

# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(
#     [salary_employee, hourly_employee, commission_employee]
# )


### Problem with ducktyping

# disgruntled_employee = disgruntled.DisgruntledEmployee(20000, "Anonymous")
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(
#     [
#         disgruntled_employee,
#     ]
# )

### New instantiation after moving Employee Classes to another file

# salary_employee = employees.SalaryEmployee("John Smith", 1500)
# hourly_employee = employees.HourlyEmployee("Jane Doe", 40, 15)
# commission_employee = employees.CommissionEmployee("Kevin Bacon", 1000, 250)

# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(
#     [salary_employee, hourly_employee, commission_employee]
# )

### Productivity system call and different types of employees
# manager = employees.Manager("Mary Poppins", 3000)
# secretary = employees.Secretary("John Smith", 1500)
# sales_guy = employees.SalesPerson("Kevin Bacon", 1000, 250)
# factory_worker = employees.FactoryWorker("Jane Doe", 40, 15)

# emps = [
#     manager,
#     secretary,
#     sales_guy,
#     factory_worker,
# ]

# productivity_system = productivity.ProductivitySystem()
# productivity_system.track(emps, 40)

# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(emps)

### Inheriting multiple classes
# error in Salary Employee
# temporary_secretary = employees.TemporarySecretary("Robin Williams", 40, 9)
# error in Hourly Employee
# temporary_secretary = employees.TemporarySecretary("Robin Williams", 40)

## If you invert TemporarySecretary class inheritance order
# still errors in both cases
# temporary_secretary = employees.TemporarySecretary("Robin Williams", 40, 9)
# temporary_secretary = employees.TemporarySecretary("Robin Williams", 40)

## If you try to force HourlyEmployee initialization with explicit init method
# same errors
# temporary_secretary = employees.TemporarySecretary("Robin Williams", 40, 9)
# temporary_secretary = employees.TemporarySecretary("Robin Williams", 40)

## Python's MRO (inheritance order)

# print(TemporarySecretary.__mro__)  # no init method: HourlyEmployee, Secretary
# print(TemporarySecretary.__mro__)  # no init method: Secretary, HourlyEmployee

# init method doesn't change the MRO
# print(TemporarySecretary.__mro__)  # init method: HourlyEmployee, Secretary
# print(TemporarySecretary.__mro__)  # init method: Secretary, HourlyEmployee

# We can solve the error with new init method that skips Sec. and Sal. Employee MROs
# print(TemporarySecretary.__mro__)  # mro doesn't change but now we can create the obj
# temporary_secretary = TemporarySecretary("Robin Williams", 40, 9)

# company_employees = [temporary_secretary]

# productivity_system = ProductivitySystem()
# productivity_system.track(company_employees, 40)

# # similar problem
# # payroll_system = PayrollSystem()
# # payroll_system.calculate_payroll(company_employees)

# # if you force the correct calculate_payroll method it will now work
# payroll_system = PayrollSystem()
# payroll_system.calculate_payroll(company_employees)

## Solution: separate calculate hours and payroll methods
ma = Manager("fulano", 1200)
# print(ma.id)
# print(ma.name)
# print(ma.weekly_salary)
# print(ma.calculate_payroll())
# print(ma.work(40))

se = Secretary("ciclano", 1000)
# print(se.id)
# print(se.name)
# print(se.weekly_salary)
# print(se.calculate_payroll())
# print(se.work(40))

sp = SalesPerson("beltrano", 400, 300)
# print(sp.id)
# print(sp.name)
# print(sp.weekly_salary)
# print(sp.commission)
# print(sp.calculate_payroll())
# print(sp.work(40))


fw = FactoryWorker("clauclau", 40, 15)
# print(fw.id)
# print(fw.name)
# print(fw.hours_worked)
# print(fw.hourly_rate)
# print(fw.calculate_payroll())
# print(fw.work(40))

temp_sec = TemporarySecretary("godines", 40, 20)
# print(temp_sec.id)
# print(temp_sec.name)
# print(temp_sec.hours_worked)
# print(temp_sec.hourly_rate)
# print(temp_sec.calculate_payroll())
# print(temp_sec.work(40))

payroll = PayrollSystem()
productivity = ProductivitySystem()

emps = (ma, se, sp, fw, temp_sec)
payroll.calculate_payroll(emps)
productivity.track(emps, 40)
