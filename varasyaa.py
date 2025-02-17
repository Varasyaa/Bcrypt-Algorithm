import bcrypt

# Plaintext password to hash
password = "VarasyaaMohan123"

# Generate the bcrypt hash
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Save the hash to a file (optional)
with open("hash.txt", "wb") as f:
    f.write(hashed)

# Print the hashed password
print("Hashed password:", hashed)

# Read the hash from the file
with open("hash.txt", "rb") as f:
    stored_hash = f.read()

# Check if the plaintext password matches the hash
if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
    print("The password matches the hash.")
else:
    print("The password does not match the hash.")
