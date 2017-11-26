file = open('file_created.txt', 'w')
file.write("Line 1")
file.close()
file = open('file_created.txt', 'w')
file.write("Line 2")
file.close()

# Adding text line by Line
file = open('file_created.txt', 'w')
file.write("Line 1\n")
file.write("Line 2\n")
file.close()

l = ["Line 1", "Line 2", "Line 3"]
file = open('file_write_with_loop.txt', 'w')
for line in l:
    file.write("{} {}".format(line, "\n"))

file.close()
