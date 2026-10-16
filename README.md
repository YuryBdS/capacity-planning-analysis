# Capacity Planning Analysis

Operational capacity planning case focused on workload, productivity, backlog and resource sizing.

## Business Problem

Operational teams need to balance incoming workload with available capacity.

When demand exceeds capacity, backlog grows, service levels may be affected and additional resources may be required.

This project demonstrates a structured approach to capacity planning using operational data and decision rules.

## Scenario

The analysis is based on a fictional operation with:

- 5 analysts
- Productivity target of 35 activities per analyst/day
- Daily operational demand
- Existing backlog
- Business-day capacity
- Different demand growth scenarios

All data used in this project is synthetic and created exclusively for portfolio purposes.

## Key Questions

This analysis aims to answer:

- What is the current daily operational capacity?
- Is the current team able to absorb incoming demand?
- How long would it take to eliminate the backlog?
- What happens if demand increases?
- How many analysts would be required under different scenarios?

## Key Metrics

The analysis will consider:

- Daily Capacity
- Average Daily Demand
- Capacity Gap
- Backlog
- Backlog Burn Rate
- Estimated Backlog Clearance Time
- Required Headcount

## Decision Logic

The basic capacity model follows:

**Daily Capacity**

`Number of Analysts × Productivity per Analyst`

**Capacity Gap**

`Daily Capacity - Daily Demand`

If the result is positive, the operation has capacity available to reduce backlog.

If the result is negative, backlog tends to increase.

## Demand Scenarios

The project will evaluate:

- Current Demand
- +10% Demand
- +20% Demand
- +30% Demand

The goal is to understand when the current structure becomes insufficient and when additional resources are required.

## Project Structure

```text
capacity-planning-analysis/
│
├── README.md
├── data/
│   └── operational_capacity.csv
│
├── analysis/
│   └── capacity_analysis.ipynb
│
└── docs/
    └── business_rules.md
