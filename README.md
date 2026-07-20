# Currency Conversion Comparison

A simple comparison between two currency conversion paths — direct vs. indirect — using live exchange rates.

## Overview

This project answers a simple question: if you have an amount in Saudi Riyal or US Dollar and want to convert it to Egyptian Pound, is it better to convert directly, or to go through an intermediate currency first?

Specifically, the project compares:
- **Direct conversion:** Saudi Riyal (SAR) → Egyptian Pound (EGP)
- **Indirect conversion:** Saudi Riyal (SAR) → US Dollar (USD) → Egyptian Pound (EGP)

It then calculates the difference between the two paths as a percentage, to see whether that difference is large enough to matter, or small enough to ignore.

## Data Source

Exchange rates come from the [Frankfurter API](https://frankfurter.dev) — a free, open-source API that pulls rates from over 80 central banks worldwide, with no API key required.

## Libraries Used

- **`requests`** - the only library used in the project, for sending HTTP requests to fetch exchange rates from the API

## Requirements

- Python 3
- `requests` library

Install it with:
```bash
pip install requests
```

## How to Run

Run the script directly:
```bash
python currency_comparison.py
```

The script fetches current exchange rates automatically, calculates both conversion paths, and prints which one is better and by how much (as a percentage).

## Example Output

```
Indirect value as 13480.97 is bigger than direct value, It's 0.0% bigger
```

## Note

The difference between the two paths is usually very small (less than 1%), because official exchange rates stay consistent with each other (there's no "free profit" from reordering the conversion). This project demonstrates that in practice with real numbers.

## Next Steps

- Add logging instead of print statements
- Add simple data quality checks (null checks, duplicate checks)
- Containerize the project with Docker
