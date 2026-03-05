# 📊 Data Report Automation

> A Python data processing and reporting tool that converts raw CSV/Excel files into cleaned datasets and professional Excel reports.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests: pytest](https://img.shields.io/badge/tests-pytest-green.svg)](#-running-tests)

---

## ✨ Overview

Data Report Automation is a **CLI-based automation tool** that:

- Loads **CSV / Excel** files from a file or folder
- Cleans and normalizes the data
- Computes key business KPIs
- Generates a professional **Excel report** (Summary + Cleaned Data + Top Products)
- Produces logs and optional charts

This project demonstrates:

- File automation and batch processing
- Data cleaning and normalization
- Report generation with Excel formatting
- CLI tooling, logging, and automated testing

---

## 🚀 Features

| Feature | Description |
|-------|-------------|
| Multi-file ingestion | Process a single file or an entire folder |
| Data cleaning | Deduplication, parsing, numeric normalization |
| KPI calculation | Revenue, cost, profit, AOV, top products |
| Excel reporting | Multiple sheets + formatted output |
| Charts | Optional PNG charts embedded in the report |
| Logging | Processing logs saved in the output folder |
| Tests | pytest suite validating core logic |

---

## 📦 Installation

### Requirements
- Python 3.10+
- pip

### Setup

```bash
git clone https://github.com/Lautarocuello98/data-report-automation.git
cd data-report-automation
python -m pip install -r requirements.txt