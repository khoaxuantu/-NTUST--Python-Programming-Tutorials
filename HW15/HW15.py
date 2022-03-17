# Encrypting all uppercase, lowercase and digits.
import random
import copy

# Create list for 0~9, A~Z, a~z
key_09 = [chr(d) for d in range(48, 48+10)]
key_AZ = [chr(A) for A in range(65, 65+26)]
key_az = [chr(a) for a in range(97, 97+26)]

# Create an encode key table
table_encode_key = key_az + key_AZ + key_09
table_encode_value = copy.copy(table_encode_key)
random.shuffle(table_encode_value)

table_encode = dict(zip(table_encode_key, table_encode_value))
print(f"Encoding table: {table_encode}")
print()

table_decode = {v:k for k, v in table_encode.items()}
print(f"Decoding table: {table_decode}")
print()

# Ask user to input text
text = input("Please enter text to be encrypted (alphabets or numbers): ")

# Encrypting text
encrypt_text = ''
for c in text:
    e = table_encode.get(c, None)
    if e is not None:
        encrypt_text += e
    else:
        encrypt_text += c
print(f"Encrypted text: {encrypt_text}")

# decrypting text
decrypt_text = ''
for c in encrypt_text:
    e = table_decode.get(c, None)
    if e is not None:
        decrypt_text += e
    else:
        decrypt_text += c
print(f"Decrypted text: {decrypt_text}")
