const salesCanvas = document.getElementById("salesChart");

if (salesCanvas) {

    const labels = JSON.parse(
        salesCanvas.dataset.labels
    );

    const values = JSON.parse(
        salesCanvas.dataset.values
    );

    new Chart(salesCanvas, {

        type: "line",

        data: {

            labels: labels,

            datasets: [{

                label: "Sales",

                data: values,

                borderWidth: 3,

                tension: 0.4

            }]

        }

    });

}

const monthlyCanvas = document.getElementById("monthlySalesChart");

if (monthlyCanvas) {

    const labels = JSON.parse(monthlyCanvas.dataset.labels);

    const values = JSON.parse(monthlyCanvas.dataset.values);

    new Chart(monthlyCanvas, {

        type: "bar",

        data: {

            labels: labels,

            datasets: [{

                label: "Monthly Sales",

                data: values,

                backgroundColor: "#0d6efd"

            }]

        },

        options: {
            responsive: true,
            scales: {
                y: {
                    ticks: {
                        callback: function (value) {
                            if (value >= 1000) {
                                return (value / 1000) + "K";
                            }
                            return value;
                        }
                    }
                }
            }
        }
    });

}

const categoryCanvas = document.getElementById("categoryChart");

if (categoryCanvas) {

    const labels = JSON.parse(
        categoryCanvas.dataset.labels
    );

    const values = JSON.parse(
        categoryCanvas.dataset.values
    );

    new Chart(categoryCanvas, {

        type: "pie",

        data: {

            labels: labels,

            datasets: [{

                data: values

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false

        }

    });

}