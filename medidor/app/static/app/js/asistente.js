$.ajax({
    url: "/chat-ai/",  // debe ser exactamente la misma ruta
    type: "POST",
    data: JSON.stringify({ pregunta: pregunta }),
    contentType: "application/json",
    success: function(response){
        $('#chat-box').append('<p><b>IA:</b> ' + response.respuesta + '</p>');
    },
    error: function(){
        $('#chat-box').append('<p><b>IA:</b> Error al conectar con el servidor.</p>');
    }
});
