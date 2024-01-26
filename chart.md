---
layout: dashboard
---

# hub-solar

<div style="margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; height: 100vh;">

<canvas id="barChart" width="100" height="100"></canvas>

<script>
    // Data for the chart
    var chartData = {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: 'Time/Date',
            data: [12, 19, 3, 5, 2, 3],
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
        // Select the HTML element by ID and set its content
        //chartData.labels = "00:00";
        //chartData.datasets[0].data = [0];
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
            indexAxis: 'x',
            scales: {
                x: {
                    grid: {
                        display: false // Removes the gridlines on the x-axis
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
    const myBarChart = new Chart(
        document.getElementById('barChart'),
        config
    );
</script>

</div>