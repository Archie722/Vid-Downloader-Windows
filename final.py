# Allows you to enter bash commands in the program
# each command is a seperate entity in a list
import subprocess


def single_url():
    url = input("Enter the URL of the video to download:> \n")
    path = 'C:/Users/User/Downloads/vid-downloads/%(title)s.%(ext)s'
    subprocess.call(['youtube-dl', '-o', path, url])

# youtube-dl is a terminal command line program, modified to use in this program
def playlist():
    url = input("Enter the URL of playlist page:> \n")
    start = input("Enter the playlist stat number (eg 1):>\n")
    end = input("Enter the playlist end number (number of videos to download):>\n")
    format = 'mp4'

    path = 'C:/Users/User/Downloads/vid-downloads/%(title)s.%(ext)s'
    subprocess.call(['youtube-dl', '-o', path, '--playlist-start', start,\
        '--playlist-end', end, '--recode-video', format,  url])

def from_file():
    path = 'C:/Users/User/Downloads/vid-downloads/%(title)s.%(ext)s'
    format = 'mp4'
    urls = open('vid_list.txt', 'r')
    urls.read()
    urls.close()
    subprocess.call(['youtube-dl', '-o', path, '-a', 'vid_list.txt',\
        '--recode-video', format])
print ("""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmmmmmmmmmmmmmmmmmmmmmmmmmmmMMMM
MMMMNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs///////////////////////////dMMM
MMMy  ... .oMMMMMMMMMMMMMMMMMMMMMMMMMMo/omd//////////////dm+//////dMMM
MMMy `MMMd  dMy+//odMMo+s//Nh+so//omMMo/oMmsyys//ss///ss/mMsyys+//dMMM
MMMy  ///. /N. odh: /M` :hhMs `hmo .MMo/oMMysdMd/MM//+MM/mMmssNMs/dMMM
MMMy `hhhdNMh `MMMd  M` hMMMs :MMd `MMo/oMm//oMm/MM//+MM/mMo//yMd/dMMM
MMMy `MMMMMMM/ :so.`sM` dMMMs /MMd `MMo/oMm//oMm/NMysdMM/mMmyyNMs/dMMM
MMMmyhMMMMMMMMmysshNMMhyNMMMmydMMNyhMMo/+so//+so/+sys+ss/ososys+//dMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs///////////////////////////dMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmmmmmmmmmmmmmmmmmmmmmmmmmmNMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
________                      .__                    .___
\______ \   ______  _  ______ |  |   _________     __| _/___________
 |    |  \ /  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ \
 |    `   (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/
/_______  /\____/ \/\_/|___|  /____/\____(____  /\____ |\___  >__|
        \/                  \/                \/      \/    \/
""")
print ("""Choose from the following options:\n
            1 - Download single Video by url
            2 - Download multiple files from a playlist url
            3 - Download multiple urls from a .txt file
            """)
choice = input(":>")
if choice == "1":
    single_url()
if choice == "2":
    playlist()
if choice == "3":
    print ("Make sure the URL's saved to a file called 'vid_list' in the same folder")
    input("press Enter to confirm :>")
    from_file()
