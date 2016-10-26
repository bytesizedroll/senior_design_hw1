# Team 1 Project 1 Solution

### Explanation for Problem 3
To run our solution:
``` 
$ python queries.py 
```
Example output is below. As you can see from the example output, you don't know which search engine is which until the end of the test. This preserves the double-blind nature of our test. Our solution takes random articles from the internet and tries to find those articles based on the key words from the article title. This provides a uniform and unbiased way to test each search engine. Each of the three search engines is queried and then given a score from 0-10 depending on how high up in the search results our target link is. 

Here is an example output:
```
query 1: assessing google smartphone
Search engine 1: 9
Search engine 2: 0
Search engine 3: 10


query 2: utah random clowns hysteria
Search engine 1: 4
Search engine 2: 10
Search engine 3: 10


query 3: google AI justice
Search engine 1: 10
Search engine 2: 0
Search engine 3: 0


query 4: Rahm Emanuel's Speech violence chicago
Search engine 1: 4
Search engine 2: 10
Search engine 3: 0


query 5: police facial recognition tougher oversight
Search engine 1: 10
Search engine 2: 10
Search engine 3: 10


totals:
{'ask': 30, 'bing': 37, 'yahoo': 30}
Search engines:
 1: bing
 2: yahoo
 3: ask

Winner: bing
```
