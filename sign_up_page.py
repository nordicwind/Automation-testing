from selenium.webdriver.common.by import By
from random_generator import Generator
from config import driver


class SignUpPage:
    def __init__(self, driver):
        driver.get("https://courses.ultimateqa.com/users/sign_up")
        self.driver = driver
        self.first_name_field = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        self.last_name_field = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        self.email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        self.new_password_field = driver.find_element(By.XPATH, "//input[@placeholder='New Password']")
        self.terms_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
        self.sign_up_btn = driver.find_element(By.XPATH, "//input[@type='submit']")

    """Calling function depends on email method parametr."""
    def check_email_method(self, email_method):
        if email_method == 'valid':
            email = Generator().valid_email()
        elif email_method == 'invalid':
            email = Generator().invalid_email()
        elif email_method == 'empty':
            email = ''
        elif email_method == 'registered':
            email = "test123@gmail.com"
        return email

    """Calling function depends on password method parametr."""
    def check_password_method(self, password_method):
        if password_method == 'too_short':
            password = Generator().too_short_password()
        elif password_method == 'too_long':
            password = Generator().too_long_password()
        elif password_method == 'empty':
            password = Generator().empty_password()
        else:
            password = Generator().valid_password()
        return password

    """Calling function depends on name method parametr."""
    def check_name_method(self, name_method):
        if name_method == 'normal_name':
            name = Generator().normal_name()
        if name_method == 'too_long':
            name = Generator().too_long_name()
        elif name_method == 'empty':
            name = Generator().empty_name()
        return name

    def check_exists_by_xpath(self, test_name, xpath):
        try:
            assert driver.find_element(By.XPATH, xpath)
            return f"Test: {test_name}.\nStatus: Passed"
        except:
            return f"Test: {test_name}.\nStatus: Failed"

    """Main sign up function, which works with check functions and generates all data to sign up new account."""
    def registration(self, name_method, email_method, password_method, checkbox_method):
        first_name = self.check_name_method(name_method)
        last_name = self.check_name_method(name_method)
        email = self.check_email_method(email_method)
        password = self.check_password_method(password_method)

        """Filling the following fields with values from the top of this function."""
        self.first_name_field.send_keys(first_name)
        self.last_name_field.send_keys(last_name)
        self.email_field.send_keys(email)
        self.new_password_field.send_keys(password)

        """If checkbox is True - we check it and click sign up button, else - we just click 'Sign up' button"""
        if checkbox_method:
            self.terms_checkbox.click()
            self.sign_up_btn.click()
        else:
            self.sign_up_btn.click()

    """Trying to sign up with all valid data and with checking term checkbox."""
    def valid_values_reg(self):
        email_method = 'valid'
        password_method = 'valid'
        name_method = 'normal_name'
        checkbox_method = True
        test_name = "Registration with valid values."
        self.registration(name_method, email_method, password_method, checkbox_method)
        return self.check_exists_by_xpath(test_name, "//input[@type='search']")

    """Trying to sign up with all valid data except email."""
    def invalid_email_reg(self):
        email_method = 'invalid'
        password_method = 'valid'
        name_method = 'normal_name'
        checkbox_method = True
        test_name = "Registration with invalid email."
        self.registration(name_method, email_method, password_method, checkbox_method)
        return self.check_exists_by_xpath(test_name, "//li[contains(text(),'Email is invalid')]")

    """Trying to sign up with all valid data, but with empty email field."""
    def empty_email_reg(self):
        email_method = 'empty'
        password_method = 'valid'
        name_method = 'normal_name'
        checkbox_method = True
        test_name = "Registration with empty email."
        self.registration(name_method, email_method, password_method, checkbox_method)
        return self.check_exists_by_xpath(test_name,
                                          "//li[contains(text(),'Email can') and contains(text(),'t be blank')]")

    """Trying to sign up an account which already has been registred."""
    def already_registered_email_reg(self):
        email_method = "registered"
        password_method = 'valid'
        name_method = 'normal_name'
        checkbox_method = True
        test_name = "Registration with already registered email."
        self.registration(name_method, email_method, password_method, checkbox_method)
        return self.check_exists_by_xpath(test_name, "//li[@role='alert' and contains(text(),'Email has already been taken')]")

    """Trying to sign up with all valid data, but checkbox is not checked."""
    def no_checkbox_reg(self):
        email_method = 'valid'
        password_method = 'valid'
        name_method = 'normal_name'
        checkbox_method = False
        test_name = "Registration with valid values without checkbox."
        self.registration(name_method, email_method, password_method, checkbox_method)
        return self.check_exists_by_xpath(test_name, "//li[@role='alert' and contains(text(), 'Terms')]")

    """Trying to sign up with all valid data, but with empty 'password' field."""
    def empty_password_reg(self):
        email_method = 'valid'
        password_method = 'empty'
        name_method = 'normal_name'
        checkbox_method = True
        test_name = "Registration with empty password."
        self.registration(name_method, email_method, password_method, checkbox_method)
        return self.check_exists_by_xpath(
            test_name, "//li[@role='alert' and contains(text(),'Password can') and contains(text(),'t be blank')]")

    """Trying to sign up with too short password, which less than 6 symblos. This count
                                            could be changed in the 'Random_generator', def too_short_name)."""
    def too_short_password_reg(self):
        email_method = 'valid'
        password_method = 'too_short'
        name_method = 'normal_name'
        checkbox_method = True
        test_name = "Registration with too short password (less than 6 symbols)."
        self.registration(name_method, email_method, password_method, checkbox_method)
        return self.check_exists_by_xpath(
            test_name, "//li[@role='alert' and contains(text(),'Password must be at least')]")

    """Trying to sign up with too long password, which longer than 128 symbols. This count
                                            could be changed in the 'Random_generator', def too_long_password)."""
    def too_long_password_reg(self):
        email_method = 'valid'
        password_method = 'too_long'
        name_method = 'normal_name'
        checkbox_method = True
        test_name = "Registration with too long password (longer than 128 symbols)."
        self.registration(name_method, email_method, password_method, checkbox_method)
        return self.check_exists_by_xpath(
            test_name, "//li[@role='alert' and contains(text(),'Password cannot be longer than')]")

    """Trying to sign up with too long name and last name, more than 255+ symbols, this count
                                            could be changed in the 'Random_generator', def too_long_name)."""

    def too_long_name_reg(self):
        name_method = 'too_long'
        test_name = "Registration with too long name and last name (more than 255 symbols)."
        self.check_name_method(name_method)
        try:
            result1 = driver.find_element(By.XPATH, "//li[@role='alert' and contains(text(),'First name is too long')]")
            result2 = driver.find_element(By.XPATH, "//li[@role='alert' and contains(text(),'Last name is too long')]")
            if result1 and result2:
                return self.check_exists_by_xpath(test_name, result1)
        except:
            return f"Test: {test_name}.\nStatus: Failed"

    """Trying to sign up with empty 'name' and 'last name' fields"""

    def empty_name_reg(self):
        name_method = 'empty'
        test_name = "Registration with empty name and last name."
        self.check_name_method(name_method)
        try:
            result1 = driver.find_element(
                By.XPATH, "//li[contains(text(),'First name can') and contains(text(),'t be blank')]")
            result2 = driver.find_element(
                By.XPATH, "//li[contains(text(),'Last name can') and contains(text(),'t be blank')]")
            if result1 and result2:
                return self.check_exists_by_xpath(test_name, result1)
        except:
            return f"Test: {test_name}.\nStatus: Failed"


