onload = principal;

let ctx;

function principal(){
    ajedrez()
    diana()
}

function ajedrez() {

    canvas = document.getElementById("myCanvas");
    ctx = canvas.getContext("2d")
    booleanBlanco = true
    filaPar = true

    for (let x = 0; x < 400; x += 50) {
        for (let y = 0; y < 400; y += 50) {
            if (y == 0) {

                if (filaPar) {
                    ctx.fillStyle = 'black'
                    booleanBlanco = true
                    filaPar = false

                } else {
                    ctx.fillStyle = 'white'
                    booleanBlanco = false
                    filaPar = true
                }
            }
            if (booleanBlanco) {
                ctx.fillStyle = 'white'
                booleanBlanco = false
            } else {
                ctx.fillStyle = 'black'
                booleanBlanco = true
            }
            console.log(x, y)
            ctx.fillRect(x, y, 50, 50)

        }
    }
}

function diana() {

    canvas = document.getElementById("myCanvas2");
    ctx = canvas.getContext("2d")
    booleanRojo = false
    filaPar = true

    for (let x = 200; x > 0; x -= 25) {

        if (booleanRojo) {
            ctx.fillStyle = 'white';
            booleanRojo=false;
        } else{
            ctx.fillStyle = 'red';
            booleanRojo=true;
        }
            ctx.beginPath();
            ctx.arc(200,200, x, 0, 2 * Math.PI);
            ctx.fill();
    }
}

    function escribirTexto(){
        var c = document.getElementById("texto");
        var ctx = c.getContext("2d");
        ctx.font = "30px Arial";
        ctx.fillStyle = "black"
        ctx.fillText("Hello World", 10, 30);
    }