onload = cuentaPronombres;

function cuentaPronombres(palabras) {
    let cont = 0

    for (let x = 0; x < palabras.length; x++) {
        if (palabras[x] == "yo" || palabras[x] == "tu" || palabras[x] == "se" || palabras[x] == "el") {
            cont++        
        }
    }
return cont
}

console.log(cuentaPronombres(["tu", "tienes","razon","yo","estaba","equivocado"]))
console.log(cuentaPronombres(["ée", "se","confundió","de","calle"]))
console.log(cuentaPronombres(["yo", "tu","el"]))