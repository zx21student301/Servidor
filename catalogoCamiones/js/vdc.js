onload = principal

let listaCamiones;

function principal(){
    listaCamiones = document.getElementById("listaCamiones");
    cargarServidorCamiones();
}

function cargarServidorCamiones(){
    //una peticion al servidor de la lista de camiones - AJAX
    //crear el objeto XMLHttpRequest para acceder al servidor
	let jsonhttp = new XMLHttpRequest();

    //*********************************
	// codigo para tratar la respuesta
	jsonhttp.onreadystatechange  = function(){
		//evaluar la respuesta del servidor
        if(this.readyState == 4 && this.status == 200){
            let listaC = JSON.parse(this.responseText);   

            for (c of listaC){
                listaCamiones.append(crearCamion(c))
            }
		}
	}

    //construir la petición al servidor
	jsonhttp.open("GET","http://www.servidor.es/catalogoCamiones/listarCamiones.py",true);
	//ejecutar la petición al servidor
	jsonhttp.send();
}

function crearCamion(c){

    let img = c[4];
    let marca = c[0];
    let modelo = c[1];
    let desc = c[2];
    let precio = c[3];

    let divTarjCam = document.createElement("div");
    divTarjCam.setAttribute("class","card m-3");

    let divRow = document.createElement("div");
    divRow.setAttribute("class","row g-0");

    let subDivImg = document.createElement("div");
    subDivImg.setAttribute("class","col-md-5");

    let imagen = document.createElement("img");
    imagen.setAttribute("src","img/"+img);
    imagen.setAttribute("class","img-fluid rounded-start");
    imagen.setAttribute("alt",marca+" "+modelo);

    let subDivInfo = document.createElement("div");
    subDivInfo.setAttribute("class","col-md-7");

    let 

    let camion = '\
    <div class="card m-3">\
        <div class="row g-0">\
        <div class="col-md-5">\
            <img src="img/'+c[4]+'" class="img-fluid rounded-start" alt="'+c[0]+' '+c[1]+'">\
        </div>\
        <div class="col-md-7">\
            <div class="card-body">\
            <h5 class="card-title">Modelo: '+c[1]+'</h5>\
            <p class="card-text">Marca: '+c[0]+'</p>\
            <p class="card-text">Precio: '+c[3]+' &euro;</p>\
            <p class="card-text">Descripci&oacute;n: '+c[2]+'</p>\
            </div>\
        </div>\
        </div>\
    </div>';

    return camion;
}