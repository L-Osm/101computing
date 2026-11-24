# Done on 22/11/26, took 27 mins.
# Header to show user the purpose of the program.
print("┌──────────────────────────────────┐")
print("│     Smart Electricity Meter      │")
print("└──────────────────────────────────┘")
print("")

# Base rate of amount charged per kWh (in £s).
f_rate = 0.25

# User inputs for kWh usage throughout week.
mon = float(input("How many kWh did you use on Monday?: "))
tues = float(input("How many kWh did you use on Tuesday?: "))
wed = float(input("How many kWh did you use on Wednesday?: "))
thurs = float(input("How many kWh did you use on Thursday?: "))
fri = float(input("How many kWh did you use on Friday?: "))
sat = float(input("How many kWh did you use on Saturday?:"))
sun = float(input("How many kWh did you use on Sunday?: "))

# Collected in list to make later calculations quicker.
days_list = [mon, tues, wed, thurs, fri, sat, sun]
total = sum(days_list)
lowest = min(days_list)
chargeable_cons = total - lowest
lowest_day_bill = min(days_list) * 0.25
total_bill = total * 0.25
total_with_deal = chargeable_cons * 0.25

# Final output statements to inform user of final bill.
print("Chargeable consumption =", chargeable_cons, "kWh.")
print("Thanks to the free electricity day, you saved £",lowest_day_bill)
print("Your predicted electricity bill at the rate of £",f_rate, "per kWh, including the deal is: £",total_with_deal)