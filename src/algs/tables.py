from collections import defaultdict


def tabularize(mappings, fill=None):
    table = defaultdict(lambda: [fill] * len(mappings))

    for index, mapping in enumerate(mappings):
        for key, value in mapping.items():
            table[key][index] = value

    return table


def detabularize(table):
    return [
        dict(zip(table, zipped))
        for zipped in zip(*table.values())
    ]
