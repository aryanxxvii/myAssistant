def check(str1, str2):
    for i in str2:
        str1 = str1.replace(i, '')
    return str1