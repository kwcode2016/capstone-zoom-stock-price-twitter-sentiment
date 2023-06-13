
# Exploring the Correlation Between Zoom Stock Price and Twitter Sentiment: A Data Science Approach

### Webapp link
Link to Webapp Github: https://github.com/kwcode2016/zoom-stock-twitter-sentiment-webapp

Link to Webapp: https://kwcode2016-zoom-stock-twit-webapp-streamlit-twitter-zoom-2elx7b.streamlit.app/ 




### Abstract:
This paper aims to delve into the exploration of the correlation between the stock price of Zoom Video Communications, Inc. (Zoom) and the sentiments expressed on Twitter regarding the said stock. The fundamental premise lies in examining how public sentiment on Twitter may be intertwined with the price fluctuations of Zoom stock.


### Introduction:
In the past four years, Zoom has seen a significant rise and fall in its stock price, primarily due to the changing work environments globally in response to the Covid-19 pandemic. This period also saw heightened activity on Twitter concerning Zoom stock, providing a unique opportunity to investigate if there exists a relationship between Twitter sentiment and stock price changes.


### Why Zoom?
Zoom was chosen due to its highly volatile stock price over the past few years and the significant volume of related tweets. The drastic swings in stock price and the considerable chatter on Twitter present an intriguing case study for examining the possible links between social media sentiment and stock market performance.


### Conda Env List
Here are the list of packages and version used for this project: [Conva Env List](./conda_env.txt)

### Data Acquisition:
Data for this project was obtained by scraping Zoom stock price information and corresponding tweets about Zoom. It's important to note that scraping data from both Twitter and stock price websites have become more challenging due to changes in these platforms' data access policies and need new ways to acquire this data.


### Data Processing (ETL):
The raw data obtained underwent a thorough extraction, transformation, and loading (ETL) process to prepare it for analysis. This included cleaning the data, dealing with missing values, and formatting the data into a usable format for subsequent analysis.


### Twitter Sentiment Model used:
RoBERTa, a transformer-based machine learning technique for natural language understanding. I used the Cardiff RoBERTa latest model as twitter was the main data that was used to train it.


### Model Training:
After finding that the model misunderstood financial jargon, I fine-tuned the model to better label the sentiment of financial tweets. This involved training the model to understand the language nuances within the context of financial data.

### Data Timeline:
The data used in this project spanned from 2019 to December 2022, encapsulating both pre-pandemic and pandemic-era data, which provided a rich, diverse dataset for this project.

### Processing with CUDA:
Initially using CPU to run the RoBERTa model was too slow. Taking about 3 days for sentiment analysis of 1500 tweets. The total number of tweets at 300k will take 600 days! (Which is unacceptable)

Given the substantial size of the data - around 300k tweets, CUDA was leveraged for faster processing times, making the data handling process more efficient.

### Results:
Through the created web application, users can explore the relationship between the 7-day average of positive, negative, and neutral Twitter sentiment and Zoom's stock price.

### Future Directions:
While the project has provided insightful results, there is ample room for future enhancements. Applying more sophisticated machine learning techniques could help uncover deeper correlations between Twitter sentiment and stock price. The model could also be expanded to encompass more than just Zoom, by identifying and analyzing tweets related to other stocks.

The fine-tuning process for RoBERTa could be adapted to handle more financial data, and the web application could be further generalized to analyze any company's stock based on its name and symbol.

Another promising avenue for future research could involve the application of time series machine learning models to predict future stock prices based on sentiment analysis. Additionally, the sentiment analysis could be expanded beyond Twitter to other social media platforms like Reddit, Facebook, Instagram, and TikTok, which host substantial discussions about stock trading.

One very interesting direction for future research is to have a specific target for sentiment analysis. For this project, only the general sentiment of the tweets were considered. So a tweet that specified very good news for another stock, but negative for the zoom stock price, RoBERTa will label it as positive sentiment. This can be corrected by modifying the use of RoBERTa (or other sentiment analysis models.) this is done by specifying 'find the sentiment analysis of Zoom Stock PRICE'. Once this is done, we can find a much better sentiment analysis of each tweet.

In conclusion, this paper provides a compelling exploration of the relationship between social media sentiment and stock price changes. Further work in this area could lead to a new understanding of the influences that drive the stock market.