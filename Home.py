from time import sleep
from selenium import webdriver
from selenium import common
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome
browser = webdriver.Chrome(executable_path="D:\chromedriver.exe")

"""To Login To your instagram page"""

browser.get('https://www.instagram.com/')
sleep(5)
username = browser.find_element_by_name("username")
username.send_keys("vijayjeyakumar0007@gmail.com")
sleep(1)
password = browser.find_element_by_name("password")
password.send_keys("GIVE YOUR PASSWORD ")
sleep(1)
login = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
login.click()
sleep(3)
browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
sleep(5)
browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

"""To Search Tag or celebrity """

browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys("SunnyLeone")
sleep(3)
browser.find_element_by_xpath(
    "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div").click()
sleep(3)

"""To Store Current page"""

browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").click()
sleep(2)
parent = browser.window_handle()
print("Parent", parent)


"""TO FOLLOW AND UNFOLLOW USER IN INSTAGRAM """
"""PROVIDE THE USERNAME YOU WANT TO FOLLOW AS THE PARAMETER"""


def Insta_Methods():
    user = "Vijay Potter"
    follow_user(user)
    unfollow_user(user)


"""Navigates to the user page and clicks follow button"""


def follow_user(self, user):
    """Searches for the user in search bar [Navigation] """
    browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(user)
    sleep(3)
    browser.find_element_by_xpath(
        "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div").click()
    sleep(3)

    follow_buttons = self.find_buttons('Follow')
    sleep(2)

    for btn in follow_buttons:
        btn.click()


"""Navigates to the user page and clicks Unfollow button"""


def unfollow_user(self, user):
    """Searches for the user in search bar [Navigation] """
    browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(user)
    sleep(3)
    browser.find_element_by_xpath(
        "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div").click()
    sleep(3)
    unfollow_btns = self.find_buttons('Following')

    if unfollow_btns:
        for btn in unfollow_btns:
            btn.click()
            unfollow_confirmation = self.find_buttons('Unfollow')[0]
            unfollow_confirmation.click()
    else:
        print('No {} buttons were found.'.format('Following'))


browser.close()
