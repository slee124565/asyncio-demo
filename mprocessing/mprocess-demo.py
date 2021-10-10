"""
    todo: take hc3 devices data as example
    todo: take multi hc3 rest api fetching as example
"""

import collections
from pprint import pprint
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


def nobel_filter(x):
    return x.nobel is True


# pprint(tuple(filter(lambda x: x.nobel is True, scientists)))
# pprint(tuple(filter(nobel_filter, scientists)))

names_n_ages = tuple(map(
    lambda x: {'name': x.name, 'age': 2021-x.born}, scientists))

pprint(names_n_ages)

from functools import reduce

total_age = reduce(
    lambda acc, val: acc + val['age'],
    names_n_ages,
    0)

print(f'total_age: {total_age}')


def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc


scientists_by_fields = reduce(
    reducer,
    scientists,
    {'math': [], 'physics': [], 'chemistry':[], 'astronomy': []}
)

pprint(scientists_by_fields)


scientists_by_fields = reduce(
    reducer,
    scientists,
    collections.defaultdict(list)
)
pprint(scientists_by_fields)
