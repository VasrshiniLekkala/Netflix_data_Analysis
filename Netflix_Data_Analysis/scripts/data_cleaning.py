
import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)
    
    # Drop duplicates
    df.drop_duplicates(inplace=True)
    
    # Fill missing values with placeholders
    df['country'].fillna('Unknown', inplace=True)
    df['rating'].fillna('Not Rated', inplace=True)
    
    return df

if __name__ == "__main__":
    df = load_and_clean_data('../data/netflix_titles.csv')
    print("✅ Data loaded and cleaned successfully!")
    print(df.shape)
