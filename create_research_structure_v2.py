import os
from pathlib import Path

def create_file(path: Path, content: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")

def main():
    base = Path(".")

    # --- Thư mục chính ---
    dirs = [
        "config",
        "data/raw/binance/klines",
        "data/interim/cleaned",
        "data/interim/features",
        "data/processed/regimes",
        "data/processed/panels",
        "data/processed/optimization",
        "docs",
        "notebooks/cycle_analysis",
        "notebooks/portfolio_optimization",
        "reports/figures/cycle_analysis",
        "reports/figures/portfolio_optimization",
        "reports/artifacts/cycle_analysis",
        "reports/artifacts/portfolio_optimization",
        "tests",
        # src/common
        "src/common/utils",
        "src/common/cli",
        # src/cycle_analysis
        "src/cycle_analysis/data",
        "src/cycle_analysis/features",
        "src/cycle_analysis/labeling",
        "src/cycle_analysis/models",
        "src/cycle_analysis/evaluation",
        # src/portfolio_optimization
        "src/portfolio_optimization/estimation",
        "src/portfolio_optimization/optimization",
        "src/portfolio_optimization/policy",
        "src/portfolio_optimization/backtest",
        "src/portfolio_optimization/evaluation",
        # src/experiments
        "src/experiments",
    ]

    # --- File cơ bản ---
    files = {
        "README.md": "# 🪙 Crypto Cycle Portfolio Optimization\nMaster’s thesis project on detecting crypto market cycles and optimizing portfolios adaptively.",
        "LICENSE": "MIT License",
        ".gitignore": "__pycache__/\n.ipynb_checkpoints/\ndata/raw/\nreports/artifacts/\n",
        "requirements.txt": "\n".join([
            "pandas", "numpy", "scipy", "matplotlib", "seaborn",
            "scikit-learn", "hmmlearn", "ruptures", "arch",
            "pywavelets", "cvxpy", "PyPortfolioOpt", "statsmodels",
            "tqdm", "loguru", "ccxt"
        ]),
        # Config files
        "config/project.yaml": "project_name: crypto-cycle-portfolio-optimization\nrandom_state: 42\ndata_path: ./data\n",
        "config/universe_top20.yaml": "as_of: '2025-09-30'\nbase_currency: 'USDT'\nsymbols: []\n",
        "config/labeling.yaml": "trend:\n  ma_long: 200\nadx:\n  threshold_trend: 22\nvol:\n  lookback: 20\n",
        "config/optimization.yaml": "rebalance: weekly\nconstraints:\n  long_only: true\n  w_max: 0.25\n",
        "config/backtest.yaml": "start_date: '2021-01-01'\nend_date: '2025-09-30'\nbenchmark: 'BTCUSDT'\n",
        # Docs
        "docs/00_overview.md": "# Research Overview\nThis project studies crypto market cycles and regime-aware portfolio optimization.",
        "docs/01_cycle_theory.md": "# Cycle Analysis Theory\nDescribe HP, BK, CF filters, HMM, MS-GARCH, Wavelet, etc.",
        "docs/02_regime_models.md": "# Regime Models\nMarkov switching, HMM, changepoint detection approaches.",
        "docs/03_portfolio_theory.md": "# Portfolio Optimization Theory\nMean-variance, Risk Parity, CVaR, Kelly, etc.",
        "docs/04_experiment_design.md": "# Experiment Design\nDescribe experiment pipeline and validation logic.",
        "docs/references.md": "# References\nList of papers and datasets used.",
        # Common utils
        "src/common/utils/io.py": "# Utility: IO helpers\n",
        "src/common/utils/stats.py": "# Utility: Statistical helpers\n",
        "src/common/utils/plotting.py": "# Utility: Plotting helpers\n",
        "src/common/utils/logging.py": "# Utility: Logging setup\n",
        "src/common/cli/fetch_data.py": "# CLI: Fetch Binance OHLCV data\n",
        "src/common/cli/build_features.py": "# CLI: Build feature sets\n",
        # Cycle Analysis
        "src/cycle_analysis/data/loader_binance.py": "# Load and standardize OHLCV data from Binance\n",
        "src/cycle_analysis/data/cleaners.py": "# Clean raw data, fix missing, timezone, anomalies\n",
        "src/cycle_analysis/features/trend_features.py": "# Compute MA, ADX, Kalman slope, etc.\n",
        "src/cycle_analysis/features/volatility_features.py": "# Compute realized vol, Parkinson, RS, etc.\n",
        "src/cycle_analysis/features/cycle_features.py": "# HP, BK, CF, Wavelet, and EMD cycle extraction\n",
        "src/cycle_analysis/labeling/rules_based.py": "# Label regimes via rule-based logic\n",
        "src/cycle_analysis/labeling/hmm_labeler.py": "# Label regimes using HMM or MS-AR\n",
        "src/cycle_analysis/labeling/hybrid_labeler.py": "# Combine rule-based seed with HMM smoothing\n",
        "src/cycle_analysis/models/hmm_model.py": "# Gaussian HMM for regime detection\n",
        "src/cycle_analysis/models/ms_ar_model.py": "# Markov Switching AR model\n",
        "src/cycle_analysis/models/garch_model.py": "# MS-GARCH volatility regime model\n",
        "src/cycle_analysis/models/changepoint_model.py": "# Changepoint detection using PELT / BOCPD\n",
        "src/cycle_analysis/evaluation/stability_tests.py": "# Check regime stability over time\n",
        "src/cycle_analysis/evaluation/transition_matrix.py": "# Compute transition probabilities\n",
        "src/cycle_analysis/evaluation/visualize_regimes.py": "# Visualize phase overlays on price\n",
        # Portfolio Optimization
        "src/portfolio_optimization/estimation/returns_covariance.py": "# Estimate conditional mean & covariance by regime\n",
        "src/portfolio_optimization/estimation/shrinkage.py": "# Shrinkage estimators (Ledoit-Wolf, Oracle)\n",
        "src/portfolio_optimization/optimization/mean_variance.py": "# Mean-Variance optimization\n",
        "src/portfolio_optimization/optimization/risk_parity.py": "# Risk Parity / Equal Risk Contribution optimization\n",
        "src/portfolio_optimization/optimization/cvar_optimization.py": "# CVaR optimization\n",
        "src/portfolio_optimization/optimization/kelly_fractional.py": "# Fractional Kelly optimization\n",
        "src/portfolio_optimization/optimization/black_litterman.py": "# Black–Litterman model\n",
        "src/portfolio_optimization/policy/regime_policy.py": "# Define regime-dependent allocation policies\n",
        "src/portfolio_optimization/policy/transition_blend.py": "# Blend allocations by regime probabilities\n",
        "src/portfolio_optimization/backtest/engine.py": "# Backtesting engine for multi-asset portfolios\n",
        "src/portfolio_optimization/backtest/reports.py": "# Generate performance and regime-aware reports\n",
        "src/portfolio_optimization/evaluation/performance_metrics.py": "# Compute Sharpe, Sortino, Calmar, etc.\n",
        "src/portfolio_optimization/evaluation/risk_analysis.py": "# Analyze drawdowns, tail risk, stability\n",
        "src/portfolio_optimization/evaluation/comparison_vs_static.py": "# Compare regime vs static portfolio performance\n",
        # Experiments
        "src/experiments/exp_cycle_detection.py": "# Run experiment: cycle detection methods\n",
        "src/experiments/exp_regime_stability.py": "# Run experiment: regime stability & transition\n",
        "src/experiments/exp_portfolio_static.py": "# Run experiment: static portfolio baseline\n",
        "src/experiments/exp_portfolio_regime_switch.py": "# Run experiment: regime-switching portfolio\n",
        "src/experiments/exp_backtest_full.py": "# Run full backtest end-to-end\n",
        # Notebooks (placeholders)
        "notebooks/cycle_analysis/01_data_ingest.ipynb": "",
        "notebooks/portfolio_optimization/07_conditional_moments.ipynb": "",
        # Tests
        "tests/test_cycle_features.py": "# Unit test: cycle feature extraction\n",
        "tests/test_regime_models.py": "# Unit test: regime modeling\n",
        "tests/test_moments_estimation.py": "# Unit test: moment estimation per regime\n",
        "tests/test_optimization_algorithms.py": "# Unit test: optimization methods\n",
        "tests/test_backtest_engine.py": "# Unit test: backtesting logic\n",
    }

    # --- Tạo thư mục & file ---
    for d in dirs:
        (base / d).mkdir(parents=True, exist_ok=True)
    for rel_path, content in files.items():
        create_file(base / rel_path, content)

    print(f"✅ Full research structure created at: {base.resolve()}")

if __name__ == "__main__":
    main()
