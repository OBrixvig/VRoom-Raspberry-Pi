async function submitPin(event) {
    if (event) event.preventDefault();
    const pin = document.getElementById('pin').value;
    const statusIcon = document.getElementById('status-icon');
    const statusText = document.getElementById('status-text');
    if (!/^\d{4}$/.test(pin)) {
        statusIcon.textContent = "❌";
        statusText.textContent = "Pincode skal være præcis 4 cifre (0-9).";
        statusText.style.color = "red";
        return;
    }
    try {
        const response = await fetch('/validate-pin', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ pincode: pin })
        });
        const data = await response.json();
        if (response.ok && data.success) {
            statusIcon.textContent = "✅";
            statusText.textContent = data.message;
            statusText.style.color = "green";
        } else {
            statusIcon.textContent = "❌";
            statusText.textContent = data.message;
            statusText.style.color = "red";
        }
    } catch (err) {
        statusIcon.textContent = "❌";
        statusText.textContent = "Der opstod en fejl. Prøv igen.";
        statusText.style.color = "red";
    }
}