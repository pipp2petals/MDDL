import os
import requests
import time

class Chapter:
	def __init__(self, chapter_id):
		self.chapter_id = chapter_id
		self.url = "https://api.mangadex.org/at-home/server/" + chapter_id

	def get_chapter(self, data_saver=False):
		page = requests.get(self.url)
		self.chapter_json = page.json()
		self.host = self.chapter_json["baseUrl"]
		self.chapter_hash = self.chapter_json["chapter"]["hash"]
		if data_saver:
			self.pages = self.chapter_json["chapter"]["dataSaver"]
		else:
			self.pages = self.chapter_json["chapter"]["data"]
		print("Obtaining chapter.")
		# time.sleep(20)
		print("Chapter obtained.")

	def download_pages(self, directory="download/"):
		os.makedirs(directory, exist_ok=True)

		for index, page in enumerate(self.pages):
			if str(index + 1) + "." + page.split(".")[-1] in os.listdir(directory):
				pass
			else:
				url = self.host + "/data/" + self.chapter_hash + "/" + page
				image = requests.get(url)
				with open(directory + "/" + str(index + 1) + "." + page.split(".")[-1], "wb") as image_file:
					image_file.write(image.content)
				time.sleep(10)
				print("Page " + str(index + 1) + " of " + str(len(self.pages)))