window.onload = maximo
window.onload = maximo

function maximo(){
    let sep = (prompt("Introduce 3 números"));
    let numeros = sep.split(" ");

    let n1 = parseInt(numeros[0]);
    let n2 = parseInt(numeros[1]);
    let n3 = parseInt(numeros[2]);

    if(Number.isInteger(n1) && Number.isInteger(n2) && Number.isInteger(n3) ){
        alert("El número mas alto es el: "+Math.max(n1, n2, n3))
    
    }else{
        alert("Lo valores introducidos no son correctos")
    }
}

