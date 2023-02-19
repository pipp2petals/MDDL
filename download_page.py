import requests
import time

def download_page(page, filename):
	current_page = requests.get(page)

	with open("download/" + filename, "wb") as image_file:
		image_file.write(current_page.content)
	time.sleep(10)
	