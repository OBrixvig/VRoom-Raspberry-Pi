// Funktion der håndterer pinkode-validering ved form submit
async function submitPin(event) {
    if (event) event.preventDefault(); // Forhindrer side reload ved submit
    const pin = document.getElementById('pin').value; // Henter pinkode fra input
    const statusIcon = document.getElementById('status-icon'); // Ikon til status
    const statusText = document.getElementById('status-text'); // Tekst til status

    // Tjekker om pinkoden er præcis 4 cifre
    if (!/^\d{4}$/.test(pin)) {
        statusIcon.textContent = "❌"; // Viser fejl-ikon
        statusText.textContent = "Pincode skal være præcis 4 cifre (0-9)."; // Fejlbesked
        statusText.style.color = "red"; // Rød tekst
        return;
    }
    try {
        // Sender pinkode til serveren for validering
        const response = await fetch('/validate-pin', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ pincode: pin })
        });
        const data = await response.json(); // Læser svaret fra serveren

        if (response.ok && data.success) {
            statusIcon.textContent = "✅"; // Viser succes-ikon
            statusText.textContent = data.message; // Succesbesked
            statusText.style.color = "green"; // Grøn tekst
        } else {
            statusIcon.textContent = "❌"; // Fejl-ikon
            statusText.textContent = data.message; // Fejlbesked fra server
            statusText.style.color = "red"; // Rød tekst
        }
    } catch (err) {
        statusIcon.textContent = "❌"; // Fejl-ikon
        statusText.textContent = "Der opstod en fejl. Prøv igen."; // Generel fejlbesked
        statusText.style.color = "red"; // Rød tekst
    }
}