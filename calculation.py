
def calculate_total_expenses(expenses):
  '''Function to add all expenses'''
  #initializaing expense with 0 and then adding up each expense for final total
  total_expense=0.0
  for expense in expenses:
    total_expense+=expense['amount']
  
  return total_expense

def calculate_total_income(income_list):
  '''Function to add on total income from all sources'''
  #initialized total income variable to 0 and then adding up to total as iteration
  total_income=0.0
  for income in income_list:
    total_income+=income['amount']

  return total_income

def calculate_net_income(total_income, total_expense):
  return total_income-total_expense
  
