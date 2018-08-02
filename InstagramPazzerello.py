__author__ = 'ehipablo'
from InstagramAPI import InstagramAPI
import time
from modules import *

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
print "Script per veri rompi coglioni ;)"
print ""

username = raw_input("[+]Your Username: ")
password = raw_input("[+]Your Password: ")

InstagramAPI = InstagramAPI(username, password)
InstagramAPI.login()

key = input("[+]1)Comment spam | 2)FollowUnfollow | 3)LikeUnlike: 4)Direct Spam: ")

#COMMENT-SPAM PART
if key == 1:
    MEDIAID()
    print ""
    text = raw_input("[+]text: ")
    mediaID = raw_input("[+]media id: ")
    continue1 = raw_input("[+]Do you wanna continue?[Y/N]: ")
    if continue1 == "Y":
        while True:
            for x in range(3):
                InstagramAPI.comment(mediaID, text)
            time.sleep(50)
        print "ok"
    else:
        exit()

#FOLLOWUNFOLLOW PART
elif key == 2:
    USERID()
    print ""
    userID = raw_input("[+]userID: ")
    while True:
        InstagramAPI.follow(userID)
        time.sleep(3)
        InstagramAPI.unfollow(userID)
        time.sleep(1)

#LIKEUNLIKE PART
elif key == 3:
    MEDIAID()
    print ""
    mediaID = raw_input("[+]media id: ")
    continue1 = raw_input("[+]Do you wanna continue?[Y/N]: ")
    if continue1 == "Y":
        while True:
            InstagramAPI.like(mediaID)
            time.sleep(2)
            InstagramAPI.unlike(mediaID)
            time.sleep(2)

#DIRECT MESSAGES SPAM PART
elif key == 4:
    USERID()
    print ""
    message = raw_input("[+]message: ")
    userID = raw_input("[+]userID: ")
    while True:
        InstagramAPI.direct_message(message, userID)
        time.sleep(5)

else:
    exit()

