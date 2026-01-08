import os
import pandas as pd

# 🔹 Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '../../data/netflix_titles.csv')  # ✅ fixed path
OUTPUT_PATH = os.path.join(BASE_DIR, '../summary_report.csv')

# 🔹 Create output folder if missing
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# 🔹 Load dataset
df = pd.read_csv(DATA_PATH)

# 🔹 Basic cleaning
df.drop_duplicates(inplace=True)
df.dropna(subset=['type', 'country', 'release_year'], inplace=True)

# 🔹 Generate summary
summary = {
    "Total Titles": len(df),
    "Total Movies": len(df[df['type'] == 'Movie']),
    "Total TV Shows": len(df[df['type'] == 'TV Show']),
    "Oldest Release Year": int(df['release_year'].min()),
    "Newest Release Year": int(df['release_year'].max()),
    "Top Country": df['country'].value_counts().idxmax(),
    "Top Director": df['director'].value_counts().idxmax() if 'director' in df.columns else "N/A"
}

# 🔹 Convert to DataFrame for saving
summary_df = pd.DataFrame(list(summary.items()), columns=['Metric', 'Value'])
summary_df.to_csv(OUTPUT_PATH, index=False)

# 🔹 Print confirmation
print("✅ Summary report created successfully!")
print(f"📁 Saved at: {OUTPUT_PATH}")


import matplotlib.pyplot as plt

# 🔹 Count how many Movies vs TV Shows
type_counts = df['type'].value_counts()

# 🔹 Plot
plt.figure(figsize=(6,4))
type_counts.plot(kind='bar', color=['tomato', 'skyblue'])

# 🔹 Customize chart
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()

# 🔹 Save chart image
chart_path = os.path.join(BASE_DIR, 'movies_vs_shows.png')
plt.savefig(chart_path)

print(f"📊 Chart saved successfully at: {chart_path}")
plt.show()
