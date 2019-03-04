import pyspark
import itertools

def combinations(order):
  return (order[0], itertools.combinations(order[1], 2))

def unwind(order):
    toCount = []
    for elem in order[1]:
        toCount.append((str(elem[0]) + '#' + str(elem[1]),1))
        toCount.append((str(elem[1]) + '#' + str(elem[0]),1))
    return toCount

def partir(row):
    one,other = row[0].split('#')
    return (one, (other, row[1]))


sc = pyspark.SparkContext()
	
orders = sc.textFile("/data/grocery/order_products__train.csv", 10)

products_by_order = orders.map(lambda line: line.split(",")) \
                        .map(lambda order: (order[0], order[1])) \
                        .groupByKey() \
                        .map(combinations) \
                        .flatMap(unwind) \
                        .reduceByKey(lambda a, b: a + b) \
                        .map(partir) \
                        .groupByKey().mapValues(list)


def toCSVLine(data):
  return ';'.join(str(d) for d in data)

products_by_order.map(toCSVLine).coalesce(1, shuffle = True).saveAsTextFile("/results/co-ocurrencias")