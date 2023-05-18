# Project_1-Group_3
# Price Correlation to real-world events
 Ryan Cornelius, Kevin Miller, Jo Ann Millegan, Nelson Linarez, and Navyasri Pusuluri
 
 
The Primary file is Main.ipynb, resources (figures), raw data, cleaned data are sorted into sub-folders.



#The following was completed for data analysis:


## Our group was primarily interested to look at recent price data over the past decade while looking at the data, we sought to answer the following questions.
## Questions:
Which world events are heavily visible in a variety of commodity prices?

Do prices decrease to normal after world events? If so, how long does it take?

Are there any items that appear to have been affected uniquely by one major event?


# Data Collection
Data was collected using the US Bureau of Labor Statistics (BLS), by both pulling from the API and by direct download CSVs.
Years between 2013 and 

Data was cleaned by removing NAN values and limitting the years betweem 2013 and 2023. 
Data was normalized for plotting by using a 0 to 100 scale between minumum and maximum values. 

## Final datasets include:
Air freight prices, water freight prices, land freight prices, electricity prices, gasoline prices, new and used automobile prices, 
general food prices, banana prices, egg prices, shelter (rent) prices, toilet paper prices, television prices, and semiconductor manufacturing machinery prices

## Discussion
Each dataset was grouped and normalized. Normalization was done by viewing the value on a scale of 0 to 100 with its minumum price of the last decade being
0 and its maximum price being 100. Grouping was made by hypothesizing the primary world event to affect each dataset. The percent change over three months 
is native to the BLS API, and is also plotted alongside normalized data. This allows for the absolute price variability to be retained alongside the normalized data.
For presentation and analysis, plots are grouped and figures are made.

## Group 1 Analysis
This dataset includes a group of goods forefront to American consumers (Automobile Prices, Food Prices, Electricity Prices, Gasoline Prices, Toilet Paper Prices). 
We see that world events are highly apperent in the price of many of these goods. Right away, the oil price crash from 2014-2016 is readily apparent in the value 
of gasoline. COVID also shows a dramatic effect in almost all data collected. Gasoline is also an interesting dataset, as it has high volatility, and also shows 
many instances of returning to baseline after increasing due to a world event.

## Group 2 Analysis
This dataset includes a group of goods ingrained in international trade (Bananas, Air Freight Prices, Water Freight Prices, Land Freight Prices, and Gasoline 
Prices). Once again, world events are immediately apperent. Not easily noted previously the world trade disruption caused by the cargo ship, The Ever Given, 
in March 2021 is easily visible in the data. Again, the oil price crash from 2014-2016 is present. This makes sense with the nature or the datasets. COVID is 
still present, but takes a much lesser role. Gasoline again has high volatility, but the 3 month % change shows clear peaks timed with world events.
In particular it is interesting to not the correlation between banana and gasoline, as well as the correlation between the other freight methods. This is 
most apparent between 2014 and 2016 where both banana and gasoline prices are dramatically affected by the crude oil price decline. 

## Group 3 Analysis
This dataset includes a group of goods that appear to have had the highest impact from the 2022 Russia-Ukraine conflict. This primarily stems from semiconductor 
manufacturing machinery prices. This dataset is known to have been dramatically impacted by the conflict, influenced by the sourcing of neon necessary in 
semiconductor manufacturing instrumentation. Water freight and food prices were found to have a high correlation with the semiconductor dataset, pointing 
towards a heavy influrence in the datasets around the 2022 timeline of the event. This is possibly an example of correlation instead of shared causation, 
but is interesting nonetheless. With less simultaniously plotted data, water freight in this instance interestingly appears to have recovered from the COVID 
price increase before the events of the Ever Given. 

## Group 4 Analysis
This dataset includes goods that appear to have had the highest impact from the 2022 Russia-Ukraine conflict. This primarily stems from semiconductor 
manufacturing machinery prices. This dataset is known to have been dramatically impacted by the conflict, influenced by the sourcing of neon necessary 
in semiconductor manufacturing instrumentation. Water freight and food prices were found to have a high correlation with the semiconductor dataset, pointing 
towards a heavy influrence in the datasets around the 2022 timeline of the event. This is possibly an example of correlation instead of shared causation, but 
is interesting nonetheless. With less simultaniously plotted data, water freight appears to have recovered from the COVID price increase before the events of 
the Ever Given. 

## Volatility
As shown, some items have much greater volatility than others. Additionally, outlier values have started to be met in recent years due to world events. 
We can compare all items using boxplots of 3 month average percent change to gauge volatility. As has been mentioned, gasoline prices have been extremely 
volatile in the recent years. Increasing and decreasing seasonally as well as dramatically increasing in value due to world events. Even so, there are few 
datapoints regarded as outliers. Interestingly, eggs also show extreme volatility, as well as many outliers to due events such as flu outbreaks. Most other 
datasets are fairly tight, though with outliers.
Futher notes: Electricity lacks outliers, and has predictable volatility despite recent events. Water freight only has extreme outliers, being predictable 
outside of events such as the Ever Given trade disruption. Televisions are one of the only datasets collected that showed negative average monthly change. 

## Data Correlation and conclusions
A correlation matrix for the collected datasets was created. Most datasets show strong correlation due to similarly dated world events causing data spikes. 
The correlation coefficients are increased on average due to the normalization method. Datasets with correlation coefficients over 0.85 are particularly 
interesting. Implying that the world events (or timelines thereof) that have strong influence on the relative datasets are similar. For instance, gasoline 
and banana prices are highly correlated due to their primary driver being crued oil pricing. Stable datasets such as shelter pricing have relatively few 
positive correlations in this dataset due to being relatively stable outside of COVID causing a slight decrease followed by an increase. One would expect 
the assorted freight types to have the highest correlation values, but in the recent events affecting primarily international trade, a dicotomy appears to 
have formed between international and domestic. Many more conclusions can be drawn, such as Television's correlation with land freight, food, and 
semiconductor manufacturing materials, but many of the conclusions may lack the necessary information to prove causation, and this would require future work.



