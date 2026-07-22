from data_management import save_data

def add_expense():
  '''Function to take input for expense from the user.'''
  amount=float(input("Enter amount spend: "))
  category=input("Category of amount spend: ")
  date=input("Date of spending (YYYY-MM-DD): ")
  expense={"amount": amount, "category": category, "date": date}

  save_data(expense, 'expenses.txt')


def add_income():
  '''Function to take income input from the user.'''
  amount=float(input("Enter income amount: "))
  source=input("Enter source of income: ")
  date=input("Date of credit (YYYY-MM-DD): ")
  income={"amount": amount, "source": source, "date": date}
  save_data(income, 'income.txt')




