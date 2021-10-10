import collections
from pprint import pprint
import multiprocessing
import time

Scientist = collections.namedtuple('Scientist', [
    'name', 'field', 'born', 'nobel',
])

scientists = [
    Scientist(name='Ada Lovelace', field='math', born=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physics', born=1867, nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', born=1951, nobel=False),
]


def transform(x):
    print(f'process record {x.name} ...')
    time.sleep(1)
    result = {'name': x.name, 'age': 2021 - x.born}
    print(f'done process record {x.name}')
    return result


if __name__ == '__main__':
    pprint(tuple(scientists))

    start = time.time()
    result = tuple(map(transform, scientists))

    end = time.time()
    print(f'\n time to complete: {end - start:.2f}\n')
    pprint(result)
