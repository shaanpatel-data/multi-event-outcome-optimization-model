"""
Configuration module for the parlay optimization project.

Contains constants for directory paths and environment variables.
"""

import os
from pathlib import Path

# Base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Reports directory
REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Notebooks directory
NOTEBOOKS_DIR = BASE_DIR / "notebooks"

# Environment variables
ODDS_API_KEY = os.getenv("ODDS_API_KEY", "your_default_key")

# Add other environment variables as needed
