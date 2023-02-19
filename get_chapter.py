import os
import requests

from download_page import download_page

def get_chapter(chapter):
	base_url = "https://api.mangadex.org/"
	chapter_page = requests.get(base_url + "at-home/server/" + chapter)
	return chapter_page.json()

	# os.makedirs("download/" + directory)
	# for index, page in enumerate(chapter_data):
	# 	file_path = directory + str(index) + "." + page.split(".")[-1]
	# 	download_page(host + "/data/" + chapter_hash + "/" + page, file_path)

	
