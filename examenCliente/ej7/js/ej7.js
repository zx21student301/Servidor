onload = principal;

function principal() {
    let ctx;
    canvas = document.getElementById("myCanvas");
    ctx = canvas.getContext("2d")

    ctx.fillStyle = '#0000FF';
    ctx.beginPath();
    ctx.arc(200, 200, 150, 0, 2 * Math.PI);
    ctx.fill();

    ctx.fillStyle = '#00FF00';
    ctx.beginPath();
    ctx.arc(200, 200, 100, 0, 2 * Math.PI);
    ctx.fill();

    ctx.fillStyle = '#FF0000';
    ctx.beginPath();
    ctx.arc(200, 200, 50, 0, 2 * Math.PI);
    ctx.fill();

    
}