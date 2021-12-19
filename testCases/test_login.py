import pytest

from pageObjects.LoginPage import PageLogin
from utilities.readProperties import ReadConnfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseurl = ReadConnfig.getApplicationURL()
    username = ReadConnfig.getUsername()
    password = ReadConnfig.getPasswoed()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("Test_001_Login")
        self.logger.info("Verifying Home Page Title")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("Verifying Home Page Title Test Passed")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("Verifying Home Page Title Test Failed")
            assert False

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("Verifying  Test Login")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = PageLogin(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPasssword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("Verifying  Test Login passed")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("Verifying  Test Login failed")
            assert False
