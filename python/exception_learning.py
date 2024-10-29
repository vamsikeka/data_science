x = input("enter the 1st number: ")
y = input("enter the 2nd number: ")

try:
    #z=int(x)/int(y)
    z = x / int(y)

#except Exception as e:
except ZeroDivisionError as e:
    print('exception occured: ', e)
    z=None

except Exception as e:
    print('exception type ', type(e).__name__)
    z = None

print('division is :', z)

#Google python built in exceptions to see standard list of exceptions
