from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
VP_WEB = ""
VP_ACC = ""
VP_PW = ""
FK_WEB = ""
FK_ACC = ""
FK_PW = ""
O_WEB = ""
O_ACC = ""
O_PW = ""
XG_WEB = ""
XG_ACC = ""
XG_PW = ""
RM_WEB = ""
RM_ACC = ""
RM_PW = ""

PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)
action = ActionChains(driver)


def login(account, password, letter):
    if letter in 'for':
        acc_name = driver.find_element_by_id("txtLoginName")
        pw = driver.find_element_by_id("txtLoginPass")
        acc_name.send_keys(account)
        pw.send_keys(password)
        if letter in 'fo':
            unique_code = input("What's the unique code: ")
            code = driver.find_element_by_id("txtVerifyCode")
            code.send_keys(unique_code)
            sleep(1)
        else:
            sleep(1)
        signin = driver.find_element_by_id("btnLogin")
        signin.send_keys(Keys.ENTER)
        sleep(1)
    elif letter == 'v':
        acc_name = driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div[1]/input')
        pw = driver.find_element_by_xpath('//*[@id="app"]/div/div/form/div[2]/div/div[1]/input')
        acc_name.send_keys(account)
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)
        sleep(1)
    elif letter == 'x':
        acc_name = driver.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div/div[1]/input')
        pw = driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div[1]/input')
        acc_name.send_keys(account)
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)
        sleep(1)


def load(letter):
    if letter in 'for':
        driver.switch_to.frame("frm_main_content")
        try:
            username, payment = input("Enter the username and recharge amount: ").split()
        except ValueError:
            print("Sorry, that was an invalid entry")
            username, payment = input("Enter the username and recharge amount: ").split()
        sleep(1)
        if letter in "fo":
            load_account = driver.find_element_by_id("txtSearch")
            load_account.send_keys(username)
            load_account.send_keys(Keys.ENTER)
            sleep(1)
            if username.lower() == 'dianalouise':
                recharge = driver.find_element_by_xpath('//*[@id="list"]/tbody/tr[3]/td[2]/a')
                action.click(recharge).perform()
            else:
                recharge = driver.find_element_by_link_text("Recharge")
                recharge.click()
            sleep(1)
        elif letter == 'r':
            load_account = driver.find_element_by_id("txtSearch")
            load_account.send_keys(username)
            search = driver.find_element_by_id("btnQuery")
            search.click()
            sleep(1)
            if username.lower() == 'bigdaddy3':
                recharge = driver.find_element_by_xpath('//*[@id="list"]/tbody/tr[3]/td[2]/a')
                action.click(recharge).perform()
            else:
                recharge = driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr[2]/td[2]/a")
                recharge.click()
            sleep(1)
        recharge_amount = driver.find_element_by_id("txtAddGold")
        recharge_amount.send_keys(payment)
        sleep(1)
        confirm = driver.find_element_by_id("btnSave1")
        confirm.click()
        print(f"{username}'s payment of {payment} has been loaded.")
        sleep(1)
        return_to_main_page = driver.find_element_by_xpath("/html/body/form/span/a[2]")
        return_to_main_page.click()


def load_FK(log):
    """To login into website"""
    driver.get(FK_WEB)
    if not log:
        login(FK_ACC, FK_PW, 'f')
    else:
        load('f')


def load_O(log):
    driver.get(O_WEB)
    if not log:
        login(O_ACC, O_PW, 'o')
    else:
        load('o')


def load_R(log):
    driver.get(RM_WEB)
    if not log:
        login(RM_ACC, RM_PW, 'r')
    else:
        load('r')


def load_VP(log):
    driver.get(VP_WEB)
    wait = WebDriverWait(driver, 10)

    if not log:
        login(VP_ACC, VP_PW, 'v')
    else:
        sleep(2)
        body = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body")))
        menu = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "hamburger")))
        menu.click()
        search_icon = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "el-input__inner")))
        search_icon.send_keys(Keys.ENTER)
        try:
            username, payment = input("Enter the username and recharge amount: ").split()
        except ValueError:
            print("Sorry, that was an invalid entry")
            username, payment = input("Enter the username and recharge amount: ").split()
        sleep(2)

        load_attempts = 0
        while load_attempts < 2:
            try:
                player_account = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div["
                                                              "1]/form/div[1]/div/div/label[2]/span[1]/span")
                search_account = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section'
                                                              '/div/div[1]/form/div[2]/div/div/div[1]/div/input')
                player_account.click()
                search_account.click()
                search_account.send_keys(username)
                search_account.send_keys(Keys.ENTER)
                sleep(1)
                set_score = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div['
                                                         '4]/div/div/div/div/div[3]/table/tbody/tr/td[14]/div/button['
                                                         '1]/span')
                set_score.click()
                sleep(1)
                enter_points = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div['
                                                            '4]/div/form/div[3]/div/div[1]/input')
                enter_points.send_keys(payment)
                confirm = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/form/div['
                                                       '5]/div/button[1]/span')
                confirm.click()
                print(f"{username}'s payment of {payment} has been loaded.")
                search_account.clear()
                sleep(3)
                body.click()
                driver.get(VP_WEB)
                sleep(1)
                break
            except StaleElementReferenceException or NoSuchElementException:
                pass
            load_attempts += 1


def load_XG(log):
    driver.get(XG_WEB)
    wait = WebDriverWait(driver, 10)

    if not log:
        login(XG_ACC, XG_PW, 'x')
    else:
        sleep(2)
        body = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body")))
        menu = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "hamburger")))
        menu.click()
        search_icon = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "el-input__inner")))
        search_icon.send_keys(Keys.ENTER)
        try:
            username, payment = input("Enter the username and recharge amount: ").split()
        except ValueError:
            print("Sorry, that was an invalid entry")
            username, payment = input("Enter the username and recharge amount: ").split()
        sleep(2)

        load_attempts = 0
        while load_attempts < 2:
            try:
                player_account = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div["
                                                              "1]/form/div[1]/div/div/label[2]/span[1]/span")
                search_account = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section'
                                                              '/div/div[1]/form/div[2]/div/div/div[1]/div/input')
                player_account.click()
                search_account.click()
                search_account.send_keys(username)
                search_account.send_keys(Keys.ENTER)
                sleep(1)
                set_score = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div['
                                                         '4]/div/div/div/div/div[3]/table/tbody/tr/td[14]/div/button['
                                                         '1]/span')
                set_score.click()
                sleep(1)
                enter_points = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div['
                                                            '4]/div/form/div[3]/div/div[1]/input')
                enter_points.send_keys(payment)
                confirm = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/form/div['
                                                       '5]/div/button[1]/span')
                confirm.click()
                print(f"{username}'s payment of {payment} has been loaded.")
                search_account.clear()
                sleep(3)
                body.click()
                driver.get(XG_WEB)
                sleep(1)
                break
            except StaleElementReferenceException or NoSuchElementException:
                pass
            load_attempts += 1
