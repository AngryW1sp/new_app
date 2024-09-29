def vaporcode(s):
    total = ''
    for i in s:
        if i == '':
            total += ''
            
        else:
            total += i.upper()
            total += '  '
    return total