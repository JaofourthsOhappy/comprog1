# import math
# h = float(input("How many hours?: "))
# b = float(input("How many Bath per hour?: "))
# park = (math.ceil(h))*b
# print(f"Parking fee is {park:.2f} Baht.")
# TV   = 3000
# Oven = 1500
# Fan  = 1000

# def cal_tv(amount):
#     return amount * TV
# def cal_oven(amount):
#     return amount * Oven
# def cal_fan(amount):
#     return amount * Fan
# tv   = int(input("How many TVs?: "))
# oven = int(input("How many ovens?: "))
# fan  = int(input("How many fans?: "))
# print(f"Total price is {cal_tv(tv)+cal_oven(oven)+cal_fan(fan)} Baht.")

# import math
# def cal_fee(h,b):
#     return math.ceil(h)*b
# h = float(input("How many hours?: "))
# b = float(input("How many Baht per hour?: "))
# print(f'Parking fee is {cal_fee(h,b):.2f} Baht.') 
# a = int(input("How many adults?: "))
# c = int(input("How many children?: "))
# day = str(input("Day (su,mo,tu,we,th,fr,sa): "))
# if day != "su" and day != "mo" and day!= "tu" and day!= "we" and day!="th" and day !="fr" and day!="sa":
#     print("Incorrect input!")
# else :
#     a_p = a*500
#     c_p = c*250
#     tol = a_p+c_p
#     print(f"{a} adults = {a}x500 = {a_p}")
#     print(f"{c} children = {c}x250 = {c_p}")
#     if day == "we":
#         dis_50 = (tol)*0.5 
#         print(f"Wednesday discount 50%  = ({a_p} + {c_p}) x 50% = {dis_50:.2f}")
#         if c_p >= 1000:
#             dis_20 = c_p*0.2
#             print(f"Wednesday children over {c_p} discount 20% = {c_p} x 20% = {dis_20:.2f}") 
#             print(f"Total price is {(tol-dis_50)-dis_20:.2f} Baht.")  
#         else:
#             print(f"Total price is {tol-dis_50:.2f} Baht.")  
#     else:
#             print(f"Total price is {tol:.2f} Baht.")
#     if day == "tu":
#         dis_25 = tol*0.25 
#         print(f"Tuesday discount 25%  = ({a_p} + {c_p}) x 25% = {dis_25:.2f}")
#         print(f"Total price is {tol-dis_25:.2f} Baht.")
#     else:
#         print(f"Total price is {tol:.2f} Baht.")
