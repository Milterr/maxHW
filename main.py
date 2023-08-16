def polin(str):
    if str[::-1] == str:
        return True
    else:
        return False
print(polin(input('Введите слово')))