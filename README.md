   # Trabajo práctico final de Sistemas Distribuidos I (7574)

## Requerimientos

- Docker & docker-compose
- Python3

## Ejemplos

Primero clonar el proyecto:

- `git clone https://github.com/gguzelj/7574-spark.git`
- `cd 7574-spark`

Luego levantar cluster de spark con dos workers

- `docker-compose -f examples/docker-compose-two-workers.yml up`

### Bible count

- `docker exec -it examples_master_1 bin/spark-submit /application/simple-count.py`
- `head examples/results/bible_count/part-00000`

### Co-occurrences

- `docker exec -it examples_master_1 bin/spark-submit /application/co-occurrence.py`

### Top-Selled

- `docker exec -it examples_master_1 bin/spark-submit /application/top-selled.py`
- `head examples/results/top-selled/part-00000`

### View Results

El siguiente programa permite visualizar los resultados del job de co-occurrencias. Permite la busqueda de resultados tanto por id como por descripción de producto

- `python examples/application/show_results.py`


```
python3 examples/application/show_results.py
Ver resultados co-ocurrencias (exit para salir)

Ingrese un id de producto: 	24852
Banana [24852]:
	2216 - Organic Avocado
	2174 - Organic Strawberries
	2158 - Large Lemon
	2000 - Organic Baby Spinach
	1948 - Strawberries
	1331 - Limes
	1231 - Honeycrisp Apple
	1210 - Organic Fuji Apple
	1162 - Seedless Red Grapes
	1071 - Yellow Onions
```


