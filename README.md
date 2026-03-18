# COVID-19 Mortality Analysis in 
United States (2020–2023)

## Overview
Analysis of COVID-19 mortality data from the CDC, exploring trends by age group, 
sex, state, and year across the United States from 2020 to 2023.

## Dataset
- **Source:** Centers for Disease Control and Prevention (CDC)
- **Records:** 137,700 rows (4,752 after cleaning)
- **Variables:** Deaths by COVID-19, Pneumonia, and Influenza disaggregated 
by state, sex, age group, and year

## Tools Used
- **Python (pandas)** — Data cleaning and transformation
- **Power BI** — Data visualization and interactive dashboard

## Data Cleaning (Python)
- Filtered to annual aggregates only (removed monthly and cumulative totals)
- Removed aggregate rows (All Sexes, All Ages)
- Selected non-overlapping age groups
- Handled suppressed values (<10 deaths) by filling with 0

## Key Findings
- COVID-19 mortality increased sharply from 2020 to 2021, then declined 
through 2023 following vaccine rollout
- Males had higher mortality than females across all age groups except 85+
- Mortality risk increased exponentially with age — over 60% of all deaths 
occurred in patients aged 65 and over
- California, Texas, and Florida recorded the highest absolute death counts, 
consistent with their population size
- At its peak in 2021, COVID-19 accounted for approximately 15% of all deaths 
in the United States

## Interactive Dashboard
Explore the full interactive dashboard here:
[Power BI Dashboard](https://app.powerbi.com/groups/me/reports/f985cdb2-0974-48f7-a0c2-8a1dda4e1df4?pbi_source=desktop)

## Files
- `analysis.py` — Data cleaning and analysis script
- `data/covid_limpio.csv` — Cleaned dataset
- `covid_analysis.pbix` — Power BI report file
