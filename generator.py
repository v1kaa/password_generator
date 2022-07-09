# lets start
import string
import random

pas = []
for k in range(6):
    pas.append(random.choice(string.ascii_lowercase))
for _ in range(random.randint(2, 3)):
    pas.append(random.choice(string.digits))
for _ in range(random.randint(2, 3)):
    pas.append(random.choice(string.punctuation))
for _ in range(random.randint(4, 5)):
    pas.append(random.choice(string.ascii_uppercase))

random.shuffle(pas)
password = ''.join(pas)
# print(password)
