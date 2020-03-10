from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import DriverManager

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.driver = webdriver.Edge(DriverManager().install())

    def runbot(self):
        self.driver.get('https://shopee.co.th/')

        #self.driver.fullscreen_window()
        self.driver.implicitly_wait(30)

        lang_screen=self.driver.find_element_by_xpath('//*[@id="modal"]/div[1]/div[1]/div')
        
        if lang_screen !=None:
            lang_button=self.driver.find_element_by_xpath('//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[1]/button')
            lang_button.click()

        welcome_screen = self.driver.find_element_by_xpath('//*[@id="modal"]/div/div/div[2]/a/img')
        
        if welcome_screen != None:
            welcome_close_button=self.driver.find_element_by_xpath('//*[@id="modal"]/div/div/div[2]/div')
            welcome_screen.click()
            self.driver.get('https://shopee.co.th/')

        login=self.driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/div/div[1]/div/ul/li[5]')
        #login=self.driver.find_element_by_css_selector('navbar__link navbar__link--account navbar__link--tappable navbar__link--hoverable navbar__link-text navbar__link-text--medium')
        login.click()

        usr = self.driver.find_element_by_xpath('//*[@id="modal"]/aside/div[1]/div/div/div/div[2]/div[1]/div[2]/div/input')
        #usr = self.driver.find_element_by_xpath('//*[@id="modal"]/aside/div[1]/div/div/div/div[2]/div[1]/div[4]/a')


        #usr=self.driver.find_element(by=id,value="loginKey")
        usr.click()
        usr.send_keys("xxx")

        pss = self.driver.find_element_by_xpath('//*[@id="modal"]/aside/div[1]/div/div/div/div[2]/div[1]/div[3]/div/input')
        
        pss.click()
        pss.send_keys("xxx")

        submitbutton = self.driver.find_element_by_xpath('//*[@id="modal"]/aside/div[1]/div/div/div/div[2]/div[2]/button[2]')
        submitbutton.click()
        
bot=Bot()
bot.runbot()