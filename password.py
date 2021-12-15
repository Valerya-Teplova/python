#строка пароль. проверка на условия/
# True - подходит False - не подходит

print('Пароль должен соответствовать следующим условиям: \n1. Пароль должен содержать не менее 6 символов')
print('2. Пароль должен содержать хотя бы 1 цифру \n3. Пароль не должен состоять только из цифр')
print('4. Пароль не должен содержать слово "password"')

def password ():
    pas = input('Введите строку пароль: ')

    if len(pas) >= 6:
        if any(map(str.isdigit,pas)):
            if pas.isdigit() == False:
                if pas.lower().find('password') == -1:
                    print("True")
                else: print("False")
            else: print("False")
        else: print("False")
    else: print("False")

password()            