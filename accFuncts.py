# accFuncts is short for Account Functions
from exitMenu import exit_menu
from os import path as ospath
from resetScreen import reset_screen
from sys import path as syspath


# This function creates user accounts ("accs") of two types: manager accounts and employee accounts (which both have different levels of access to certain functionalities within the program)


# Saves account settings menus from accMenus.txt to a list
acc_menus_lst = []

with open(ospath.join(syspath[0], "accMenus.txt"), 'r') as f:
    reader = f.read().splitlines()
  
for menuLine in list(reader):
    acc_menus_lst.append(menuLine.replace('\\n', '\n'))

def manager_check(user_name, valid_accs):
    # Checks if user is a manager or an employee)
    if valid_accs[user_name][0] == "manager":
        return True
    else:
        return False


def print_menu(manager_status):
      # Saves menu items according to manager or employee status (ex. employees can only access employee actions, not manager-only actions)
    
    if manager_status == True:
        for line in range(len(acc_menus_lst)):
          print(acc_menus_lst[line])
    else:
        print(acc_menus_lst[0])


def acc_menu(manager_status):

    # Initial menu print
    reset_screen(False)
    print_menu(manager_status)
    
    # Allows user to enter menu items allowed based on their status as a manager or employee
    while True:
      act = input("SELECT AN ACTION: ").strip()
      act_valid = True
  
      # Ensures only managers can access manager-only functions
      if act == "1":
          change_pass()
      elif act == "2" and manager_status:
          create_acc()
      elif act == "3" and manager_status:
          delete_acc()
      elif act == "exit":
          exit_menu()
      else:
          act_valid = False
        
      reset_screen(False)
      print_menu(manager_status)
      
      if not act_valid:
          print("Invalid action. Please try again.")


def write_users_csv():
    print


def change_pass():
   new_pass = input(str(""))


def create_acc():
    print("Test create_acc")


def delete_acc():
    print("Test delete_acc")