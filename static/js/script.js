light_dark = document.getElementsByClassName("sun-moon")[0];

light_dark.addEventListener("click", function(){
	if (light_dark.className.includes("dark")) {
		light_dark.src = "static/img/night.png";
	}
	else {
		light_dark.src = "static/img/brightness.png";
	}
})