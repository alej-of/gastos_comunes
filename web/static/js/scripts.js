setTimeout(function() {
    const message = document.getElementById('auto-hide-message');
    if (message) {
        message.style.display = 'none';
    }
}, 5000);

document.querySelectorAll('.delete-form').forEach(form => {
    form.addEventListener('submit', function(event) {
        if (!confirm('¿Estás seguro de que deseas eliminar este extra?')) {
            event.preventDefault(); // Prevent the form submission if user cancels
        }
    });
});