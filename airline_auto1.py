from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import DriverManager

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.driver = webdriver.Edge(DriverManager().install())

    def runbot(self):
        self.driver.get('https://www.skyscanner.co.th/')

        #self.driver.fullscreen_window()
        #self.driver.implicitly_wait(30)

        # lang_screen=self.driver.find_element_by_xpath('//*[@id="modal"]/div[1]/div[1]/div')
        
        
        # if lang_screen !=None:
        #     lang_button=self.driver.find_element_by_xpath('//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[1]/button')
        #     lang_button.click()

        # welcome_screen = self.driver.find_element_by_xpath('//*[@id="modal"]/div/div/div[2]/a/img')
        
        # if welcome_screen != None:
        #     welcome_close_button=self.driver.find_element_by_xpath('//*[@id="modal"]/div/div/div[2]/div')
        #     welcome_screen.click()
        #     self.driver.get('https://shopee.co.th/')

        #robot check bypass
        robot_checker=self.driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]')
        if robot_checker!=None:
                robot_checker.click()

        #change Lang to EN
        lang_btn =self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/header/div/div[1]/nav/ul/li[2]/button')
        
        lang_btn.click()

        lang_btn2=self.driver.find_element_by_xpath('//*[@id="culture-selector-switch-to-english"]')
        lang_btn2.click()

        dest=self.driver.find_element_by_xpath('//*[@id="59cdbbf0-d4e9-4b6b-8fbd-47949ba14f29"]')
        # //*[@id="59cdbbf0-d4e9-4b6b-8fbd-47949ba14f29"]
        dest.click()
        dest.send_keys("LHR")

        searchbutton=self.driver.find_element_by_xpath('//*[@id="panel0"]/div/div/div/section/div[4]/div[1]/div[4]/a/span')
        searchbutton.click()

        # usr = self.driver.find_element_by_xpath('//*[@id="modal"]/aside/div[1]/div/div/div/div[2]/div[1]/div[2]/div/input')
        # #usr = self.driver.find_element_by_xpath('//*[@id="modal"]/aside/div[1]/div/div/div/div[2]/div[1]/div[4]/a')


        # #usr=self.driver.find_element(by=id,value="loginKey")
        # usr.click()
        # usr.send_keys("xxx")

        # pss = self.driver.find_element_by_xpath('//*[@id="modal"]/aside/div[1]/div/div/div/div[2]/div[1]/div[3]/div/input')
        
        # pss.click()
        # pss.send_keys("xxx")

        # submitbutton = self.driver.find_element_by_xpath('//*[@id="modal"]/aside/div[1]/div/div/div/div[2]/div[2]/button[2]')
        # submitbutton.click()
        
bot=Bot()
bot.runbot()