# class_static_methods_demo.py

class Calculator:
    # 🔹 Class Attribute (خاص بالكلاس وليس بالكائنات)
    calculation_type = "Arithmetic Operations"

    # 🔹 Static Method
    @staticmethod
    def add(a, b):
        """
        Static methods don't use class or instance data.
        They just perform a standalone task.
        """
        return a + b

    # 🔹 Class Method
    @classmethod
    def multiply(cls, a, b):
        """
        Class methods have access to class attributes and methods.
        'cls' refers to the class itself.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
