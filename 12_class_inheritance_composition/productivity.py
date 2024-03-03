# class ProductivitySystem:
#     def track(self, employees, hours):
#         print("Tracking Employee Productivity")
#         print("==============================")
#         for employee in employees:
#             employee.work(hours)
#         print("")


class ProductivitySystem:
    def track(self, employees, hours):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            result = employee.work(hours)
            print(f"{employee.name}: {result}")
        print("")


## Solution for multiple inheritance error
# These class are not instantiated. They only serve to be inherited


class ManagerRole:
    def work(self, hours):
        return f"screams and yells for {hours} hours."


class SecretaryRole:
    def work(self, hours):
        return f"expends {hours} hours doing office paperwork."


class SalesRole:
    def work(self, hours):
        return f"expends {hours} hours on the phone."


class FactoryRole:
    def work(self, hours):
        return f"manufactures gadgets for {hours} hours."
