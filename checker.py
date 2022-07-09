from generator import password
import string

totalup, totallv, totaldig, totalpn = 0, 0, 0, 0

if len(password) < 14:
    print('The password must be least 14 characters long')

for i in string.ascii_uppercase:
    if i in password:
        totalup += 1
if totalup == 0:
    print('The password must contains uppercase characters')

for k in string.ascii_lowercase:
    if k in password:
        totallv += 1
if totallv == 0:
    print('The password must contains  lowercase')

for h in string.digits:
    if h in password:
        totaldig += 1
if totaldig == 0:
    print('The password must contains at least one digit')

for j in string.punctuation:
    if j in password:
        totalpn += 1
if totalpn == 0:
    print('The password must contains at least one punctuation character')

elif totalup != 0 and totallv != 0 and totalpn != 0 and totaldig != 0:
    print('good')
