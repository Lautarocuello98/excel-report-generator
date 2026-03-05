import json
from pathlib import Path

import pandas as pd

from src.loader import load_input


def test_load_input_csv(tmp_path: Path):
    f = tmp_path / "sales.csv"
    f.write_text(
        "date,sku,product,quantity,unit_price,unit_cost\n"
        "2026-01-01,SKU1,Widget,2,10,6\n",
        encoding="utf-8",
    )

    config = json.loads(
        """
        {
          "input": {
            "supported_extensions": [".csv", ".xlsx", ".xls"],
            "column_mapping": {
              "date": ["date"],
              "sku": ["sku"],
              "product": ["product"],
              "quantity": ["quantity"],
              "unit_price": ["unit_price"],
              "unit_cost": ["unit_cost"]
            }
          }
        }
        """
    )

    df, sources = load_input(f, config=config)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert len(sources) == 1
    assert "source_file" in df.columns