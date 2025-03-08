document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const confirmationMessage = document.getElementById('confirmationMessage');

    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Previene el envío por defecto del formulario

        // Recoger los datos del formulario
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);

        // Enviar los datos al servidor
        fetch('http://localhost:5000/submit_form', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            // Oculta el formulario
            form.style.display = 'none';

            // Muestra el mensaje de confirmación
            confirmationMessage.textContent = data.message;
            confirmationMessage.style.display = 'block';

            // Opcional: Desplázate hasta el mensaje de confirmación
            confirmationMessage.scrollIntoView({ behavior: 'smooth' });

            // Opcional: Reinicia el formulario después de un tiempo
            setTimeout(() => {
                form.reset();
                form.style.display = 'block';
                confirmationMessage.style.display = 'none';
            }, 5000); // 5 segundos
        })
        .catch((error) => {
            console.error('Error:', error);
            confirmationMessage.textContent = 'Hubo un error al enviar el formulario. Por favor, inténtalo de nuevo.';
            confirmationMessage.style.display = 'block';
        });
    });
});



