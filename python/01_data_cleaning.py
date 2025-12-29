import pandas as pd 

#load data
df = pd.read_csv("data/social_media_content_performance.csv")

#check data
print(df.head()) 
print(df.info()) 

#remove duplicates
df.drop_duplicates(inplace= True) 

#create engagement rate
df["engagement_rate"] = (
    df["likes"] + df["comments"] + df["shares"] + df["saves"]
) / df["likes"] 

#save cleaned file
df.to_csv("data/cleaned_social_media_data.csv", index= False)

print("cleaning done & file saved!") 