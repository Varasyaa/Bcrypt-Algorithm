import bcrypt

# Your original password
password = "mypassword"

# Read the hash from the file
with open("hash.txt", "rb") as f:
    stored_hash = f.read()

# Check if the password matches the hash
if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
    print("The password matches the hash.")
else:
    print("The password does not match the hash.")
