# crypto-cycle-portfolio-optimization
Quantitative research project on crypto market cycle detection and portfolio optimization — identifying bull/bear/sideways regimes and adapting allocations accordingly.


# 🪙 Crypto Cycle Portfolio Optimization
> Master's thesis project — “Tối ưu hóa danh mục đầu tư tiền điện tử dựa trên phân tích chu kỳ”.

---

## 🎯 Overview
This repository contains the full research workflow for analyzing **market cycles** (bull / bear / sideways phases) and using that knowledge to **optimize crypto portfolios**.  
The study focuses on the **Top 20 cryptocurrencies by market capitalization**, using **daily OHLCV data from Binance** up to **30 September 2025**.

The project is divided into two main parts:

### 1️⃣ Cycle Analysis
- Detects and classifies **market regimes** using both **rule-based** and **statistical models**.  
- Methods include:
  - Trend & volatility indicators (MA slope, ADX, realized volatility)
  - Hodrick–Prescott (HP), Baxter–King (BK), Christiano–Fitzgerald (CF) filters
  - Wavelet and Hilbert–Huang (EMD) spectral decomposition
  - Hidden Markov Models (HMM) and Markov-Switching AR/GARCH

### 2️⃣ Portfolio Optimization
- Builds **regime-aware portfolio strategies** using estimated conditional moments (μ, Σ) from each phase.
- Implements multiple optimization frameworks:
  - Mean-Variance (Markowitz)
  - Risk Parity / Equal Risk Contribution
  - Conditional Value-at-Risk (CVaR)
  - Regime-switching allocation policy based on transition probabilities

---

##  Project Structure
crypto-cycle-portfolio-optimization/
├─ config/ # YAML configuration files
├─ data/ # raw, interim, and processed data (OHLCV, features, regimes)
├─ docs/ # theory and documentation
├─ notebooks/ # Jupyter notebooks for EDA and modeling
├─ src/ # core source code (data, features, regimes, optimization, backtest)
├─ reports/ # generated reports and visualizations
└─ tests/ # unit tests




---

## ⚙️ Tech Stack
- **Python 3.11+**
- **ccxt / yfinance** – data acquisition  
- **pandas / numpy / scipy** – preprocessing & features  
- **hmmlearn / ruptures / arch / pywavelets** – regime detection  
- **cvxpy / PyPortfolioOpt** – portfolio optimization  
- **matplotlib / seaborn / plotly** – visualization  
- **tqdm / loguru** – workflow and logging

---

## 🚀 Quick Start

# Clone repository
git clone https://github.com/<your-username>/crypto-cycle-portfolio-optimization.git
cd crypto-cycle-portfolio-optimization

# Install dependencies
pip install -r requirements.txt

# Run initial data fetch & processing
python -m src.cli.fetch_data --config config/exchanges.yaml
python -m src.cli.build_features
python -m src.cli.label_regimes
python -m src.cli.optimize_portfolio
python -m src.cli.run_backtest



📖 Research Goals

Build a robust cycle detection framework for the cryptocurrency market.

Quantify how returns and volatility differ across regimes.

Design adaptive portfolio strategies that shift allocations according to the detected phase.

Evaluate risk-adjusted performance improvements vs static portfolios.

📚 References

Hamilton, J.D. (1989). A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle.

Baxter & King (1999). Measuring Business Cycles: Approximate Band-Pass Filters.

Christiano & Fitzgerald (2003). The Band Pass Filter.

Huang et al. (1998). The Empirical Mode Decomposition and the Hilbert Spectrum.

Ledoit & Wolf (2004). Honey, I Shrunk the Sample Covariance Matrix.

Author: Luong Thi Giang
Affiliation: 
Supervisor: 
Date: October 2025
