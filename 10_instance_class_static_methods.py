class ClassTest:
    def instance_method(self):
        print(f"Called an instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called a class method of {cls}")

    def static_method():
        print(f"Called a static method.")


class_test = ClassTest()
# class_test.instance_method()
# class_test.class_method()
# class_test.static_method()  # error

# ClassTest.instance_method()  # error
# ClassTest.class_method()
# ClassTest.static_method()

# ClassTest.instance_method(class_test)
# ClassTest.class_method(class_test)  # error
# ClassTest.static_method(class_test)  # error

# ClassTest.instance_method(ClassTest)
# ClassTest.class_method(ClassTest)  # error
# ClassTest.static_method(ClassTest)  # error

# correct ways to call these methods
class_test.instance_method()
ClassTest.class_method()
ClassTest.static_method()
