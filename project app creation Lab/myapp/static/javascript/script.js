// Wait for DOM to load before attaching listeners
document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("clickMeBtn");
    const msg = document.getElementById("message");

    btn.addEventListener("click", function () {
        msg.innerText = "Button clicked! JavaScript is working!";
        msg.style.color = "green";
    });
});