def manual():
    while True:
        answer = input("""
Enter one of the following scripts:
[1] - All valid values
[2] - All valid data, but email is invalid.
[3] - All valid data, but email is empty.
[4] - All valid data, but email has been already registred.
[5] - All valid data, but checkbox wouldn't be checked.
[6] - All valid data, but password will be empty.
[7] - All valid data, but too short password (shorter than 6 symbols).
[8] - All valid data, but too long password (longer than 255 symbols).
[9] - All valid data, but too long name and last name (more than 255 symbols).
[10] - All valid data, but name and last name field will be empty.

[b] - Back to main menu.
[q] - Stop the test.
""")

        if answer == '1':
            print(SignUpPage(driver).valid_values_reg())
        elif answer == '2':
            print(SignUpPage(driver).invalid_email_reg())
        elif answer == '3':
            print(SignUpPage(driver).empty_email_reg())
        elif answer == '4':
            print(SignUpPage(driver).already_registered_email_reg())
        elif answer == '5':
            print(SignUpPage(driver).no_checkbox_reg())
        elif answer == '6':
            print(SignUpPage(driver).empty_password_reg())
        elif answer == '7':
            print(SignUpPage(driver).too_short_password_reg())
        elif answer == '8':
            print(SignUpPage(driver).too_long_password_reg())
        elif answer == '9':
            print(SignUpPage(driver).too_long_name_reg())
        elif answer == '10':
            print(SignUpPage(driver).empty_name_reg())
        elif answer == 'q':
            print("Stopping the program...")
            return answer
        elif answer == 'b':
            break
        else:
            print('Invalid command...')
def auto():
    valid_values_reg = SignUpPage(driver).valid_values_reg()
    invalid_email_reg = SignUpPage(driver).invalid_email_reg()
    empty_email_reg = SignUpPage(driver).empty_email_reg()
    already_registered_email_reg = SignUpPage(driver).already_registered_email_reg()
    no_checkbox_reg = SignUpPage(driver).no_checkbox_reg()
    empty_password_reg = SignUpPage(driver).empty_password_reg()
    too_short_password_reg = SignUpPage(driver).too_short_password_reg()
    too_long_password_reg = SignUpPage(driver).too_long_password_reg()
    too_long_name_reg = SignUpPage(driver).too_long_name_reg()
    empty_name_reg = SignUpPage(driver).empty_name_reg()

    print(f"""
{valid_values_reg}\n
{invalid_email_reg}\n
{empty_email_reg}\n
{already_registered_email_reg}\n
{no_checkbox_reg}\n
{empty_password_reg}\n
{too_short_password_reg}\n
{too_long_password_reg}\n
{too_long_name_reg}\n
{empty_name_reg}
    """)


"""If started as main script - it will start all tests from the Sign_up_page class. After ending all tests
                                it will show results of each test (passed or failed)."""
if __name__ == "__main__":
    answer = ''
    while answer != 'q':
        print("Enter type of test you want to do: ")
        answer = input("Type 'a' to run all tests, type 'm' to run it one by one or 'q' to quit:\n")
        if answer == 'a':
            auto()
            continue
        elif answer == 'm':
            answer = manual()
        elif answer == 'q':
            driver.quit()
            break
        else:
            print('Invalid command...')
driver.quit()
