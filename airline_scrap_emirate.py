from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import DriverManager

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.driver = webdriver.Edge(DriverManager().install())

    def runbot(self):
        self.driver.get('https://www.emirates.com/th/english')

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
        # robot_checker=self.driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]')
        # if robot_checker!=None:
        #         robot_checker.click()

        # #change Lang to EN
        # lang_btn =self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/header/div/div[1]/nav/ul/li[2]/button')
        
        # lang_btn.click()

        # lang_btn2=self.driver.find_element_by_xpath('//*[@id="culture-selector-switch-to-english"]')
        # lang_btn2.click()

        # dest=self.driver.find_element_by_xpath('//*[@id="59cdbbf0-d4e9-4b6b-8fbd-47949ba14f29"]')
        # # //*[@id="59cdbbf0-d4e9-4b6b-8fbd-47949ba14f29"]
        # dest.click()
        # dest.send_keys("LHR")

        # searchbutton=self.driver.find_element_by_xpath('//*[@id="panel0"]/div/div/div/section/div[4]/div[1]/div[4]/a/span')
        # searchbutton.click()

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

        location_button=self.driver.find_element_by_xpath('//*[@id="panel0"]/div/div/div/section/div[4]/div[1]/div[1]/div/div[2]/div/div/div[1]/div/label')
        location_button.click()

        location_box=self.driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div[1]/div/div/div/section/div[4]/div[1]/div[1]/div/div[2]/div/div/div[1]/div/input')
        location_box2=self.driver.find_element_by_name('Arrival airport')
        if location_box2 !=None:
            location_box2.send_keys('LHR')
            location_box2.send_keys(Keys.TAB)
            # location_box2.send_keys(Keys.TAB)
            # location_box2.send_keys(Keys.SPACE)

            # date1=self.driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div[1]/div/div/div/section/div[4]/div[1]/div[3]/eol-datefield/div[1]/div[1]/input')
            # date1.click()
            # date1.send_keys(Keys.TAB)
            # #//*[@id="search-flight-date-picker--depart"]

            
            #one_way_btn=self.driver.find_element_by_xpath('//*[@id="panel0"]/div/div/div/section/div[4]/div[1]/div[3]/eol-datefield/eol-calendar/div/div/div[1]/div/label[2]')
            one_way_btn=self.driver.find_element_by_xpath('//*[@id="panel0"]/div/div/div/section/div[4]/div[1]/div[3]/eol-datefield/eol-calendar/div/div/div[1]/div/label[2]/input')
            #one_way_btn.click()
            self.driver.execute_script("arguments[0].click();",one_way_btn)
            

            #cal_selector=self.driver.find_elements_by_xpath('//*[@id="panel0"]/div/div/div/section/div[4]/div[1]/div[3]/eol-datefield/eol-calendar/div/div/div[2]')
            cal_selector=self.driver.find_element_by_xpath('//*[@id="panel0"]/div/div/div/section/div[4]/div[1]/div[3]/eol-datefield/eol-calendar/div/div/div[2]/table')
           
            rows = cal_selector.find_elements_by_tag_name('tr')
            columns = cal_selector.find_elements_by_tag_name('td')
            
            for cell in columns:
                # if cell=='10':
                #     cell.find_element_by_link_text('10').click()
                # break
                cell2=cell.find_elements_by_tag_name('a')
                for cell_detail in cell2:
                    #a_link=cell_detail.find_element_by_link_text('10')
                    if cell_detail.get_attribute('innerHTML') =='11':
                        cell_detail.click()

                    # if a_link!=None:
                    #     #a_link.click()
                    #     print(a_link)
            
            #default search is economy class

            #find search button
            btn_search=self.driver.find_element_by_xpath('//*[@id="panel0"]/div/div/div/section/div[4]/div[2]/div[3]/form/button')
            btn_search.click()

            btn_search2=self.driver.find_element_by_xpath('//*[@id="ctl00_c_IBE_PB_FF"]')
            btn_search2.click()
            
            #flight table body
            flight_table=self.driver.find_elements_by_xpath('//*[@id="ctl00_c_dvOBBResult"]/div[3]')
            





        
bot=Bot()
bot.runbot()