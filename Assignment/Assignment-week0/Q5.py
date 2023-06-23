""""
note - This Assignment are written in the pycharm

Q5 Using a while loop, verify if the number A is purely divisible by number B and if so then how many
times it can be divisible.
"""""

a= 20
b = 2
count = 0

while a % b == 0:
    count += 1
    a /= b

if count!=0:
    print(f"The number a is divisible by b exactly {count} times.")
else:
    print("Number a is not Divisible by b")
