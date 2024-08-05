
# is_goodcredit = True
# price = 100000
# if is_goodcredit:
#     down_payment = 10/100*price
# else:
#     down_payment = 20/100*price
# print(f"down payment = ${down_payment}")

has_high_income = True
has_good_credit = True
has_criminal_record = True

# Logical Operators:
# AND:
# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# OR:
# if has_good_credit or has_high_income:
#     print("Eligible for loan")

# NOT:
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

# temprature = 30

# if temprature > 30:
#     print("It's a hot day")
# elif temprature < 10:
#     print("It's a cold day")
# else:
#     print("It's neither hot or cold")


# name = "O"

# if len(name) < 3:
#     print("Name must be atleast 3 chracters long")
# elif len(name) > 50:
#     print("Name can be maximum of 50 characters")
# else:
#     print("Name looks good!")


weight = int(input("Enter weight: "))
is_lb_or_pound = input("L for lbs and K for Kg: ")


if is_lb_or_pound == 'l' or is_lb_or_pound == 'L':
    converted = weight*0.45
    print(f"You are {converted} kg")
elif (is_lb_or_pound == 'k' or is_lb_or_pound == 'K'):
    converted = weight/0.45
    print(f"You are {converted} lbs")
