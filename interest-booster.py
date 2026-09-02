money = float(input("Enter the amount of money: "))
is_member = int(input("Are you a member of the bank? [1 = Yes | 0 = No]: ")) == 1

if is_member:
    age = int(input("Enter your age:"))
    paid_last_month = float(input("Enter the amount you paid last month: "))
    credit_score = int(input("Enter your credit score: "))

    interest_rate = 4.5

    if age > 21:
        interest_rate += 0.5
    if paid_last_month > 100:
        interest_rate += 1
    if credit_score > 700:
        interest_rate += 2

    final_amount = money + (money * interest_rate / 100)

    print(f"Final money with interest: {final_amount:.2f}")
else:
    print("You are not a member. No interest will be added.")
