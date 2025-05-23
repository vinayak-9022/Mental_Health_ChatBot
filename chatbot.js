// Simple function to send user input to the Flask API
function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (userInput.trim() === "") return;

    // Display the user's message in the chat box
    const chatBox = document.getElementById('chatBox');
    const userMessage = document.createElement('div');
    userMessage.classList.add('chat-entry');
    userMessage.innerHTML = `<p><strong>You:</strong> ${userInput}</p>`;
    chatBox.appendChild(userMessage);

    // Make a POST request to the Flask backend with user input
    fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_input: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = document.createElement('div');
        botMessage.classList.add('chat-entry');
        botMessage.innerHTML = `<p><strong>Chatbot:</strong> ${data.response}</p>`;
        chatBox.appendChild(botMessage);

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
    });

    // Clear the input field
    document.getElementById('userInput').value = "";
}
