import matplotlib.pyplot as plt

def plot_expenses(expense_list):
  '''Function that will be used to plot bar chart of the expenses list'''
  #extracting category and amount in seperate lists using list comprehension
  categories=[expense['category'] for expense in expense_list]
  amounts=[expense['amount'] for expense in expense_list]

  plt.bar(categories, amounts)
  plt.xlabel("Categories")
  plt.ylabel("Amount")
  plt.title("Categories Vs Amount")
  plt.show()


def plot_income(income_list):
  '''Function that will be used to plot bar chart of the income list'''
  #extracting source and income in seperate lists using list comprehension
  sources=[sour['source'] for sour in income_list]
  incomes=[inc['amount'] for inc in income_list]


  plt.bar(sources, incomes)
  plt.xlabel("Source")
  plt.ylabel("Income")
  plt.title("Source Vs Income")
  plt.show()
