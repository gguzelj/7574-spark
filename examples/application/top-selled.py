import pyspark
import itertools

def combinations(row):
  l = row[1]
  k = row[0]
  return [(k, v) for v in itertools.combinations(l, 2)]

def partir(row):
    one,other = row[0].split('#')
    return (one, (other, row[1]))

sc = pyspark.SparkContext()
	
orders = sc.textFile("/data/grocery/order_products__train.csv")

sort_by_selled = orders.map(lambda line: line.split(",")) \
                        .map(lambda order: (order[1], 1)) \
                        .reduceByKey(lambda a, b: a + b) \
                        .sortBy(lambda a: a[1], False)

def toCSVLine(data):
  return ','.join(str(d) for d in data)


sort_by_selled.map(toCSVLine).coalesce(1).saveAsTextFile("/results/top-selled")