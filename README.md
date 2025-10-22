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

## 🧩 Project Structure
