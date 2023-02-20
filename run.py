from flask import Flask, render_template, url_for, request

from pyscripts.chapter import Chapter

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		print(request.form)
		if "SearchBar" in request.form:
			if request.form["SearchValues"] == "chapter":
				chapter = Chapter(request.form["SearchBar"])
				data_saver = "DataSaver" in request.form
				if "Directory" in request.form:
					download = request.form["Directory"]
				else:
					download = "download/"
				chapter.get_chapter(data_saver)
				chapter.download_pages(download)
			
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)
