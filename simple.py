import numpy as np

'''
Write 6 print() statements to "draw" the following on the console

ooo/\ooo
oo/  \oo
o/ '' \o
/______\
|| || ||
xxxxxxxx

(hint: use escape sequence)
'''
line1 = 'ooo/\ooo'
line2 = 'oo/  \oo'
line3 = 'o/ \'\' \o'
line4 = '/______\\'
line5 = '|| || ||'
line6 = 'xxxxxxxx'
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)

# Why are comments invisible?????
image_print = """
ooo/\ooo
oo/  \oo
o/ '' \o
/______\\
|| || ||
xxxxxxxx
"""
print(image_print)
'''
Choose three positive values for a, b, and c such that the final print() statement returns True
'''

a = 1
b = 1
c = np.sqrt(2)
print(a**2 + b**2 == int(c**2))
