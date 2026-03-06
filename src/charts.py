from __future__ import annotations

from pathlib import Path

import matplotlib
import pandas as pd

# Use a non-interactive backend so chart generation works in CI/headless environments.
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def build_charts(df_clean: pd.DataFrame, kpis: dict, charts_dir: Path) -> list[Path]:
    charts_dir.mkdir(parents=True, exist_ok=True)

    chart_files: list[Path] = []

    # 1) Revenue by day
    if "date" in df_clean.columns and not df_clean["date"].isna().all():
        chart_df = df_clean.assign(
            date=pd.to_datetime(df_clean["date"], errors="coerce"),
            revenue=df_clean["quantity"] * df_clean["unit_price"],
        ).dropna(subset=["date"])
        by_day = chart_df.groupby(chart_df["date"].dt.date)["revenue"].sum().sort_index()
        if not by_day.empty:
            p = charts_dir / "revenue_by_day.png"
            plt.figure(figsize=(8, 4))
            plt.plot(list(by_day.index), list(by_day.values))
            plt.title("Revenue by Day")
            plt.xlabel("Date")
            plt.ylabel("Revenue")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.savefig(p, dpi=150)
            plt.close()
            chart_files.append(p)

    # 2) Top products by revenue
    top = kpis.get("top_products")
    if top is not None and len(top) > 0:
        p = charts_dir / "top_products.png"
        plt.figure(figsize=(8, 4))
        plt.bar(top["product"].astype(str), top["revenue"])
        plt.title("Top Products by Revenue")
        plt.xlabel("Product")
        plt.ylabel("Revenue")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(p, dpi=150)
        plt.close()
        chart_files.append(p)

    return chart_files
