from flask import Flask, jsonify, request
from monitor_kpis import monitor_kpis
from reconfigure_network import reconfigure
from logger import log_change

app = Flask(__name__)

@app.route('/kpis', methods=['GET'])
def get_kpis():
    kpis = monitor_kpis()
    log_change("Fetched KPI data")
    return jsonify(kpis)

@app.route('/reconfigure', methods=['POST'])
def trigger_reconfiguration():
    link = request.json.get('link')
    result = reconfigure(link)
    log_change(f"Reconfigured link {link}")
    return jsonify({"status": "success", "message": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
