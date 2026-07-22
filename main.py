import user_interface, calculation, visualization
def main_menu():
  '''Function that will be used to display instructions and inputs from user'''
  print("1- for adding expense \n 2- for adding income \n 3- for viewing summaries \n 4- to exit the program")

  while(1):
    choice=input("Enter the appropriate command to proceed: ")
    if choice.isdigit():
      choice=int(choice)
      if(choice==1):
        user_interface.add_expense()
      elif (choice==2):
        user_interface.add_income()
      elif (choice==3):
        visualization.plot_expenses()
        visualization.plot_income()
      elif(choice==4):
        break
    else:
      print("Enter a valid choice from options!!!")

if '__name__' == __main__:
  '''will be used for running direct script'''
  #calling main_menu function to initial the project
  main_menu()


