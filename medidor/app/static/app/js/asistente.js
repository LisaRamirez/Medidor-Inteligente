
document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("acuaria-pregunta");
    const btnEnviar = document.getElementById("acuaria-enviar");
    const mensajes = document.getElementById("acuaria-messages");

    function agregarMensaje(texto, tipo="user") {
        const msg = document.createElement("div");
        msg.classList.add("acuaria-msg", `acuaria-${tipo}`);
        msg.innerHTML = `
            <div class="acuaria-avatar">${tipo === "user" ? "🙋" : "🤖"}</div>
            <div class="acuaria-message-content">
                <div class="acuaria-message-sender">${tipo === "user" ? "Tú" : "AcuaRIA"}</div>
                <div class="acuaria-message-text">${texto}</div>
            </div>`;
        mensajes.appendChild(msg);
        mensajes.scrollTop = mensajes.scrollHeight;
    }

    async function enviarPregunta() {
        const pregunta = input.value.trim();
        if (!pregunta) return;

        agregarMensaje(pregunta, "user");
        input.value = "";

        agregarMensaje("Escribiendo...", "bot");

        const resp = await fetch("/acuaria-chat/", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({pregunta})
        });

        const data = await resp.json();
        const ultBot = mensajes.querySelector(".acuaria-bot:last-child .acuaria-message-text");
        if (ultBot) ultBot.textContent = data.respuesta;
    }

    btnEnviar.addEventListener("click", enviarPregunta);
    input.addEventListener("keypress", e => {
        if (e.key === "Enter") enviarPregunta();
    });

    document.querySelectorAll("[data-question]").forEach(btn => {
        btn.addEventListener("click", () => {
            input.value = btn.dataset.question;
            enviarPregunta();
        });
    });
});

