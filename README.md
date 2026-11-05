# dispatch_optimizer
An automated Python solution designed to optimize industrial inventory allocation for freight transport. The script filters available items, prioritizes urgent deliveries based on priority level and weight, and exports automated shipping manifests in JSON and CSV formats.
- Automated Filtering: Processes only inventory items with `READY` status.
- Algorithmic Prioritization: Sorts by urgency level (`priority`) and maximizes payload efficiency by weight (`weight_kg`).
- Load Capacity Constraints: Enforces configurable vehicle weight limits (default: 2,500 kg).
- Dual Format Export:
  - `dispatch_summary.json`: Structured operational summary with timestamps and key payload metrics.
  - `dispatch_manifest.csv`: Clean tabular manifest ready for ERP system integration.

## 🛠️ Tech Stack

- **Python 3.x**
- Standard Libraries: `csv`, `json`, `datetime`
