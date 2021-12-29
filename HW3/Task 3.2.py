def my_func (name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])


name = input('enter name')
surname = input('enter surname')
year = input('enter year')
city = input('enter city')
email = input('enter email')
phone = input('input phone')


print(my_func(name =name, surname =surname, year =year, city =city, email =email,phone =phone))

