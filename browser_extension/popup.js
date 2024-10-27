document.getElementById('checkBtn').addEventListener('click', () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const currentUrl = tabs[0].url;

        chrome.runtime.sendMessage({ action: "checkPhishing", url: currentUrl }, (response) => {
            const resultDiv = document.getElementById('result');
            if (response.result === "phishing") {
                resultDiv.textContent = "Warning! This site might be a phishing site.";
                resultDiv.style.color = "red";
            } else if (response.result === "safe") {
                resultDiv.textContent = "This site appears safe.";
                resultDiv.style.color = "green";
            } else {
                resultDiv.textContent = response.message || "Error checking site.";
                resultDiv.style.color = "orange";
            }
        });
    });
});
