# Hatch
Hatch is a brute force tool that is used to brute force most websites

# Update! recoed by FlroianBord2
You can run Hatch with python3 now.
The main pupose of this fork is to improve number of password tested by second.
The orginal code call a two second scleep between each try, i replace this by the wait until presence of element located.
time.sleep(2) -> wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, login_btn_selector)))
The procces is two time faster with this modification.

# Update! v.1.3
added arg support **yay**
<br>
  -h, --help            show this help message and exit<br>
  -u USERNAME, --username=USERNAME Choose the username<br>
  --usernamesel=USERNAMESEL Choose the username selector<br>
  --passsel=PASSSEL     Choose the password selector<br>
  --loginsel=LOGINSEL   Choose the login button selector<br>
  --passlist=PASSLIST   Enter the password list directory<br>
  --website=WEBSITE     choose a website<br>
dont worry if you load up the tool without any args youll go to the default wizard!
Also i removed the apt xvfb and pip2 pyvirtualdisplay
## Installation Instructions
```
git clone https://github.com/MetaChar/Hatch
python2 main.py
```

## Requirements
```
pip2 install selenium
pip2 install requests
```
chrome driver and chrome are also required!
link to chrome driver: http://chromedriver.chromium.org/downloads
copy it to bin!
<br>
## How to use (text)
1). Find a website with a login page<br>
2). Inspect element to find the Selector of the username form<br>
3). Do the same for the password field<br>
4). The the login form <br>
5). When Asked put in the username to brute force<br>
6). Watch it go!

## How to use (Video)
[![IMAGE ALT TEXT](https://i.ytimg.com/vi/Hd_kQVnajxk/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLC7N67-Q67WAxMViUrHWJDdnkSM9A)](https://youtu.be/Hd_kQVnajxk "Video Title")

