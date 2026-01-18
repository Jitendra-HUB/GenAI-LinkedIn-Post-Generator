import json 
import pandas as pd

class PrepareData:

    def __init__(self, filepath='processed_data.json'):
        # self.df= None
        # self.unique_tags= None
        self.load_posts(filepath)

    def load_posts(self, filepath):
        with open(filepath, encoding='utf-8') as f:
            posts=json.load(f)
            df=pd.json_normalize(posts)
            df['Length']=df['line_count'].apply(self.category_length)
            all_tags=df['tags'].apply(lambda x: x).sum()
            self.unique_tags= set(list(all_tags))
            self.df=df

    def get_tags(self):
        return self.unique_tags     

    def category_length(self,line_count):
        if line_count < 5:
            return "Short"
        elif 5<= line_count <=15:
            return "Medium"
        else:
            return "Long"
        
    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df["language"] == language) &
            (self.df['Length'] == length) &
            (self.df['tags'].apply(lambda tags: tag in tags))
        ]
        return df_filtered.to_dict(orient="records")

if __name__=="__main__":
    fs=PrepareData()
    post=fs.get_filtered_posts("Medium","English","Motivation")
    print(post)
