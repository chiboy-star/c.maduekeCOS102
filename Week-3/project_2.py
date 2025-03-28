print("            Welcome to Lzifin Technology")
staff_age = int(input("How old are you?: "))
staff_work_exp = int(input("How many years of work experince do you have?: "))

if staff_work_exp > 25 and staff_age >= 55:
    print("Your Annual Tax Revenue(ATR) is 5,600,000")
elif staff_age >= 45 and staff_work_exp > 20:
    print("Your Annual Tax Revenue(ATR) is 4,480,000")
elif staff_age >= 35 and staff_work_exp > 10:
    print("Your Annual Tax Revenue(ATR) is 1,500,000")
else:
     print("Your Annual Tax Revenue(ATR) is 550,000")