import subprocess

def monitor_kpis():
    kpis = {}
    devices = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

    for device in devices:
        result = subprocess.run(["ping", "-c", "4", device], stdout=subprocess.PIPE, text=True)
        latency = result.stdout.split("time=")[-1].split(" ms")[0]
        kpis[device] = {"latency": latency}
    return kpis
