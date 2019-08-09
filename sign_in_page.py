from selenium.webdriver.common.by import By
from config import driver


class SignInPage:
    def __init__(self, driver):
        driver.get("https://courses.ultimateqa.com/users/sign_in")
        self.driver = driver
        self.email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        self.password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        self.sign_in_btn = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Sign in']")
        self.new_acc_btn = driver.find_element(By.XPATH, "//a[contains(@href,'sign_up')]")
        self.forgot_password_btn = driver.find_element(By.XPATH, "//a[contains(@href,'password/new')]")


    def check_exists_by_xpath(self, test_name, xpath):
        try:
            assert driver.find_element(By.XPATH, xpath)
            return f"Test: {test_name}.\nStatus: Passed"
        except:
            return f"Test: {test_name}.\nStatus: Failed"

    def login(self, email, password, test_name, method):
        self.email_field.send_keys(email)
        self.password_field.send_keys(password)
        self.sign_in_btn.click()
        return self.login_result(method, test_name)

    def check_valid_values(self):
        email = "test3@gmail.com"
        password = "123456"
        test_name = "Check login with valid values."
        return self.login(email, password, test_name, 'valid_values')

    def check_invalid_email(self):
        invalid_email = "testL@gmail.com"
        password = "testpassword1"
        test_name = "Check login with invalid email."
        return self.login(invalid_email, password, test_name, 'invalid_email')

    def check_invalid_password(self):
        email = "test1@gmail.com"
        invalid_password = "testpassword2"
        test_name = "Check login with invalid password."
        return self.login(email, invalid_password, test_name, 'invalid_password')

    def check_new_acc_btn(self):
        test_name = "Check 'Create a new account' link for exists and its working."
        self.new_acc_btn.click()
        return self.check_exists_by_xpath(test_name, "//h1[contains(text(),'Create a new account')]")

    def check_forgot_password_btn(self):
        test_name = "Check 'Forgot Password?' link for exists and its working."
        self.forgot_password_btn.click()
        return self.check_exists_by_xpath(test_name, "//h1[contains(text(),'Forgot your Password?')]")

    def login_result(self, method, test_name):
        if method == 'valid_values':
            return self.check_exists_by_xpath(test_name, "//div[@data-message='Signed in successfully.']")

        elif method == 'invalid_email':
            return self.check_exists_by_xpath(test_name, "//li[@role='alert' and text()='Invalid Email or password.']")

        elif method == 'invalid_password':
            return self.check_exists_by_xpath(test_name, "//li[@role='alert' and text()='Invalid Email or password.']")


def manual():
    while True:
        answer = input("""
Enter one of the following scripts:
[1] - Test with all valid values.
[2] - Test with invalid email.
[3] - Test with invalid password.
[4] - Test Check 'Create a new account' link for exists and its working
[5] - Test 'Forgot Password?' link for exists and its working

[b] - Back to main menu.
[q] - Stop the test.
""")
        if answer == '1':
            print(SignInPage(driver).check_valid_values())
        elif answer == '2':
            print(SignInPage(driver).check_invalid_email())
        elif answer == '3':
            print(SignInPage(driver).check_invalid_password())
        elif answer == '4':
            print(SignInPage(driver).check_new_acc_btn())
        elif answer == '5':
            print(SignInPage(driver).check_forgot_password_btn())
        elif answer == 'q':
            print("Stopping the program...")
            return answer
        elif answer == 'b':
            break
        else:
            print('Invalid command...')


def auto():
    check_valid_values = SignInPage(driver).check_valid_values()
    check_invalid_email = SignInPage(driver).check_invalid_email()
    check_invalid_password = SignInPage(driver).check_invalid_password()
    check_new_acc_btn = SignInPage(driver).check_new_acc_btn()
    check_forgot_password_btn = SignInPage(driver).check_forgot_password_btn()

    print(f"""
{check_valid_values}\n
{check_invalid_email}\n
{check_invalid_password}\n
{check_new_acc_btn}\n
{check_forgot_password_btn}
    """)


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
