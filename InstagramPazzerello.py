__author__ = 'ehipablo'
#tested with python 2.7.5 on Parrot Os (Debian)
from InstagramAPI import InstagramAPI
import time

#INSTALL MODULE InstagramAPI: python -m pip install -e git+https://github.com/LevPasha/Instagram-API-python.git#egg=InstagramAPI
#TO SEE THE MEDIA ID "https://api.instagram.com/oembed/?url= + URLPHOTO"

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

text = raw_input("[+]Comment: ")
mediaID = raw_input("[+]media id: ")
print ""
continue1 = raw_input("[+]Do you wanna continue?[Y/N]: ")

if continue1 == "Y":
    while True:
        for x in range(6):
            InstagramAPI.comment(mediaID, text)
        time.sleep(20)
    print "ok"
else:
    exit()
