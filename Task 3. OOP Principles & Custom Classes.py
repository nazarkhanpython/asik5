class Person:
    def __init__(self, name, age):
        self.name = name       
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

class Student(Person):     
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):     
        return f"My name is {self.name}, I am {self.age}, student ID: {self.student_id}"

def main():
    person = Person("Ali", 20)
    student = Student("Dana", 19, "ST-01")

    print(person.introduce())
    print(student.introduce())


if __name__ == "__main__":
    main()