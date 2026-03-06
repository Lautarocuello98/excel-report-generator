from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

def _normalize_col(col: str) -> str:
    return (
        str(col)
        .strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
    )


def _apply_column_mapping(df: pd.DataFrame, config: dict[str, Any]) -> pd.DataFrame:
    mapping = config.get("input", {}).get("column_mapping", {})
    normalized_cols = {_normalize_col(c): c for c in df.columns}  # normalized -> original

    rename: dict[str, str] = {}
    for target, candidates in mapping.items():
        for cand in candidates:
            cand_norm = _normalize_col(cand)
            if cand_norm in normalized_cols:
                rename[normalized_cols[cand_norm]] = target
                break

    df = df.rename(columns=rename)
    df.columns = [_normalize_col(c) for c in df.columns]
    return df


def _load_one_file(path: Path, config: dict[str, Any]) -> pd.DataFrame:
    ext = path.suffix.lower()
    if ext == ".csv":
        df = pd.read_csv(path)
    elif ext in {".xlsx", ".xls"}:
        df = pd.read_excel(path)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

    df = _apply_column_mapping(df, config)
    return df


def load_input(input_path: Path, config: dict[str, Any]) -> tuple[pd.DataFrame, list[str]]:
    """
    Load a single file or a folder of files into a unified DataFrame.

    Supported: CSV, XLSX, XLS
    Returns: (df, sources)
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Input not found: {input_path}")

    supported = set(config.get("input", {}).get("supported_extensions", [".csv", ".xlsx", ".xls"]))

    files: list[Path] = []
    if input_path.is_dir():
        for p in sorted(input_path.rglob("*")):
            if p.is_file() and p.suffix.lower() in supported:
                files.append(p)
    else:
        if input_path.suffix.lower() not in supported:
            raise ValueError(f"Unsupported file extension: {input_path.suffix}")
        files = [input_path]

    if not files:
        raise ValueError(f"No supported files found in: {input_path}")

    dfs: list[pd.DataFrame] = []
    sources: list[str] = []
    for f in files:
        df = _load_one_file(f, config)
        df["source_file"] = f.name
        dfs.append(df)
        sources.append(str(f))

    merged = pd.concat(dfs, ignore_index=True)
    return merged, sources
