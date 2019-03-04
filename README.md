# Trabajo práctico final de Sistemas Distribuidos I (7574)

- `git clone https://github.com/gguzelj/7574-spark.git`
- `cd 7574-spark`

## Ejemplos

- `docker-compose -f examples/docker-compose-two-workers.yml up`

### Bible count

- `docker exec -it examples_master_1 bin/spark-submit /application/simple-count.py`
- `head examples/results/bible_count/part-00000`

### Co-occurrences

- `docker exec -it examples_master_1 bin/spark-submit /application/co-occurrence.py`
- `head examples/results/bible_count/part-00000`