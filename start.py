def add(a, b):
    print(a + b)
    return
add(3, 5)

def addAllNumbers(*numbers):
    print(sum(numbers))
    return
addAllNumbers(1,3,6,4,7,8,3)

def introduceYourself(**data):
    print(f"Name: {data['name']}, age: {data['age']}")
    return
introduceYourself(name = "Kuba", age = 20)