chrome.runtime.onInstalled.addListener(() => {
    console.log("PhishEye Extension Installed");
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "checkPhishing") {
        checkPhishing(message.url, sendResponse);
        return true;  // Keeps the message channel open for async response
    }
});

function checkPhishing(url, sendResponse) {
    fetch('http://127.0.0.1:5000/detect', {  // Ensure the route matches your Flask app
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        sendResponse({ result: data.result === "Phishing" ? "phishing" : "safe" });
    })
    .catch(error => {
        console.error("Error checking URL:", error);
        sendResponse({ result: "error", message: "Could not connect to backend." });
    });
}
