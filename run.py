from flask import Flask, render_template, url_for, request

from pyscripts.chapter import Chapter
from pyscripts.manga import Manga

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
	manga = "Manga Name"
	chapter = "Chapter 0"
	scanlator = "Scanlator"
	if request.method == "POST":
		print(request.form)
		if "SearchBar" in request.form:
			if "Directory" in request.form and len(request.form["Directory"]) > 0:
				download = request.form["Directory"]
			else:
				download = "download/"

			languages = []
			for form in request.form:
				if len(form) <= 5:
					languages.append(request.form[form])

			print(languages)
			if request.form["SearchValues"] == "manga":
				manga = Manga(request.form["SearchBar"])
				manga.get_manga()
				manga.set_parameters(languages)
				manga.get_feed()
				if download == "download/":
					download = download + manga.title + "/"
					old_download = download
				manga_feed = manga.feed.json()["data"]
				manga_feed.reverse()
				for index, chap in enumerate(manga_feed):
					print(chap, "\n")
					chapter = Chapter(chap["id"])
					data_saver = "DataSaver" in request.form
					
					chapter.get_chapter(data_saver)
					download = old_download + str(chap["attributes"]["chapter"]) + "/"
					chapter.download_pages(download)

			elif request.form["SearchValues"] == "chapter":
				chapter = Chapter(request.form["SearchBar"])
				data_saver = "DataSaver" in request.form
				
				chapter.get_chapter(data_saver)
				chapter.download_pages(download)
			
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)
