""""
Q5 Using a while loop, verify if the number A is purely divisible by number B and if so then how many
times it can be divisible.
"""""
#
# A = 81
# B = 9
# count = 0
#
# while A%B == 0:
#     count = count+1
#     a= A/B
#
# if count!=0:
#     print("A is Divisible by B")
#     print("Number of time divisible is:",count)
#
# else:
#     print("A is not Divisible by B")
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
