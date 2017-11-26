def string_length(mystring):
    if type(mystring) == int or type(mystring) == float:
        return "Sorry integers don't have length"

    return len(mystring)

def celcius_to_fahrenheit(celcius):
    if celcius < -273.15:
        return "It's not possible"
    fahrenheit = celcius * 9/5 + 32
    return fahrenheit
