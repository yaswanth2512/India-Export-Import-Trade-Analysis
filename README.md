# India Export-Import Trade Analysis for Foreign Trade Policy (FTP) Support

## Objective
This project analyzes India’s export-import datasets to derive structured insights supporting Foreign Trade Policy (FTP) formulation and trade facilitation. It focuses on data validation, trend analysis, and policy-oriented interpretation of trade flows.

## Executive Summary
This project presents a structured analysis of India’s export trends across commodities and countries. The findings highlight concentration patterns, growth sectors, and trade dependencies that can inform Foreign Trade Policy decisions and trade facilitation strategies.

## Why This Project Matters
International trade data plays a critical role in government decision-making. This project demonstrates how structured data analysis can support:
- Policy formulation
- Trade monitoring
- Sector performance evaluation
- Evidence-based decision making

## Key Policy Insights
- Export concentration in limited commodities indicates potential need for diversification under Foreign Trade Policy (FTP)
- High-growth sectors reflect emerging global demand trends requiring trade facilitation support
- Country-wise dependency suggests scope for market diversification strategies
- Declining sectors highlight areas requiring policy intervention
- Trade patterns indicate uneven distribution across sectors

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
