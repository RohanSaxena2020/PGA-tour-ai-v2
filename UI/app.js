async function calculateScoringAverage() {
    const inputs = [
        "sg_ott",
        "sg_app",
        "sg_atg",
        "sg_putting",
        "birdie_avg",
        "driving_dist_yds",
        "gir_pct",
    ];

    const data = {};
    inputs.forEach((id) => {
        data[id] = parseFloat(document.getElementById(id).value);
    });

    try {
        const response = await fetch("/predict/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        document.getElementById("result").innerHTML =
            `Predicted Scoring Average: ${result.scoring_average.toFixed(2)}`;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerHTML =
            "An error occurred while calculating the scoring average.";
    }
}
