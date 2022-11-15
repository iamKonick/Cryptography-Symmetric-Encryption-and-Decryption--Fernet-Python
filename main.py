from cryptography.fernet import Fernet

f = Fernet(b'iI0wdMEysPRLW4aSckKtoSs0G7BA9fc3Jf6QjJexh0E=')

encrypted = b'gAAAAABfLCA9FCFclrsHxWr9QGvm-1hUBUPuCWYOkeD5QWz9wq0cJ0ugAe4DJpx-M0VVo3WTE2SC-wwEXUKizVG0Nun-jjHtGg=='

decrypted = f.decrypt(encrypted).decode("utf-8")

print(decrypted)

## Tapire is the decrypted word
