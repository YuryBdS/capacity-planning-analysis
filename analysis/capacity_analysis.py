from pathlib import Path
import math
import pandas as pd


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
