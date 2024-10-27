window.onload = () => {
    const currentUrl = window.location.href;
    chrome.runtime.sendMessage({ action: "checkPhishing", url: currentUrl }, (response) => {
        if (response.result === "phishing") {
            alert("Warning! This site might be a phishing site.");
        } else if (response.result === "safe") {
            console.log("This site appears safe.");
        } else {
            console.log(response.message || "Error checking site.");
        }
    });
};
