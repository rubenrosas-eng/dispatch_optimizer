import csv
import json
from datetime import datetime
inventory_data = [
{"item_id": "PIPE-101", "weight_kg": 450.5, "priority": 1, "status": "READY"},
{"item_id": "PIPE-103", "weight_kg": 300.0, "priority": 2, "status": "HOLD"}
]
def optimize_dispatch(items, max_weight):
    ready_items = [i for i in items if i["status"] == "READY"]
    sorted_items = sorted(ready_items, key=lambda x: (x["priority"], -x["weight_kg"]))
    manifest = []
    total_weight = 0.0
    for item in sorted_items:
        if total_weight + item["weight_kg"] <= max_weight:
            manifest.append(item)
            total_weight += item["weight_kg"]
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_items": len(manifest),
        "total_weight_kg": round(total_weight, 2),
        "remaining_capacity_kg": round(max_weight - total_weight, 2),
        "manifest": manifest
    }
def save_reports(data):
    with open("dispatch_summary.json", "w") as f:
        json.dump(data, f, indent=4)
    with open("dispatch_manifest.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["item_id", "weight_kg", "priority", "status"])
        writer.writeheader()
        writer.writerows(data["manifest"])
if __name__ == "__main__":
    results = optimize_dispatch(inventory_data, 2500.0)
    save_reports(results)
    print(f"Despacho procesado: {results['total_items']} items ({results['total_weight_kg']} kg)")
