def minutes_to_hours(minutes):
    return (minutes / 60)


x = minutes_to_hours(70)
print(x)


def hello():
    return "Hello World"

def power(number):
    return (number ** 2)

# Function with two arguments and default argument
def minutes_to_hours_with_seconds(minutes=70, seconds):
    return ((minutes / 60) + (seconds / 3600))

print(minutes_to_hours_with_seconds(70, 7200))

def power(base, exponent):
    return (base ** exponent)
