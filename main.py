import re # Import the regular expression module
import hashlib # Import the hashlib module for password hashing

from datetime import datetime # Import the datetime module for date and time

# Password hashing function

def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()

#Password Checker Function

def is_strong_password(password):
  if len(password) < 8:
    return False, "Password must be at least 8 characters long."

  if not re.search(r"[A-Z]", password):
    return False, "Password must contain at least one uppercase letter."

  if not re.search(r"[0-9]", password):
    return False, "Password must contain at least one number."

  if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    return False, "Password must contain one of the following special characters: !@#$%^&*(),.?\":{}|<>."

  return True, "Password is strong." #Must integrate this function into the registration function in the register_user function


# User Activity Logging Function

def log_event(event):
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open("audit_log.txt", "a") as log_file:
    log_file.write(f"{timestamp} - {event}\n")
    


# Registration Function

def register_user():
  username = input("Enter a username: ")
  password = input("Enter a password: ")

  is_vaild, feedback = is_strong_password(password)
  if not is_vaild:
    print("Password is not strong. Please try again.")
    print(feedback)
    log_event(f"Registration failed for user {username}")
    return

# Hash the password before storing it

  hashed_password = hash_password(password)
  
  with open("users.txt", "a") as file:
    file.write(f"{username}:{hashed_password}\n")
  print("Registration successful!")
  log_event(f"{username} successfully registered.")

#Login Function

def login_user():
  username = input("Enter your username: ")
  password = input("Enter your password: ")

  with open("users.txt", "r") as file:    #Open the file in read mode "r"
    users = file.readlines()

  for user in users:    #For loop to iterate through the users
    stored_username, stored_password = user.strip().split(":")  #Split the username and password using the colon
    if username == stored_username and hash_password(password) == stored_password:
      print("Login successful!")
      log_event(f"{username} successfully logged in.")
      post_login_menu(username)
      return

  print("Invalid username or password.")
  log_event(f"Failed login attempt for user {username}")

#Function to display Post Login Menu

def post_login_menu(username):
  while True:
    print("\nPost Login Menu")
    print("1. View my Logs")
    print("2. Logout")
    choice = input("What do you want to do? ")

    if choice == "1":
      view_logs(username)
    elif choice == "2":
      log_event(f"{username} successfully logged out.")
      print("Logged out successfully.")
      break
    else:
      print("Invalid choice. Please try again.") # Must integrate this function into the login function
      
# View Logs Function

def view_logs(username):
  print(f"\nLogs for user '{username}'")
  with open("audit_log.txt", "r") as log_file:
    logs = log_file.readlines()

  user_logs = [log.strip() for log in logs if username in log]

  if user_logs:
    for log in user_logs:
      print(log)

  else:
    print("No logs found for your account.")


def main():
  while True:
    print("Welcome to the user Registration System")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
      register_user()

    elif choice == "2":
      login_user()

    elif choice == "3":
       log_event("System exited.")
       print("Exiting the system. Goodbye!")
       break
      
    else:
     print("Invalid choice. Please try again.")

main()