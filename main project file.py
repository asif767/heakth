# import datetime
# def gettime():
#     return datetime.datetime.now()
# def take(k):
#     if k==1:
#         c=int(input("enter 1 for excersise and 2 for food"))
#         if(c==1):
#             value=input("type here\n")
#             with open("harry-ex.txt","a") as op:
#                 op.write(str([str(gettime())])+": "+value+"\n")
#             print("successfully written")
#         elif(c==2):
#             value = input("type here\n")
#             with open("harry-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif(k==2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("rohan-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("rohan-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif(k==3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("hammad-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("hammad-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     else:
#         print("plz enter valid input (1(harry),2(rohan),3(hammad)")
# def retrieve(k):
#     if k==1:
#         c=int(input("enter 1 for excersise and 2 for food"))
#         if(c==1):
#             with open("harry-ex.txt") as op:
#                 for i in op:
#                     print(i,end="")
#         elif(c==2):
#             with open("harry-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif(k==2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("rohan-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("rohan-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif(k==3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("hammad-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("hammad-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     else:
#         print("plz enter valid input (harry,rohan,hammad)")
# print("health management system: ")
# a=int(input("press 1 for lock the value and 2 for retrieve "))
#
# if a==1:
#     b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
#     take(b)
# else:
#     b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
#     retrieve(b)
#
#









#Trying my own program


import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("Harry ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("Harry.txt", "a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
    elif k==2:
        c = int(input("Enter 1 for excersise and 2 for food"))
        if (c==1):
            value = input("Type hare\n")
            with  open("rohan exe.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif (c==2):
            value = input("Type hare\n")
            with open("rohan.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
    elif k==3:
        c = int(input("Enter 1 for execrsise and 2 for food"))
        if (c==1):
            value = input("Type hare\n")
            with open("Hamad exe.txt") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif (c==2):
            value = input("Type hare\n")
            with open("Hamad.txt") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
    else:
        print("plss enter a valid Entry (harry),(rohan), (hamad)")
def retrive(k):
    if k==1:
        c = int(input("Enter 1 for execersise and 2 for food"))
        if c==1:
            with open("Harry ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("Harry.txt") as op:
                for i in op:
                    print(i,end="")
    elif k==2:
        c = int(input("Enter 1 for execersise and 2 for food"))
        if (c==1):
            with open("rohan exe.txt") as op:
                for i in op:
                    print(i,end="")
        elif (c==2):
            with open("rohan.txt") as op:
                for i in op:
                    print(i,end="")
    elif k==3:
        c = int(input("Enter 1 for execersise and 2 for food"))
        if (c==1):
            with open("Hamad exe.txt") as op:
                for i in op:
                    print(i,end="")
        if (c==2):
            with open("Hamad.txt") as op:
                for i in op:
                    print(i,end="")
    else:
        print("plss enter a valid entery (harry), (rohan), (hamad)")
print("Health managment system")
a = int(input("Press 1 for log and 2 for retrive "))
if a==1:
    b = int(input("Press 1 for Harry 2 for rohan 3 for hamad"))
    take(b)
else:
    b = int(input("Press 1 for Harry 2 for rohan 3 for hamad "))
    retrive(b)

