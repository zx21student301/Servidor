onload = principal;

function principal() {
	document.getElementById("enviar").setAttribute("onclick", "compruebaPrimo()");
}

function compruebaPrimo() {

	let n = parseInt(document.getElementById("num").value);

	if (Number.isInteger(n)) {
		if (n >= 0 && n <= 100) {

			//crear el objeto XMLHttpRequest para acceder al servidor
			let xmlhttp = new XMLHttpRequest();

			//registrar la funcion que se ejecuta con la respuesta del servidor
			xmlhttp.onreadystatechange = function () {

				//evaluar la respuesta del servidor
				if (this.readyState == 4 && this.status == 200) {

					//tratar los datos enviados por el servidor
					document.getElementById("salida").innerHTML = this.responseText;
				}
			};

			//construir la peticion al servidor
			xmlhttp.open("GET", "primos.py?numero=" + n, true);

			//ejecutar la peticion al servidor
			xmlhttp.send();

		} else {
			alert("no es un número entre 0 y 100");
		}
	} else {
		alert("no es un número entero");
	}

}