const messageInput = document.getElementById("message");
const charCount = document.getElementById("charCount");
const clearButton = document.querySelector('button[type="button"]');
const submitButton = document.querySelector('button[type="submit"]');
const predictionSection = document.getElementById("prediction-section");
const predictionCard = document.getElementById("prediction-card");
const form = document.querySelector("form");


if (predictionSection && predictionSection.textContent.trim() === "") {
    predictionSection.style.display = "none";
} else {
    predictionSection.style.display = "block";
}

submitButton.disabled = messageInput.value.trim().length === 0;

submitButton.textContent = "Detect Spam";

clearButton.disabled = false;

charCount.textContent = `${messageInput.value.length} / 500`


messageInput.addEventListener("input", function(){

    charCount.textContent = `${messageInput.value.length} / 500`;

    submitButton.disabled = messageInput.value.trim() === "";

    messageInput.style.height = "auto";

    messageInput.style.height = messageInput.scrollHeight+"px";

});

clearButton.addEventListener("click", function(){

    messageInput.value = "";
    messageInput.style.height = "auto";
    charCount.textContent = "0 / 500";

    submitButton.disabled = true;
    submitButton.textContent = "Detect Spam";

    predictionCard.innerHTML = `<p class="waiting-text">Waiting for prediction...</p>`;

    messageInput.focus();

})


form.addEventListener("submit", function(){

    if (messageInput.value.trim() === "") {
        return;
    }

    submitButton.disabled = true;
    clearButton.disabled = true;

    submitButton.innerHTML = "⏳ Analyzing...";

})
