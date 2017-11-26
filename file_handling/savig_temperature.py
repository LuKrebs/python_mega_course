file = open('temperature.txt', 'w')

temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"

    f=(c*9/5)+32
    file.write("{} {}".format(f, "\n"))
    return f

for t in temperatures:
    c_to_f(t)
