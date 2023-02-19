from flask import Flask, render_template, url_for, request

from get_chapter import get_chapter

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		print(request.form)
		if request.form["exact_type"] == "Search":
			print("Search for a manga. Redirect to search page.")
		elif request.form["exact_type"] == "Manga":
			print("Download manga.")
		elif request.form["exact_type"] == "Chapter":
			chapter = get_chapter(request.form["searchbar"])
			if "data_saver" in request.form:
				chapter_data = chapter["chapter"]["dataSaver"]
			else:
				chapter_data = chapter["chapter"]["data"]

			
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)
