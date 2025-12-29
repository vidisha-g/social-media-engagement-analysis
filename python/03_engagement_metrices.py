import pandas as pd 

#load cleaned data 
df = pd.read_csv("data/cleaned_social_media_data.csv")

#basic stats
avg_engagement = df["engagement_rate"].mean()


#performance labels 
df["performance_label"] = "average"

df.loc[df["engagement_rate"] >= avg_engagement * 1.2, "performance_label"] = "high"
df.loc[df["engagement_rate"] <= avg_engagement * 0.8, "performance_label"] = "low"


#viral posts(business rule)
df["is_viral"] = 0
df.loc[(df["shares"] > df["shares"].quantile(0.90)) &
       (df["engagement_rate"] > avg_engagement), "is viral"] = 1


#save metrices file
df.to_csv("data/social_media_with_metrices.csv", index= False)

print("engagement metrices created successfully!") 