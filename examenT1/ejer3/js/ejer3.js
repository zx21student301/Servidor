//hacer una funcion que se llame sonPares

//que recibe un array con numeros

//comprueba que son todos pares

//devuelve true si se cumple la condicion y false en caso contrario
onload = sonPares;

function sonPares() {
    par = true
    array=[2,6,44,2]
    for (let x = 0; x < array.length; x++) {
        resto = array[x]%2
        if (resto!=0) {
            par = false            
        }
    }

    console.log(par)

}