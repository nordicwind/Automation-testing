import random


class Generator:
    def __init__(self):
        self.password_chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        self.email_chars = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        self.name_chars = "abcdefghijklnopqrstuvwxyz"
        self.domains = ['@gmail.com', '@mail.ru', '@rambler.ru', '@microsoft.com']
        self.spec_symbols = list("+-/*!&$#?=@<>°«©®»•'")

    def valid_email(self):
        email_part1 = self.random_string()
        email_part2 = random.choice(self.domains)
        email = email_part1 + email_part2
        return email

    def invalid_email(self):
        spec_symbols = random.choice(self.spec_symbols)
        email = self.valid_email() + spec_symbols
        return email

    def valid_password(self):
        password = ''
        for i in range(random.randint(6, 129)):
            password += random.choice(self.password_chars)
        return password

    def too_short_password(self):
        password = ''
        for i in range(random.randint(1, 6)):
            password += random.choice(self.password_chars)
        return password

    def too_long_password(self):
        password = ''
        for i in range(random.randint(129, 150)):
            password += random.choice(self.password_chars)
        return password

    def empty_password(self):
        password = ''
        return password

    def normal_name(self):
        name_part1 = random.choice(self.name_chars.upper())
        name_part2 = ''
        for i in range(random.randint(6, 16)):
            name_part2 += random.choice(self.name_chars)
        name = name_part1 + name_part2
        return name

    def too_long_name(self):
        name_part1 = random.choice(self.name_chars.upper())
        name_part2 = ''
        for i in range(random.randint(256, 300)):
            name_part2 += random.choice(self.name_chars)
        name = name_part1 + name_part2
        return name

    def empty_name(self):
        name = ''
        return name

    def random_string(self):
        random_string = ''
        for i in range(random.randint(6, 16)):
            random_string += random.choice(self.email_chars)
        return random_string
