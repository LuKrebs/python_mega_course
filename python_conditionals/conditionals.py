a = 5

if a < 5:
    print("less than 5")
elif a == 5:
    print("equal to 5")
else:
    print("greater than 5")

def age_foo(age):
    new_age = float(age) + 50
    return new_age

age = int(input("Enter your age: "))

if age < 150:
    print(age_foo(age))
else:
    print("How is that possible?")
