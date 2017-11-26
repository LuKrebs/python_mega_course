# Strings
c = "Hi there!"
replace_string = c.replace("e", "i")
print(replace_string)

# printing all the available methods to use on Strings
print(dir(c))

# printing help for a method or execute the same on the command line
# print(help("".replace))

# Indexing Strings
c = "Hi there!"
# first string
print(c[0])
# last string
print(c[-1])

# the two first: zero up to two, but not include 2
print(c[0:2])
print(c[-3:-1])
print(c[-4:])
