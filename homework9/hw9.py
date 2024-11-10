import re
while True:
    def parse_email(email):
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if re.match(pattern, email):
            username, domain = email.split("@")
            return username, domain
        else:
            return None, None

    def main():
        email = input("Введите email: ")
        username, domain = parse_email(email)
        if username and domain:
            print(f"Username: {username}")
            print(f"Domain: {domain}")
        else:
            print("Некорректный email")

    if __name__ == "__main__":
        main()
