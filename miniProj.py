#my first mini project in python
import random
i=0
while True:
    up = "QWERTYUIOPASDFGHJKLZXCVBNM"
    do = "qwertyuiopasdfghjklzxcvbnm"
    sym = "!@#$%^&*()_+="
    num = "1234567890"
    all = up+do+sym+num
    lenght= 12
    password="".join(random.choices(all,k=lenght))
    print(password)
    i +=1
    if i == 5:
        break