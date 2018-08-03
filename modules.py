import subprocess, time

def MEDIAID():
    global urlfoto
    global mediaID
    urlfoto = raw_input("[+]Url foto: ")
    url = ("https://api.instagram.com/oembed/?url="+urlfoto)
    subprocess.Popen(['xdg-open', url])
    time.sleep(10)

def USERID():
    global username
    global url
    username = raw_input("[+]Username of the enemy XD: ")
    url = "https://www.instagram.com/"+username+"?__a=1"
    subprocess.Popen(['xdg-open', url])
    time.sleep(10)
