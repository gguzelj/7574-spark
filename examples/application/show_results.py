import csv
import sys
from ast import literal_eval as make_tuple
import re

def load_products():
    products = {}
    with open('./examples/data/grocery/products.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            products[row[0]] = row[1]
    return products

def search_results(product_id):
	with open("./examples/results/co-ocurrencias/part-00000") as origin_file:
		for line in origin_file:
			if re.search('^' + product_id + ';', line):
				tuples = make_tuple(line.split(';')[1])
				tuples = sorted(tuples, key=lambda tup: tup[1], reverse=True)
				return  tuples

def print_entry(key):
	if (not search_results(key)):
		print("No hay informacion del producto %s" % key)
		return
	print("%s [%s]:" % (dic[key],key))
	print_max = 0
	for correlation in search_results(key):
		if(print_max == 10):
			break
		print("\t%s - %s" % (correlation[1], dic[correlation[0]]))
		print_max +=1

def is_num(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


dic = load_products()
print("Ver resultados co-ocurrencias (exit para salir)\n")

while (True):
	text = input("Ingrese un id de producto: \t")
	if (text == "exit"):
		break

	if (is_num(text)):
		print_entry(text)
	else:
		for x in dic:
			if re.search(text, dic[x], re.IGNORECASE):
				print_entry(x)


#results = load_results()
#a = load_products()

#keys = ['16','4605','42265','45066','31717','5876','44632','43352','28204','5450','8424','21616','24184','19057','30489','26604','37646','27104','49235','28985','49215','13176','21137','21903','47626','47766','47209','16797','26209','27966','39275','27845','30391']

#for key in keys:
#    print_entry(key, results[key])