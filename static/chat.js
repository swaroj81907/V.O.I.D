
function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;
    if (!message) return;

    addToChat("You", message);
    input.value = "";

    fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        addToChat("AI", data.reply);
    })
    .catch(error => {
        addToChat("AI", "❌ Error: " + error);
    });
}

function addToChat(sender, message) {
    const chatLog = document.getElementById("chat-log");
    const msgDiv = document.createElement("div");
    msgDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatLog.appendChild(msgDiv);
    chatLog.scrollTop = chatLog.scrollHeight;
}
