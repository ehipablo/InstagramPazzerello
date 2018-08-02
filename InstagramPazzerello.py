#tested on python 2.7.15

__author__ = 'ehipablo'
from InstagramAPI import InstagramAPI
import time, requests, subprocess

#INSTALL MODULE InstagramAPI: "python -m pip install -e git+https://github.com/LevPasha/Instagram-API-python.git#egg=InstagramAPI"

print " __               __ "
print "|__|.-----.-----.|  |_.---.-.-----.----.---.-.--------."
print '|  ||     |__ --||   _|  _  |  _  |   _|  _  |        | '
print '|__||__|__|_____||____|___._|___  |__| |___._|__|__|__| '
print '                            |_____|        __ __   '
print '.-----.---.-.-----.-----.-----.----.-----.|  |  |.-----.'
print '|  _  |  _  |-- __|-- __|  -__|   _|  -__||  |  ||  _  |'
print '|   __|___._|_____|_____|_____|__| |_____||__|__||_____|'
print '|__| '
print ""
print "Per veri rompi coglioni ;)"
print ""

username = raw_input("[+]Your Username: ")
password = raw_input("[+]Your Password: ")

InstagramAPI = InstagramAPI(username, password)
InstagramAPI.login()

key = input("[+]1)Comment spam 2)FollowUnfollow: ")

#COMMENT SPAM
if key == 1:
    text = raw_input("[+]Comment: ")
    urlfoto = raw_input("[+]Url foto: ")
    url = ("https://api.instagram.com/oembed/?url="+urlfoto)
    subprocess.Popen(['xdg-open', url])
    mediaID = raw_input("[+]media id: ")
    print ""
    continue1 = raw_input("[+]Do you wanna continue?[Y/N]: ")

    if continue1 == "Y":
        while True:
            for x in range(3):
                InstagramAPI.comment(mediaID, text)
            time.sleep(50)
        print "ok"
    else:
        exit()

#FOLLOWUNFOLLOW
elif key == 2:
    username = raw_input("[+]Username to follow: ")
    url = "https://www.instagram.com/"+username+"?__a=1"
    subprocess.Popen(['xdg-open', url])
    userID = raw_input("[+]userID: ")
    while True:
        InstagramAPI.follow(userID)
        time.sleep(3)
        InstagramAPI.unfollow(userID)
        time.sleep(1)
else:
    exit()
