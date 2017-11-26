a = 5
b = 0
def divide(a,b):
    try:
        return(a/b)
    # except + the name of the error here:
    except ZeroDivisionError:
        return("Zero Division")

print(divide(1,0))
