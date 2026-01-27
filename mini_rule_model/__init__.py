# Package exports and metadata

__version__ = "0.1.0"

from .simulator import run_simulation
from .evaluator import run_script
from .visualize import plot_variable
from .generator import generate_rules

__all__ = [
    "run_simulation",
    "run_script",
    "plot_variable",
    "generate_rules",
    "__version__",
]