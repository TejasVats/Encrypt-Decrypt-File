from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("secret.key","wb") as key_file:
        key_file.write(key)

# Uncomment to generate a new key
# write_key() // it generate the secret key

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

# UNCOMMNENT TO ENCRYPT FILE
# encrypt_file("SECRETS.TXT")

# UNCOMMNENT TO DECRYPT FILE
# decrypt_file("SECRETS.TXT")