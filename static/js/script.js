light_dark = document.getElementsByClassName("light-img")[0];
header = document.getElementsByClassName("header-dark")[0];
body = document.getElementsByClassName("body-dark")[0];
footer = document.getElementsByClassName("footer-dark")[0];
freepik_attribute = document.getElementsByClassName("freepik")[0];

light_dark.addEventListener("click", function(){
	if (light_dark.className.includes("light-img")) {
		light_dark.src = "static/img/night.png";

		light_dark.className = "dark-img light";
		body.className = "body-light light";
		header.className = "header-light light header";
		footer.className = "footer-light light footer";
		freepik_attribute.className = "light freepik";
	}
	else {
		light_dark.src = "static/img/brightness.png";

		light_dark.className = "light-img dark";
		body.className = "body-dark dark";
		header.className = "header-dark dark header";
		footer.className = "footer-dark dark footer";
		freepik_attribute.className = "dark freepik";
	}
})