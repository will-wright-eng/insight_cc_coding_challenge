# Insight Customer Complaints Coding Challenge

![cfpb](https://github.com/william-cass-wright/insight_cc_coding_challenge/blob/master/images/cfpb.png)

## Objectives
For each financial product and year: 
- the total number of complaints
- number of companies receiving a complaint
- the highest percentage of complaints directed at a single company.

## Enhancments & Exploratory

- API call to complaints database

- Generators in extract stage:  
By timing each stage of the ETL I found that the extraction process tool the longest. I believe that implmenting generators or iterators, e.g. in the form of list comprehension, would better scale the program. 

- Comparison to pandas:  
Packages like Pandas are notoriously slow so I'm curious to understand how much slower an implementation would be relative to the code written.