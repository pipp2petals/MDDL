import requests
import time

from pyscripts.chapter import Chapter

class Manga:
	def __init__(self, manga_id):
		self.manga = manga_id
		self.base_url = "https://api.mangadex.org/"
		self.manga_url = self.base_url + "manga/" + manga_id
		self.feed_url = self.base_url + "manga/" + manga_id + "/feed"
		self.lang = []

		self.title = "Manga Name"

	def set_parameters(self, languages=[]):
		self.lang = languages
	
	def get_manga(self):
		print("Retrieving Manga.")
		self.manga = requests.get(self.manga_url)
		self.title = self.manga.json()["data"]["attributes"]["title"]
		self.title = self.title["en"] if "en" in self.title else self.title["jp"]
		print("Manga retrieved.")
		time.sleep(5)

	def get_feed(self):
		print("Retrieving feed.")
		self.feed = requests.get(self.feed_url,
								params={
									"translatedLanguage[]": self.lang
								})
		print("Feed retrieved.")
		time.sleep(10)