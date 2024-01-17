# hub-solar
Solar energy generation data for The Hub, Beeding

<div id="content"></div>

<script>
// Use the Fetch API to load the JSON file
fetch('plant_data/today.json')
  .then(response => {
    // Check if the response is successful
    if (!response.ok) {
      throw new Error('Network response was not ok ' + response.statusText);
    }
    return response.json(); // Parse the JSON in the response
  })
  .then(data => {
    // Now 'data' contains the parsed JSON object
    const value = data.plantData.currentEnergy; // Replace 'key' with the actual key from your JSON file

    // Select the HTML element by ID and set its content
    document.getElementById('content').textContent = value;
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('Fetching and parsing data error', error);
  });
</script>