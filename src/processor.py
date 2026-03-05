from __future__ import annotations

import pandas as pd


def compute_kpis(df: pd.DataFrame) -> dict:
    """
    Compute core KPIs from cleaned sales data.

    Adds computed columns:
    - revenue, cost, profit, margin_pct
    """
    out = df.copy()

    out["revenue"] = out["quantity"] * out["unit_price"]
    out["cost"] = out["quantity"] * out["unit_cost"]
    out["profit"] = out["revenue"] - out["cost"]
    out["margin_pct"] = out.apply(
        lambda r: (r["profit"] / r["revenue"] * 100) if r["revenue"] else 0.0,
        axis=1,
    )

    total_orders = int(len(out))
    total_units = float(out["quantity"].sum())
    total_revenue = float(out["revenue"].sum())
    total_cost = float(out["cost"].sum())
    total_profit = float(out["profit"].sum())
    avg_order_value = float(total_revenue / total_orders) if total_orders else 0.0

    top_products = (
        out.groupby("product", dropna=False)["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    return {
        "total_orders": total_orders,
        "total_units": total_units,
        "total_revenue": total_revenue,
        "total_cost": total_cost,
        "total_profit": total_profit,
        "avg_order_value": avg_order_value,
        "top_products": top_products,
        "df_with_calculations": out,
    }