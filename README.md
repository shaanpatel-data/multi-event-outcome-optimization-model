# Multi-Event Outcome Optimization Model

This repository contains a data‑driven sports analytics project that explores how to optimize multi‑leg outcomes across sporting events by evaluating probabilities and expected values.  The goal is to apply rigorous statistical methods to identify profitable combinations (parlays) in a research context—not to provide gambling advice.  By modelling individual game probabilities, converting bookmaker odds to implied probabilities, and calculating the expected value of combined outcomes, the model helps illustrate how pricing inefficiencies can compound across legs and which groupings merit further analysis.

## Features

- **Probability modelling:** Build probabilistic models (e.g., logistic regression) to estimate the likelihood of individual game outcomes based on historical data and current information.
- **Expected value calculation:** Convert American odds into implied probabilities, compute the expected value (EV) for each selection, and aggregate EV across multiple legs.
- **Parlay optimization:** Enumerate combinations of outcomes, filter out correlated legs (e.g., same‑game picks), and rank parlays by joint probability and expected value.
- **Modular codebase:** Structured into packages (`src/optimizer`, `src/models`, `src/utils`) with clear separation of concerns and docstrings.
- **Reproducible scripts:** Command‑line scripts in the `scripts/` folder for data acquisition, model training, and parlay generation.
- **Extensible tests:** Placeholder unit tests in the `tests/` directory that demonstrate how to validate key functionality with `pytest`.

## Directory Structure

```
├── data/
│   ├── raw/              # Raw data (not committed) – historical game results, betting lines, etc.
│   ├── interim/          # Intermediate data created during processing
│   └── processed/        # Final cleaned datasets used for modelling
├── notebooks/            # Jupyter notebooks for exploratory data analysis and research
├── reports/
│   ├── figures/          # Plots and figures generated from notebooks or scripts
│   └── …                 # Additional reports or markdown summaries
├── scripts/
│   ├── download_games.py             # Download historical and current game data into data/raw
│   ├── generate_parlay.py            # Produce optimized parlay combinations from probability estimates
│   ├── train_probability_model.py    # Train probability models on processed features
│   └── evaluate_parlay_strategies.py # Evaluate parlay performance over historical seasons
├── src/
│   ├── __init__.py
│   ├── config.py                     # Centralized configuration for paths and environment variables
│   ├── optimizer/
│   │   ├── __init__.py
│   │   └── multi_leg_optimizer.py    # Logic for EV computation and parlay optimization
│   ├── models/
│   │   ├── __init__.py
│   │   └── probability_model.py      # Probability model implementation (e.g., logistic regression)
│   └── utils/
│       ├── __init__.py
│       └── data_loader.py            # Utility functions for loading and saving data
├── tests/
│   ├── __init__.py
│   ├── test_multi_leg_optimizer.py   # Unit tests for parlay optimizer
│   └── test_probability_model.py     # Unit tests for probability model
├── .env.example          # Template for environment variables (copy to .env and fill in your API keys)
├── .gitignore            # Specifies intentionally untracked files (e.g., .env, data)
├── LICENSE
└── README.md
```

## Getting Started

1. **Clone the repository**:

```bash
git clone https://github.com/shaanpatel-data/parlay-optimization-model.git
cd parlay-optimization-model
```

2. **Create a virtual environment and install dependencies**:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\\Scripts\\activate`
pip install -r requirements.txt
```

The `requirements.txt` should include common data‑science libraries such as `pandas`, `numpy`, and `scikit-learn`.  Adjust as needed based on your environment.

3. **Set up environment variables**:

Copy `.env.example` to `.env` and replace placeholder values with your actual API keys and other secrets.  Do **not** commit your `.env` file.

```bash
cp .env.example .env
# Edit .env to add ODDS_API_KEY and any other variables
```

4. **Acquire data**:

Use the provided script to download historical game data and betting lines into `data/raw`:

```bash
python scripts/download_games.py --sport nba --season 2025
```

Replace the sport and season as required.  You can preprocess the raw data into `data/processed` using your own workflows or notebooks.

5. **Train a probability model**:

```bash
python scripts/train_probability_model.py \
    --input data/processed/model_features.csv \
    --output models/probability_model.pkl
```

This script loads cleaned features, trains a logistic regression model, and saves the trained model to the `models/` directory.

6. **Generate optimal parlays**:

```bash
python scripts/generate_parlay.py \
    --probabilities data/processed/model_probs.csv \
    --max-legs 3 \
    --top-k 10
```

This command loads probability estimates, enumerates multi‑leg combinations, filters out correlated legs, computes joint expected values, and prints the top‑10 parlays by EV.  Adjust `max-legs` and `top-k` for deeper searches.

## Methodology

The parlay optimizer follows these general steps:

1. **Probability estimation** – Each candidate event or selection (e.g., team to win, over/under) is assigned a model probability using historical data and contextual features.  The provided `ProbabilityModel` in `src/models/probability_model.py` implements a basic logistic regression approach, but you can substitute any probabilistic model (e.g., gradient boosting, Bayesian models).

2. **Odds conversion** – Bookmaker odds in American format are converted to implied probabilities.  This allows direct comparison between model probabilities and market probabilities.

3. **Expected value (EV) calculation** – For each selection, the expected value is computed as:

\( EV = p \times (o - 1) - (1 - p) \),

where \( p \) is the model probability and \( o \) is the decimal odds equivalent.  A positive EV indicates potential pricing inefficiency.
4. **Parlay enumeration** – The optimizer enumerates combinations of selections up to a specified number of legs.  It skips combinations that include multiple legs from the same game (to reduce correlation) or that have negative individual EV.

5. **Joint metrics** – For each parlay, the joint probability is the product of individual probabilities (assuming independence), and the joint EV is computed accordingly.  Parlays are ranked by EV and filtered to those meeting a minimum threshold.

This approach demonstrates how quantitative analysis can uncover favourable multi‑outcome opportunities.  It should be used for academic or research purposes and not as betting advice.

## Testing

Basic unit tests are included in the `tests/` directory.  To run the tests:

```bash
pip install pytest
pytest tests
```

These tests are placeholders illustrating how to structure tests for your models and optimizers.  Expanding test coverage is encouraged for production applications.

## Contributing

Contributions are welcome!  If you have ideas for improving the optimization logic, adding more sophisticated probability models, or integrating new data sources, feel free to open an issue or submit a pull request.  Please ensure that any contributions adhere to the project’s focus on research and analysis.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


