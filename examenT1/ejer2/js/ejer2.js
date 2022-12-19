function validaTexto() {

    //SI EL TEXTO ES CORRECTO ENVIA EL FORMULARIO, AUNQUE DE ERROR

    //validar que el texto tiene entre 8 y 10 caracteres
    //validar que empiece por "123"
    let resp = true;
    let t = document.getElementById("texto").value;

    //PARA VER QUE ESTA ENTRE 8 Y 10 CARACTERES
    if (t.length < 8 || t.length > 10) {
        alert("No tiene entre 8 y 10 caracteres");
        resp = false;
    }else{
        alert("Numero de caracteres correcto");
    }

    //PARA VER SI EMPIEZA O NO POR 123
    if (t.substring(0, 3) !== "123") {
        alert("El texto no empieza por 123");
        resp = false;
    }else{
        alert("Empieza por 123");
    }
    
    //PARA VER SI TERMINA O NO POR 123
    if(t.slice(-3)=="123"){
        alert("termina en 123")
    }else{
        alert("no termina por 123")
        resp = false;
    }
    console.log(t.slice(-3))
    return resp

    /*
    OTRAS FORMAS DE VER QUE NO EMPIEZA POR 123

    if(t.substring(-3)!=="123"){
        alert("El texto no empieza por 123");
        resp=false;
    }
    console.log(t.slice(-3))
    return resp

------------------------------------------------------------

    if (t[0] != "1" || t[1] != "2" || t[2] != "3") {
        alert("El texto no empieza por 123");
        resp = false;
    return resp
    
    }*/
}