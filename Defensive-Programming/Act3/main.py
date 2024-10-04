import base64
import hashlib

class ISS_Lab:
    def __init__(self, data):
        if not isinstance(data, str):
            raise ValueError("Data must be a string")
        self.data = data
        self.data_hash = "sha256$" + hashlib.sha256(self.data.encode()).hexdigest()
    
    def encrypt(self):
        if not isinstance(self.data, str):
            raise ValueError("Data must be a string")
        self.data = base64.b64encode(self.data.encode()).decode()
        self.data_hash = "sha256$" + hashlib.sha256(self.data.encode()).hexdigest()
        print("Encryption successful!")
    
    def decrypt(self):
        if not isinstance(self.data, str):
            raise ValueError("Data must be a string")
        try:
            self.data = base64.b64decode(self.data).decode()
        except ValueError:
            raise ValueError("Data must be a valid base64 string")
        self.data_hash = "sha256$" + hashlib.sha256(self.data.encode()).hexdigest()
        print("Decryption successful!")
    
    def hash(self):
        if not isinstance(self.data, str):
            raise ValueError("Data must be a string")
        self.data_hash = "sha256$" + hashlib.sha256(self.data.encode()).hexdigest()
        print(f"New hash: {self.data_hash}")
        print("Hashing successful!")
    
    def verify(self, data):
        if not isinstance(data, str):
            raise ValueError("Data must be a string")
        if self.data_hash == "sha256$" + hashlib.sha256(data.encode()).hexdigest():
            print("Verification successful!")
            return True
        else:
            print("Verification failed!")
            return False
    
    def view(self):
        return self.data
    
    def backup(self):
        if not isinstance(self.data, str):
            raise ValueError("Data must be a string")
        try:
            with open("backup.txt", "w") as f:
                f.write(self.data)
        except IOError as e:
            print(f"Error writing backup file: {e}")
        else:
            print("Backup successful!")
    
    def restore(self):
        try:
            with open("backup.txt", "r") as f:
                self.data = f.read()
        except FileNotFoundError:
            print("Backup file not found!")
        except IOError as e:
            print(f"Error reading backup file: {e}")
        else:
            print("Restore successful!")


def main():
    while True:
        user_input = input("Enter data: ")
        try:
            iss_lab = ISS_Lab(user_input)
        except ValueError as e:
            print(e)
            continue
        while True:
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Hash")
            print("4. Verify")
            print("5. View")
            print("6. Backup")
            print("7. Restore")
            print("8. Exit")
            option = input("Choose an option: ")

            match option:
                case "1":
                    iss_lab.encrypt()
                case "2":
                    iss_lab.decrypt()
                case "3":
                    iss_lab.hash()
                case "4":
                    iss_lab.verify(user_input)
                case "5":
                    print(iss_lab.view())
                case "6":
                    iss_lab.backup()
                case "7":
                    iss_lab.restore()
                case "8":
                    break
                case _:
                    print("Invalid option")
        break


if __name__ == "__main__":
    main()