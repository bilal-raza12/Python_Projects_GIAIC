class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}")
        self.age = age
    
def check_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    else:
        print(f"Valid age: {age}")

try:
    check_age(-5)
except InvalidAgeError as e:
    print(e)
