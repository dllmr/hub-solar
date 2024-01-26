layout: dashboard

# hub-solar

Solar energy generation data for The Hub, Beeding: -

<div id="today">
</div>

<div id="this_month">
</div>

<script>
// Use the Fetch API to load the JSON file for today's data
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
    document.getElementById('today').textContent = value + ' generated today;';
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('Fetching and parsing data error', error);
  });

// Use the Fetch API to load the JSON file for this month's data
fetch('plant_data/this_month.json')
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
    document.getElementById('this_month').textContent = value + ' generated this month.';
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('Fetching and parsing data error', error);
  });
</script>
