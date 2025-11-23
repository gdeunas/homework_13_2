from pathlib import Path
from typing import Union

import pandas as pd


def read_csv(file_csv: Union[Path | str]) -> list[dict]:
    """функция для считывания финансовых операций из CSV."""
    try:
        df = pd.read_csv(file_csv, delimiter=";")
        # grouped_df = df.groupby('id').agg({})
        return df.to_dict(orient="records")
    except Exception as e:
        print(e)
        return []


def read_xl(file_xl: Union[Path | str]) -> list[dict]:
    """функция для считывания финансовых операций из Excel."""
    try:
        excel_data = pd.read_excel(file_xl)
        return excel_data.to_dict(orient="records")
    except Exception as e:
        print(e)
        return []
