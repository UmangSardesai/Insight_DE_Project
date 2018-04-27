# Insight Data Engineering Project - 18B

## Summary
Low Latency search of high velocity incoming data

## Purpose
Search engine is based on indexing. Search results are dependent of two things. 

a) How fast is the indexing 
b) How efficient is the indexing.

Streaming data - Data changes continuously. That means index changes continuously., which makes it very difficult to search.

Elastic Search provides Percolators which is specifically used for stream data. 
However can it scale?

### Basic Goal:
Implement Low Latency search (as real time as possible) of high velocity incoming data using Percolators

### Good to have:
Tune parameters and do significant modifications to improve the response time for search. 

### Cherry on the cake: 
Implement a simple inverted index search on multi node Spark and check if can out perform percolators. 

## Use case:
Amazon Customer support.    
