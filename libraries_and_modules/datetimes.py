import datetime as dt

filename = dt.datetime.now()

def create_file(filename):
    name_of_the_file = str(filename)
    file = open("{}.txt".format(name_of_the_file), "w")
    file.write("{}".format(name_of_the_file))
    file.close()

create_file(filename)
now = dt.datetime.now()
formated_date = now.strftime("%Y-%m-%d-%H-%M")
print(formated_date)
