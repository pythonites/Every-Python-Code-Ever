import urllib.request 

url = input("Enter URL of video to be downloaded: ")

name = "/storage/emulated/0/Abhi/" + input("Enter name of the video: ") + '.mp4'

try:
	print("Downloading starts..")
	urllib.request.urlretrieve(url,  name)
	print("Downloading completed")
	
except Exception as e:
	print(e)
