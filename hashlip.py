import hashlib

target = input("Enter the MD5 hash to crack: ")

with open("rockyou.txt", "r") as file:
    for line in file:
        password = line.strip()

        result = hashlib.md5(
            password.encode()
        ).hexdigest()

        if result == target:
            print("Found:", password)
            break
    else:
        print("No match found")