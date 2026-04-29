# India Export-Import Trade Analysis for Foreign Trade Policy (FTP) Support

## Objective
This project presents a structured analysis of India’s export-import data to derive insights supporting Foreign Trade Policy (FTP) formulation and trade facilitation. The focus is on data validation, trend analysis, and policy-oriented interpretation of trade patterns.

## Executive Summary
This analysis examines India’s export trends across commodities and countries to identify growth sectors, trade concentration, and dependencies. The findings provide insights relevant to policy formulation, sectoral support, and trade facilitation strategies.

## Why This Project Matters
Trade data analysis plays a crucial role in supporting government decision-making. This project demonstrates how structured data analysis can contribute to:
- Policy formulation
- Trade monitoring
- Sector performance evaluation
- Evidence-based decision making

## Key Policy Insights
- Export concentration in select commodities indicates the need for diversification under Foreign Trade Policy
- High-growth sectors reflect emerging global demand and require facilitation support
- Country-wise dependency suggests scope for market diversification
- Declining sectors highlight areas requiring policy attention
- Trade patterns indicate uneven distribution across commodities and regions

## Methodology
1. **Data Orchestration:** Generating synthetic but highly realistic international trade logs.
2. **Stringent Data Cleaning:** Implemented modular Python scripts to detect and rectify duplicates, null values, malformed categorical data, and sub-zero numeric anomalies.
3. **Validation Logging:** Automated the generation of a professional audit trail (`data_validation_log.txt`) ensuring complete transparency in the ETL process.
4. **Statistical Analysis:** Calculated YoY growth rates, market concentration metrics, and sectoral trajectories.
5. **Data Visualization:** Produced formal, executive-ready graphical assets tailored for government policy consumption.
6. **Insight Extraction:** Synthesized the data into high-impact, actionable policy observations.

## Tools Used
* **Python (Pandas, NumPy):** For rigorous ETL operations, data cleaning, and aggregation.
* **Matplotlib & Seaborn:** For producing formal, publication-ready data visualizations.
* **Markdown:** For structured, professional executive report generation.

## How to Run
Ensure you have Python 3.8+ installed. 

1. **Clone the repository and navigate to the root directory.**
2. **Install all necessary dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Execute the analysis pipeline:**
   ```bash
   python src/analysis.py
   ```

## Folder Structure
```text
.
├── data/
│   ├── raw_data.csv                # Ingested synthetic raw data with anomalies
│   └── cleaned_data.csv            # Processed, validated, and scrubbed data
├── reports/
│   ├── final_report.md             # Policy-oriented executive summary
│   └── data_validation_log.txt     # Audit log of data cleaning transformations
├── src/
│   ├── analysis.py                 # Core orchestration script
│   └── utils.py                    # Modular functions for generation, cleaning, & plotting
├── visuals/
│   ├── export_trends.png           # YoY macro trend visualization
│   └── top_commodities.png         # Bar chart for category aggregations
├── README.md                       # High-level project documentation
└── requirements.txt                # Python environment dependencies
```
