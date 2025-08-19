document.getElementById("generateBtn").addEventListener("click", async () => {
  const durationType = document.getElementById("durationType").value;
  const durationValue = document.getElementById("durationValue").value;

  // Simple validation
  if (!durationValue || durationValue < 1) {
    alert("Please enter a valid duration value.");
    return;
  }

  try {
    // Call backend Python API (you need to set up a simple server to run generatekey.py)
    const response = await fetch(`/generate-key?type=${durationType}&value=${durationValue}`);
    const data = await response.json();

    if (data.key) {
      document.getElementById("generatedKey").value = data.key;
    } else {
      document.getElementById("generatedKey").value = "Error generating key";
    }
  } catch (err) {
    console.error(err);
    document.getElementById("generatedKey").value = "Error generating key";
  }
});
