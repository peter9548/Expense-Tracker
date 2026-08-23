##                        ===== Expense Tracker =====                           ##


class Expense:
    def __init__(self,amount,category,description):
        self.amount =amount
        self.category =category
        self.description =description


# expense1 =Expense(12000,"EMI","This is Homecredit EMI")
# print(expense1.amount)
# print(expense1.category)
# print(expense1.description)




expenses = []

# expense2 = Expense(5000,"Food","This is for food")
# expenses.append(expense2)




# amount = int(input("Enter your amount:"))
# category = input("Enter your category:")
# description = input("Enter your description:")

# expense3 = Expense(amount,category,description)
# expenses.append(expense3)

for expense in expenses:
    print(expense.amount)
    print(expense.category)
    print(expense.description)



while True:
    print("1. Add expense")
    print("2. Display expense")
    print("3. Total expense")
    print("4. Exit")
    choice =int(input("Enter your choice:"))

    if choice ==1:
        amount =int(input("Enter your amount:"))
        category =input("Enter your category:")
        description =input("Enter your description:")

        expense3 =Expense(amount,category,description)
        expenses.append(expense3)

    elif choice ==2:
        for expense in expenses:
            print(expense.amount)
            print(expense.category)
            print(expense.description)

    elif choice ==3:
        total_expense =0
        for expense in expenses:
            total_expense += expense.amount
        print("Total expense:",total_expense)

    elif choice ==4:
        break


    else:
        print("invalid choice")




