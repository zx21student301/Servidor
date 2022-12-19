onload = compruebaLoteria;


function compruebaLoteria() {

	let n = parseInt(document.getElementById("boleto").value)
    let cont = 0

	if (Number.isInteger(n)) {
		if (n >= 1 && n <= 60) {
            cont++;
			//crear el objeto XMLHttpRequest para acceder al servidor
			let xmlhttp = new XMLHttpRequest();

			//registrar la funcion que se ejecuta con la respuesta del servidor
			xmlhttp.onreadystatechange = function () {

				//evaluar la respuesta del servidor
				if (this.readyState == 4 && this.status == 200) {

					//tratar los datos enviados por el servidor
					document.getElementById("salida").innerHTML = "Boleto con "+this.responseText+"aciertos";
				}
			};

			//construir la peticion al servidor
			xmlhttp.open("GET", "ej6.py?numeros=" + n, true);

			//ejecutar la peticion al servidor
			xmlhttp.send();

		} else {
			alert("no es un número entre 0 y 60");
		}
    }
}
