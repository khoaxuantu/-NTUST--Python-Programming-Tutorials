# Check user password

# Input a password
password = input("Please enter the password: ")

# Strip the password
strip_pass = password.strip()
# Convert the input to lower case
strip_pass = strip_pass.lower()

# Check if the password is valid
if strip_pass == "python":
    print("Password is valid!")
else:
    print("Password is invalid!")
