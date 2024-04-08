"""
PowerOfTen
"""
# Provide your solution here
# n = int(input("enter a max 3 digit number: "))
# if n < 0:
#     print("number cannot be negative")
# elif n > 999:
#     print("number has more than 3 digits")
# elif n > 0 and n <= 999:
#     if n < 10:
#         print(f"{n} = {n} * 1")
#     elif n >= 10 and n < 100:
#         print(f"{n} = {n//10} * 10 + {n%10} * 1")
#     elif n >= 100 and n < 999:
#         print(f"{n} = {n//100} * 100 + {n//10%10} * 10 + {n%10} * 1")



pay = int(input("to pay: "))

if pay <= 0:
    print("negative payment is invalid")
elif pay > 0:
    rec = int(input("received: "))
    if int(pay) > int(rec):
        print("you did not pay enough")
    elif int(rec) > int(pay):
        diff = int(rec) - int(pay)
        print("your change is: ", int(diff))
    elif rec <= 0:
        print("negative received payment is invalid.")

"""
Cash Box
"""
# Provide your solution here
