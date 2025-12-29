CREATE DATABASE social_media_db;
USE social_media_db;

CREATE TABLE social_media_posts(
  post_id             INT,
  platform            VARCHAR(20),
  post_type           VARCHAR(20),
  post_date           DATE,
  day_of_week         VARCHAR(15),
  posting_hour        INT,
  caption_length      INT,
  hashtags_count      INT,
  likes               INT,
  comments            INT,
  shares              INT,
  saves               INT,
  engagement_rate     FLOAT,
  performance_label   VARCHAR(10),
  is_viral           INT
);

#total posts check 
SELECT COUNT(*)
FROM social_media_with_metrices;

#top 10 high performing posts
SELECT post_id, platform, post_type, engagement_rate
FROM social_media_with_metrices
WHERE performance_label = "high"
ORDER BY engagement_rate DESC
limit 10; 

#platform-wise avg engagement
SELECT platform, ROUND(AVG(engagement_rate), 2) AS avg_engagement
FROM social_media_with_metrices
GROUP BY platform
ORDER BY avg_engagement DESC;

#best post type per platform
SELECT platform, post_type, ROUND(AVG(engagement_rate), 2) AS avg_engagement
FROM social_media_with_metrices
GROUP BY platform, post_type
ORDER BY platform, avg_engagement DESC;

#viral posts percentage
SELECT
  ROUND(SUM(is_viral) * 100.0 / COUNT(*), 2) AS viral_percentage
FROM social_media_with_metrices;

#best posting hours
SELECT posting_hour, ROUND(AVG(engagement_rate), 2) AS avg_engagement
FROM social_media_with_metrices
GROUP BY posting_hour
ORDER BY avg_engagement DESC
LIMIT 5;
