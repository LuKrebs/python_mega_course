file = open("fruits.txt", 'r')
content = file.read()
file.close()
print(content)

print("")
file = open("fruits.txt", 'r')
file.seek(0)
content = file.readlines()
file.close()
content = [i.rstrip("\n") for i in content]
for fruit in content:
    print(len(fruit))

print("")
file = open("exercise_two.txt", 'w')
numbers = [1, 2, 3]
for n in numbers:
    file.write("{} {}".format(n, "\n"))

file.close()
