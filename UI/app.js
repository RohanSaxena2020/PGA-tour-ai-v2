function calculateScoringAverage() {
    const sgOTT = parseFloat(document.getElementById('sg_ott').value);
    const sgAPP = parseFloat(document.getElementById('sg_app').value);
    const sgATG = parseFloat(document.getElementById('sg_atg').value);
    const sgPutting = parseFloat(document.getElementById('sg_putting').value);
    const birdieAvg = parseFloat(document.getElementById('birdie_avg').value);
    const drivingDistYds = parseFloat(document.getElementById('driving_dist_yds').value);
    const girPct = parseFloat(document.getElementById('gir_pct').value);

    const data = {
        sg_ott: sgOTT,
        sg_app: sgAPP,
        sg_atg: sgATG,
        sg_putting: sgPutting,
        birdie_avg: birdieAvg,
        driving_dist_yds: drivingDistYds,
        gir_pct: girPct
    };

    fetch('http://localhost:8000/predict/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Predicted Scoring Average: ${data.scoring_average}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Failed to retrieve prediction.';
    });
}