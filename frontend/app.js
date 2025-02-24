async function fetchKPIs() {
    const response = await fetch('/kpis');
    const data = await response.json();
    document.getElementById('kpi-container').innerText = JSON.stringify(data, null, 2);
}

async function triggerReconfiguration() {
    const response = await fetch('/reconfigure', { method: 'POST' });
    const result = await response.json();
    alert(result.message);
}

fetchKPIs();
