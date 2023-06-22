def check_palindrom(my_string):
    if my_string == my_string[::-1]:
        return True
    return False
string = '121'
print(check_palindrom(string))