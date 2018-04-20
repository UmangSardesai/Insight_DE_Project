# Insight Data Engineering Project - 18B

## Summary
Mining comment made by users on Reddit

## Purpose
Can compute 500 GB of data smoothly without any hiccups. Elastic Search has a lot of a features. Try to show them using this data.  

## Use cases
1) Get all the comments made by one user over the years: 
a) Understand user behavior.
b) Does he/she swear a lot.

2) Fetch the most discussed topic (number of times a word as appeared) on a day/week/month.

3) Performance testing: Compare time taken to process 100 GB of data on:

a) Elastic Search running on a Spark Cluster.

b) Elastic Search running separately with Spark doing preproceessing.

c) Mutli Node Elastic Search with Mutil Node Spark.

## Technologies used:
a) Reddit data is on S3

b) Spark for Preprocessing and Filtering

c) Elastic Search for Search 

d) Web UI: Using Flask and Bootstrap

## Architechture
![Arch](https://github.com/UmangSardesai/Insight_DE_Project/blob/master/arch.png)
