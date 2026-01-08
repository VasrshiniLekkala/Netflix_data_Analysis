
import pandas as pd

def generate_summary(df):
    summary = {
        "Total Titles": len(df),
        "Movies": (df['type'] == 'Movie').sum(),
        "TV Shows": (df['type'] == 'TV Show').sum(),
        "Unique Countries": df['country'].nunique(),
        "Unique Ratings": df['rating'].nunique()
    }
    summary_df = pd.DataFrame(summary, index=[0])
    summary_df.to_csv('../outputs/summary_report.csv', index=False)
    print("✅ Summary report saved successfully!")

if __name__ == "__main__":
    df = pd.read_csv('../data/netflix_titles.csv')
    generate_summary(df)
