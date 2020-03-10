from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())


class Music():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def play(self):
        name=input("enter your youtube!")
        self.driver.get('https://www.youtube.com/user/Nintendo/videos')

        new = self.driver.find_element_by_xpath('//*[@id="items"]/ytd-grid-video-renderer[3]')
        new.click()

bot=Music()
bot.play()

