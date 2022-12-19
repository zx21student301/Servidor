


function ponerBorde() {
    let borde = document.getElementById('ancho').value;
    document.getElementById("parrafo").style.border=""+borde+"px solid";
}

function quitarBorde() {
    document.getElementById("parrafo").style.border="0px solid";
}