import pandas as pd

from src.processor import compute_kpis


def test_compute_kpis(sample_df):
    kpis = compute_kpis(sample_df)

    assert kpis["total_orders"] == 2
    assert kpis["total_units"] == 3
    assert kpis["total_revenue"] == 40.0  # 2*10 + 1*20
    assert kpis["total_cost"] == 24.0     # 2*6 + 1*12
    assert kpis["total_profit"] == 16.0


def test_compute_kpis_margin_pct_handles_zero_revenue():
    df = pd.DataFrame(
        {
            "date": ["2026-01-01"],
            "sku": ["SKU-0"],
            "product": ["Free Sample"],
            "quantity": [2],
            "unit_price": [0],
            "unit_cost": [0],
        }
    )

    kpis = compute_kpis(df)
    df_out = kpis["df_with_calculations"]

    assert float(df_out.loc[0, "revenue"]) == 0.0
    assert float(df_out.loc[0, "margin_pct"]) == 0.0
