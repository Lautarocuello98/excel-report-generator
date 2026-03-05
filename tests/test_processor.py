from src.processor import compute_kpis


def test_compute_kpis(sample_df):
    kpis = compute_kpis(sample_df)

    assert kpis["total_orders"] == 2
    assert kpis["total_units"] == 3
    assert kpis["total_revenue"] == 40.0  # 2*10 + 1*20
    assert kpis["total_cost"] == 24.0     # 2*6 + 1*12
    assert kpis["total_profit"] == 16.0