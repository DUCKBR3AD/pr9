import re

def parse_email(email):
    pattern = r"(.*)@(.*)"
    match = re.match(pattern, email)
    if match:
        username = match.group(1)
        domain = match.group(2)
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
