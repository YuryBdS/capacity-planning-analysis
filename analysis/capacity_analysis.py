from pathlib import Path
import math
import pandas as pd
import matplotlib.pyplot as plt


# Locate the dataset
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "operational_capacity.csv"


# Load data
df = pd.read_csv(DATA_FILE)

# Calculate operational metrics
df["daily_capacity"] = (
    df["analysts_available"] * df["productivity_target"]
)

df["capacity_gap"] = (
    df["daily_capacity"] - df["incoming_demand"]
)

df["backlog_reduction"] = (
    df["starting_backlog"] - df["ending_backlog"]
)


# Summary metrics
average_demand = df["incoming_demand"].mean()
average_capacity = df["daily_capacity"].mean()
average_gap = df["capacity_gap"].mean()
average_backlog_reduction = df["backlog_reduction"].mean()

productivity_per_analyst = df["productivity_target"].mean()

required_headcount = math.ceil(
    average_demand / productivity_per_analyst
)


# Display results
print("CAPACITY PLANNING SUMMARY")
print("-" * 30)

print(f"Average daily demand: {average_demand:.1f}")
print(f"Average daily capacity: {average_capacity:.1f}")
print(f"Average capacity gap: {average_gap:.1f}")
print(f"Average backlog reduction: {average_backlog_reduction:.1f}")
print(f"Required headcount: {required_headcount}")
# Demand growth scenarios
scenarios = {
    "Current": 0.00,
    "+10%": 0.10,
    "+20%": 0.20,
    "+30%": 0.30,
}

print("\nDEMAND SCENARIOS")
print("-" * 50)

for scenario_name, growth_rate in scenarios.items():
    scenario_demand = average_demand * (1 + growth_rate)

    scenario_gap = average_capacity - scenario_demand

    scenario_headcount = math.ceil(
        scenario_demand / productivity_per_analyst
    )

    status = "Sufficient" if scenario_gap >= 0 else "Insufficient"

    print(
        f"{scenario_name}: "
        f"Demand={scenario_demand:.1f} | "
        f"Capacity Gap={scenario_gap:.1f} | "
        f"Headcount={scenario_headcount} | "
        f"Status={status}"
    )
    # Generate demand scenario chart
scenario_names = []
scenario_demands = []

for scenario_name, growth_rate in scenarios.items():
    scenario_names.append(scenario_name)
    scenario_demands.append(average_demand * (1 + growth_rate))

output_dir = BASE_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

plt.figure(figsize=(8, 5))

plt.bar(scenario_names, scenario_demands)

plt.axhline(
    y=average_capacity,
    linestyle="--",
    label=f"Current Capacity ({average_capacity:.0f})"
)

plt.title("Demand Growth vs Current Capacity")
plt.xlabel("Demand Scenario")
plt.ylabel("Activities per Day")
plt.legend()

plt.tight_layout()

plt.savefig(
    output_dir / "demand_scenarios.png",
    dpi=150
)

plt.close()

print("\nChart generated: outputs/demand_scenarios.png")
