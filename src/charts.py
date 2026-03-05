from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def build_charts(df_clean: pd.DataFrame, kpis: dict, charts_dir: Path) -> list[Path]:
    charts_dir.mkdir(parents=True, exist_ok=True)

    chart_files: list[Path] = []

    # 1) Revenue by day
    if "date" in df_clean.columns and not df_clean["date"].isna().all():
        by_day = (
            df_clean.assign(revenue=df_clean["quantity"] * df_clean["unit_price"])
            .dropna(subset=["date"])
            .groupby(df_clean["date"].dt.date)["revenue"]
            .sum()
        )
        if not by_day.empty:
            p = charts_dir / "revenue_by_day.png"
            plt.figure()
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
        plt.figure()
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