from time import sleep
import sys
from selenium import webdriver

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome() 

    def logIn(self, logInType):
        self.driver.get("https://tinder.com")
        sleep(10) # based on your internet speed
        
        if logInType == 'fb':
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
            fb_btn.click()
            #switching window
            base_window, popUp_window =  self.driver.window_handles
            self.driver.switch_to_window(popUp_window)
            email_in = self.driver.find_element_by_xpath('/b/*[@id="email"]')
            email_in.send_keys('pankaj.dbz.teen@gmail.com')

            password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
            password_in.send_keys('password here')

            login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
            login_btn.click()

            #switch back to base window
            self.driver.switch_to_window(base_window)

        else:
            phone_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[1]/button')
            phone_btn.click()
            phone_number = input("Enter your phone number: ")
            phone_number_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
            phone_number_in.send_keys(phone_number)
            
            continue_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
            continue_btn.click()
            
            sleep(2)
            otp = input("Enter OTP: ")
            otp_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[1]')
            otp_in.send_keys(otp)
            
            # otp_in = ['//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[1]',
            # '//*[@id="modal-manager"]/div/div/div[2]/div[3]/inpopiv[2]/div[3]/input[4]',
            # '//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[5]',
            # '//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[6]']

            continue_btn_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
            continue_btn_2.click()

        sleep(5)
        popup_1= self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        sleep(5)
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        like = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like.click()

    def disLike(self):
        unlike = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        unlike.click()

    def closePopup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def freeSwipeOver(self):
        popup_4 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        popup_4.click()
    
    def closeMatch(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()
        exit()
    
    def autoSwipe(self):
        while True:
            sleep(1)
            try:
                self.like()
            except Exception:
                try:
                    self.closePopup()
                except Exception:
                    try:
                        self.freeSwipeOver()
                    except Exception:
                        self.closeMatch()


bot = TinderBot()
logInType = sys.argv[1] if len(sys.argv)>1 else "phone"
bot.logIn(logInType)
bot.autoSwipe()