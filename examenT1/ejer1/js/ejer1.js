let n1 = parseInt(prompt("Introduce 1) numero"));
let n2 = parseInt(prompt("Introduce 2) numero"));
let n3 = parseInt(prompt("Introduce 3) numero"));
let n4 = parseInt(prompt("Introduce 4) numero"));

if (Number.isInteger(n1) && Number.isInteger(n2) && Number.isInteger(n3) && Number.isInteger(n4)) {
    let media = (n1 + n2 + n3 + n4) / 4;
    alert("La media de sus numeros es: " + media);

    //PARA COGER EL MINIMO VALOR DE TODOS LOS N
    alert("El número mas pequeño es el: "+Math.min(n1,n2,n3,n4))

    //PARA COGER EL MAXIMO VALOR DE TODOS LOS N
    alert("El número mas grande es el: "+Math.max(n1,n2,n3,n4))

} else {
    alert("Error algún número no es entero");
}