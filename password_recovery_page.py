from selenium.webdriver.common.by import By
from config import driver


class PasswordRecoveryPage:
    def __init__(self, driver):
        driver.get("https://courses.ultimateqa.com/users/password/new")
        self.email_field = driver.find_element(By.XPATH, "//input[@type='email' and @placeholder='Email']")
        self.submit_btn = driver.find_element(By.XPATH, "//input[@type='submit']")

    def email_recovery(self):
        email = input("Enter the email you want to recovery: ")
        self.email_field.send_keys(email)
        self.submit_btn.click()
        test_name = "Email recovering."
        try:
            driver.find_element(By.XPATH, "//h1[contains(text(),'Help is on the way')]")
            print(
                f"Test: {test_name}\nStatus: Passed.\nTo fully pass this test you should to check your email: {email}")
        except:
            print(f"Test: {test_name}\nStatus: Failed")


if __name__ == '__main__':
    PasswordRecoveryPage(driver).email_recovery()
driver.quit()
