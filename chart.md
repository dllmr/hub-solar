---
layout: dashboard
---

# hub-solar

<!-- Step 2: Create a canvas element where the chart will be rendered -->
<canvas id="barChart" width="100" height="100"></canvas>

<!-- Step 3 & 4: Embed your data and initialize the chart -->
<script>
    // Data for the chart
    var chartData = {
        labels: [],
        datasets: [{
            label: 'Time/Date',
            data: [],
            borderWidth: 1
        }]
    };

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
        chartData.labels = Object.keys(data.data);
        chartData.datasets[0].data = Object.values(data.data);
    })
    .catch(error => {
        // Handle any errors that occurred during the fetch
        console.error('Fetching and parsing data error', error);
    });

    // Configuration for the chart
    const config = {
        type: 'bar',
        data: chartData,
        options: {
            responsive: true, // Makes the chart responsive to window size
            maintainAspectRatio: false, // Allows chart to stretch in height
            layout: {
                padding: { // Add padding around the canvas
                    top: 50,
                    right: 50,
                    bottom: 50,
                    left: 50
                }
            },
            indexAxis: 'x', // Sets the index axis to y, creating a horizontal bar chart
            scales: {
                x: {
                    grid: {
                        display: false // Removes the gridlines on the y-axis
                    }
                },
                y: {
                    grid: {
                        display: false // Removes the gridlines on the y-axis
                    }
                }
            },
            barPercentage: 0.95,
            categoryPercentage: 1.0
        }
    };

    // Initialize the chart
    const myHorizontalBarChart = new Chart(
        document.getElementById('barChart'),
        config
    );
</script>
</body>
</html>

