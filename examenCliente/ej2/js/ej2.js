function validaDatos() {

    //validar que el texto tiene menos de 10 caracteres
    let resp = true;
    let t = document.getElementById("tex").value;
    let n = parseInt(document.getElementById("num").value);
    
     //PARA VER QUE TIENE MENOS DE 10 CARACTERES
    if (t.length < 10) {
        resp = true;

        //PARA VER QUE ES UN NUMERO
        if (Number.isInteger(n)) {
            //PARA VER QUE ES MENOR DE 10
            if (n < 100) {
                alert("El numero es: " + n)
                resp = true;
            }else {
                alert("Debe ser menor que 100")
                resp = false
            }
        }else{
            alert("No es un número")
            resp = false;
        }
    } else {
        alert("Debe tener menos de 10 caracteres");            
        resp = false;
    }

    return resp
}


