from src.cleaner import clean_sales_df


def test_clean_sales_df_basic(sample_df):
    config = {"cleaning": {"drop_duplicates": True, "fill_missing_numeric_with_zero": True}}
    cleaned, summary = clean_sales_df(sample_df, config=config)

    assert len(cleaned) == 2
    assert "bad_dates_coerced_to_na" in summary
    assert cleaned["quantity"].sum() == 3