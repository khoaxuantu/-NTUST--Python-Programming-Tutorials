# Encryption-Decryption Program
 
<b>Purposes:</b>
- Write a program that encrypts all uppercase, lowercase and digits.
- If the input text is not uppercase, lowercase, or digits, it will not be encrypted.
- The program must be able to output "encrypted text" and "decrypted text".


<b>Hints:</b>
- Create Lists for 0 ~ 9, A ~ Z, a ~ z and merge all of them:<br>
  key_09 = [chr(d) for d in range(48, 48+10)]<br>
  key_AZ = [chr(A) for A in range(65, 65+26)]<br>
  key_az = [chr(a) for a in range(97, 97+26)]<br>
  table_encode_key = key_09 + key_AZ + key_az
- Shuffle the merged table for encryption:<br>
  table_encode_value = copy.copy(table_encode_key)
  random.shuffle(table_encode_value)
