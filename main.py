from multiprocessing import Pool
import time
import threading

def read_info(name:str):
    """Функция создает локальный список all_data, открывает файл name для чтения,
        считывает информацию построчно (readline), пока считанная строка не окажется пустой.
        Каждую считанную строку добавлять в список all_data."""
    all_data = []
    try:
        with open(name, 'r', encoding='utf8') as file:
            while (line := file.readline()) != '':
                all_data.append(line)
    except OSError as e:
        print(f'Ошибка чтения файла: {e}')


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    # m = map(read_info, filenames)
    # ts = time.time()
    # for n in m:
    #     pass
    # print(f'Линейный вызов функций: {time.time() - ts} сек.')

    ts = time.time()
    with Pool(4) as pool:
        pool.map(read_info, filenames)
    print(f'Многопроцессный вызов функций: {time.time() - ts}')
