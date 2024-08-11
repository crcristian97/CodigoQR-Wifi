document.getElementById('password').addEventListener('input', function() {
  const passwordHint = document.getElementById('passwordHint');
  const password = this.value;

  if (password) {
    passwordHint.textContent = `You have entered ${password.length} characters`;
  } else {
    passwordHint.textContent = ''; // Limpia el texto cuando no hay contraseña
  }
});

document.getElementById('qrForm').addEventListener('submit', async function(e) {
  e.preventDefault();

  const ssid = document.getElementById('ssid').value;
  const password = document.getElementById('password').value;

  const response = await fetch('/generate_qr', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ ssid, password })
  });

  const result = await response.json();

  if (response.ok) {
    const qrCodeImage = document.getElementById('qrCodeImage');
    qrCodeImage.src = result.image_path;
    qrCodeImage.style.display = 'block';

    Toastify({
      text: "Código generado",
      duration: 3000, 
      gravity: "top", 
      position: "right", 
      backgroundColor: "#28a745",
    }).showToast();

  } else {
    alert(result.error || 'An error occurred');
  }
});
