
function cambiaFondo(id) {
	//COGEMOS TODOS LOS ID DE LOS PARRAFOS PARA USARLOS 
    let p1 = document.getElementById('p1')
	let p2 = document.getElementById('p2')
	let p3 = document.getElementById('p3')

	//PINTAMOS TODOS BLANCOS PARA QUE CADA VEZ QUE DEMOS A OTRO BOTON LOS REINICIE A SU COLOR ORIGINAL PARA DESPUES PINTARLO ENCIMA
    p1.style.backgroundColor = "white";
	p2.style.backgroundColor = "white";
	p3.style.backgroundColor = "white";

	//AQUI INDICAMOS CUAL ES EL QUE QUEREMOS QUE PINTE DE AZUL
	let parrafoAzul = document.getElementById(id)
	parrafoAzul.style.backgroundColor = "lightblue";
}
	

