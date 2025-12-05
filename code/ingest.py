import pandas as pd
import os
from pathlib import Path

def load_energy_data(data_dir="data"):
    combined = []

    for file in Path(data_dir).glob("*.csv"):
        try:
            df = pd.read_csv(file)
            df["building"] = file.stem       # add building name
            combined.append(df)
        except FileNotFoundError:
            print(f"Missing file: {file}")
        except pd.errors.ParserError:
            print(f"Corrupt data skipped: {file}")

    if not combined:
        raise ValueError("No valid files found")

    df_combined = pd.concat(combined, ignore_index=True)
    df_combined["timestamp"] = pd.to_datetime(df_combined["timestamp"])

    return df_combined
