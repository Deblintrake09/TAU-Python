
def sum():
    a = 10
    b = 30
    print(a+b)


sum()



def inputaddition():
    a = int(input('Enter a number. '))
    b = int(input('Enter another number. '))
    print(a+b)


inputaddition()


def addition(a,b):
    print(a+b)


addition(5, 10)


def user_info(name,age=0 , city="Tucson"):
    print("{} is {} years old, from {}.".format(name, age, city))


user_info("Andres", 38, "San Luis")
user_info('Michael')
