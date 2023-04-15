import pytube

download_loc = "./"
videourl = input("Enter url: \n")
video_instance = pytube.YouTube(videourl)
stream = video_instance.streams.get_highest_resolution()

stream.download()
