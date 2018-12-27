# Hatch
Hatch is a brute force tool that is used to brute force most websites

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
[![IMAGE ALT TEXT](https://i.ytimg.com/vi/Hd_kQVnajxk/1.jpg)](https://youtu.be/Hd_kQVnajxk "Video Title")

