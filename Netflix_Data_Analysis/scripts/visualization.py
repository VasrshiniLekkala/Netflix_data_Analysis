import os
import pandas as pd
import matplotlib.pyplot as plt

# Try to import seaborn, but provide a lightweight fallback if it's not installed.
try:
    import seaborn as sns
except Exception:
    # Minimal seaborn-like API using matplotlib so the rest of the script works without seaborn.
    class _FallbackSNS:
        @staticmethod
        def countplot(x, data=None, ax=None):
            if data is None:
                raise ValueError("data is required for countplot fallback")
            counts = data[x].value_counts()
            ax = ax or plt.gca()
            ax.bar(counts.index.astype(str), counts.values)
            ax.set_xlabel(x)
            ax.set_ylabel("count")
            for label in ax.get_xticklabels():
                label.set_rotation(45)

        @staticmethod
        def barplot(x=None, y=None, data=None, ax=None):
            # Expectation in this script: x -> values, y -> labels (e.g. x=top.values, y=top.index)
            if x is None or y is None:
                raise ValueError("x and y are required for barplot fallback")
            ax = ax or plt.gca()
            ax.barh([str(label) for label in y], x)

    sns = _FallbackSNS()
    print("⚠️ seaborn not available; using fallback matplotlib-based plotting helpers")

# ✅ Automatically create charts folder based on absolute path
