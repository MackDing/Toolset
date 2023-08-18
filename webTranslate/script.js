const translateButton = document.getElementById("translateButton");
const wordInput = document.getElementById("wordInput");
const translationResult = document.getElementById("translationResult");

translateButton.addEventListener("click", async () => {
  const word = wordInput.value.trim();
  
  if (word === "") {
    translationResult.textContent = "Please enter a word.";
    return;
  }

  try {
    const response = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`);
    const data = await response.json();

    if (Array.isArray(data) && data.length > 0) {
      const translation = data[0].meanings[0].definitions[0].definition;
      translationResult.textContent = `Translation: ${translation}`;
    } else {
      translationResult.textContent = "Word not found.";
    }
  } catch (error) {
    console.error("Error fetching translation:", error);
    translationResult.textContent = "An error occurred.";
  }
});