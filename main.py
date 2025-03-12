import datetime
import random
import re


class User:
    def __init__(self, user_id, name, surname, email, password, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday

    def get_details(self):
        return f'User ID: {self.user_id}, Name: {self.name}, Surname: {self.surname}, Email: {self.email}'

    def get_age(self):
        today = datetime.date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))


class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id, None)

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, user_update):
        if user_id in cls.users:
            cls.users[user_id] = user_update

    @classmethod
    def get_number(cls):
        return len(cls.users)


class UserUtil:
    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.datetime.now().year)[-2:]
        random_digits = str(random.randint(1000000, 9999999))
        return int(year_prefix + random_digits)
    
    @staticmethod
    def generate_password():
        import string
        import random
        characters = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(random.choice(characters) for _ in range(8))
            if UserUtil.is_strong_password(password):
                return password
            
    @staticmethod
    def is_strong_password(password):
        return (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in '!@#$%^&*()-+=' for c in password) 
        )
            
    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}.kg"
    
    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None


def main():
    print("Welcome to the User Management System!\n")
    while True:
        print("\nChoose an option:")
        print("1. Add a new user")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            name = input("Enter your first name: ")
            surname = input("Enter your last name: ")

            while True:
                try:
                    birthday_str = input("Enter your birthday (YYYY-MM-DD): ")
                    birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Invalid date format. Please try again in YYYY-MM-DD format.")

            user_id = UserUtil.generate_user_id()
            email = UserUtil.generate_email(name, surname, "alatoo.edu")
            password = UserUtil.generate_password()

            user = User(user_id, name, surname, email, password, birthday)
            UserService.add_user(user)

            print("\nUser successfully created!")
            print(user.get_details())
            print(f"Generated Password: {password} (Keep it safe!)")
            print(f"Age: {user.get_age()}")
            print("\nTotal Users in System:", UserService.get_number())

        elif choice == "2":
            print("\nThank you for using the User Management System!")
            break
        else:
            print("\nInvalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
