import pandas as pd
import os
import utils

def main():
    print("Initiating Trade Policy Data Analysis Pipeline...")
    
    # Setup Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    RAW_DATA_PATH = os.path.join(BASE_DIR, 'data', 'raw_data.csv')
    CLEAN_DATA_PATH = os.path.join(BASE_DIR, 'data', 'cleaned_data.csv')
    VAL_LOG_PATH = os.path.join(BASE_DIR, 'reports', 'data_validation_log.txt')
    COMMODITY_PLOT_PATH = os.path.join(BASE_DIR, 'visuals', 'top_commodities.png')
    TREND_PLOT_PATH = os.path.join(BASE_DIR, 'visuals', 'export_trends.png')
    
    # 1. Data Generation
    print(f"[*] Generating synthetic raw trade data -> {RAW_DATA_PATH}")
    utils.generate_synthetic_data(RAW_DATA_PATH, num_rows=1000)
    
    # 2. Data Cleaning
    print("[*] Loading raw data and initiating data cleaning protocols...")
    df_raw = pd.read_csv(RAW_DATA_PATH)
    df_clean, stats = utils.clean_data(df_raw)
    
    os.makedirs(os.path.dirname(CLEAN_DATA_PATH), exist_ok=True)
    df_clean.to_csv(CLEAN_DATA_PATH, index=False)
    print(f"[*] Clean data exported successfully -> {CLEAN_DATA_PATH}")
    
    # 3. Validation Logging
    print(f"[*] Compiling robust validation audit log -> {VAL_LOG_PATH}")
    utils.generate_validation_log(VAL_LOG_PATH, stats)
    
    # 4. Visualization Generation
    print("[*] Generating strategic visualizations for report inclusion...")
    utils.plot_top_commodities(df_clean, COMMODITY_PLOT_PATH)
    utils.plot_export_trends(df_clean, TREND_PLOT_PATH)
    
    # 5. Pipeline Summary
    total_value = df_clean['VALUE'].sum()
    print("\n=============================================")
    print("       PIPELINE EXECUTION COMPLETE           ")
    print("=============================================")
    print(f"Validated Records Analyzed: {stats['final_count']}")
    print(f"Total Export Value Indexed: ${total_value:,.2f}M")
    print("Output available in /data, /reports, and /visuals.")

if __name__ == "__main__":
    main()
