names = ['james', 'john', 'jack']
email_domains = ["gmail", "hotmail", "yahoo"]

for i,j in zip(names, email_domains):
    print("{}@{}.com".format(i, j))

print("")

def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"

    f = (c * 9 / 5) + 32
    return f

temperatures=[10,-20,-289,100]
for temperature in temperatures:
    print(c_to_f(temperature))
