def count_sheep_generator(n: int):
    for i in range(1, n+1):
        yield f"Coutning: {"🐑" * i}"

for sheep in count_sheep_generator(10000):
    print(sheep)