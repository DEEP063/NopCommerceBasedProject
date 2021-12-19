

class PageLogin:
        textbox_email_class = "email"
        textbox_password_id = "Password"
        login_button_class ="login-button"
        logout_button_xpath= '//*[@id="navbarText"]/ul/li[3]/a'

        def __init__(self, driver):
            self.driver = driver

        def setUserName(self, username):
            self.driver.find_element_by_class_name(self.textbox_email_class).clear()
            self.driver.find_element_by_class_name(self.textbox_email_class).send_keys(username)

        def setPasssword(self, password):
            self.driver.find_element_by_id(self.textbox_password_id).clear()
            self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

        def clickLogin(self):
            self.driver.find_element_by_class_name(self.login_button_class).click()

        def clickLogout(self):
            self.driver.find_element_by_xpath(self.logout_button_xpath).click()


