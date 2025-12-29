import pandas as pd 
import matplotlib.pyplot as plt

#load cleaned data
df = pd.read_csv("data/cleaned_social_media_data.csv")


#average engagement by post type 
post_type_engagement = df.groupby("post_type")["engagement_rate"].mean()
print(post_type_engagement) 

post_type_engagement.plot(kind= "bar", color= "blue", title= "engagement rate by post type")
plt.show() 


#engagement by platform
platform_engagement = df.groupby("platform")["engagement_rate"].mean()
print(platform_engagement) 

platform_engagement.plot(kind= "bar", color= "red", title= "engagement rate by platform")
plt.show() 


#best posting hour
hourly_engagement = df.groupby("posting_hour")["engagement_rate"].mean()
print(hourly_engagement)

hourly_engagement.plot(kind= "bar", color= "green", title= "best posting hour")
plt.show() 


#hashtags vs engagement
plt.scatter(df["hashtags_count"], df['engagement_rate'])
plt.xlabel("hashtags count")
plt.ylabel("engagement rate")
plt.title("hashtags vs engagement")
plt.show() 