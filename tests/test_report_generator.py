from pathlib import Path

from src.processor import compute_kpis
from src.report_generator import generate_excel_report


def test_generate_excel_report_creates_file(tmp_path: Path, sample_df):
    kpis = compute_kpis(sample_df)
    out = tmp_path / "out.xlsx"

    generate_excel_report(
        report_path=out,
        df_clean=sample_df,
        kpis=kpis,
        currency="USD",
        sources=["sample.csv"],
        chart_files=[],
    )

    assert out.exists()
    assert out.stat().st_size > 0