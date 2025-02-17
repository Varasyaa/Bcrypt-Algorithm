import bcrypt

def generate_hash(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

password = "Varas@@07"

hash1 = generate_hash(password)
hash2 = generate_hash(password)

print("Hash 1:", hash1)
print("Hash 2:", hash2)
