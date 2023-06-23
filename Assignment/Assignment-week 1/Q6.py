"""
note - This Assignment are written in the pycharm

Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
divisible by 3 or not.
"""
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

for i in l:
    print(i)
    if(i%3==0):
        print("Element",i,"is Divisible by 3")
    else:
        print("Element", i, "is not Divisible by 3")
    print("")