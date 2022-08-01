import os
import time
import urllib.request
from moviepy.editor import VideoFileClip

from notemanager import Movie

def task1():
    return hash("Python Bootcamp") # simple hash function to solve the problem

def task2(link):
    tempname = "temp.mp4" # defining file extension
    save_path = os.path.join(os.getcwd(), "output/")
    if not os.path.exists(save_path): # creating output folder if not exists
        os.makedirs(save_path)
    urllib.request.urlretrieve(link, tempname) # downloading source video
    vid = VideoFileClip(tempname) # converting source video into VideoFileClip object
    gif_name = save_path + time.strftime("%Y%m%d%H%M%S") + ".gif"
    vid.write_gif(gif_name, 5, verbose = False, logger = None) # second parameter there is the number of frames per second - for showcase purposes 5 fps was used to speed up the converting process, which may take quite a bit of time if source video is long enough. You can remove 3rd and 4th parameters to enable console progress bar
    vid.close() # closing temporary videofile to allow us to remove it in the next step
    os.remove("temp.mp4")
    return gif_name

#print(task1())
#print(task2("https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55"))
#Movie.print_notes("movielist.csv")
#Movie.best_rated("movielist.csv", 3)
#Movie.worst_rated("movielist.csv", 2)
#Movie.get_average_rating("movielist.csv")
#Movie.add_note("movielist.csv", "The Rising Hawk", "historical action", "5")
#Movie.remove_note("movielist.csv", "The Rising Hawk")