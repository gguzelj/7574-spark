import pyspark
import re
import time

sc = pyspark.SparkContext()
	
text_file = sc.textFile("/data/bible.txt")

stopwords = [
'the','and','of','to','that','in','he','shall','unto', 'for','i','his',
'a','they','be','is','not', 'him', 'them','it','with','thou','thy',
'was','which','','all', 'my','but','their','have','ye','from','as',
'are','when','were','this','by','then','there','him','into','had','came',
'on','up','one','we','your','me']

def simulated_long_process(x):
    time.sleep(0.0001)
    return x

counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: word.lower()) \
             .map(lambda word: re.sub('[.,;,\',\",:,\,]','',word)) \
             .filter(lambda x: x not in stopwords) \
             .map(simulated_long_process) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b) \
             .sortBy(lambda a: a[1], False)

counts.saveAsTextFile("/results/bible_count")