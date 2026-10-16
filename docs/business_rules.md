# Business Rules

This document defines the decision logic used in the capacity planning analysis.

## 1. Daily Capacity

Daily operational capacity is calculated as:

`Analysts Available × Productivity Target`

Example:

`5 analysts × 35 activities = 175 activities/day`

## 2. Capacity Gap

Capacity gap measures the difference between available capacity and incoming demand.

`Daily Capacity - Incoming Demand`

Decision:

- If the result is positive, the operation has available capacity.
- If the result is zero, capacity and demand are balanced.
- If the result is negative, demand exceeds available capacity.

## 3. Backlog Evolution

Backlog changes according to the difference between incoming demand and completed activities.

`Ending Backlog = Starting Backlog + Incoming Demand - Completed Activities`

## 4. Backlog Reduction

Backlog is reduced when:

`Completed Activities > Incoming Demand`

The difference represents the daily backlog burn rate.

## 5. Required Headcount

Required headcount is calculated as:

`Incoming Demand ÷ Productivity per Analyst`

When the result is not a whole number, it should be rounded up.

Example:

`180 activities ÷ 35 = 5.14`

Required headcount:

`6 analysts`

## 6. Demand Scenarios

The analysis evaluates the current operation under the following scenarios:

- Current demand
- Demand +10%
- Demand +20%
- Demand +30%

The objective is to identify when the current team structure becomes insufficient.
