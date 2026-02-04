import csv

class NumericArray:
    def __init__(self, data):
        self._data = [float(x) for x in data]
    def astype(self, _type):
        return self
    def __sub__(self, other):
        return NumericArray([x - other for x in self._data])
    def __truediv__(self, other):
        return NumericArray([x / other for x in self._data])
    def __iter__(self):
        return iter(self._data)
    def __len__(self):
        return len(self._data)
    def __getitem__(self, key):
        if isinstance(key, slice):
            return self._data[key]
        return self._data[key]

class Series:
    def __init__(self, data):
        self._data = list(data)
    def to_numpy(self):
        return NumericArray(self._data)

class DataFrame:
    def __init__(self, data):
        # assume dict of lists
        self._data = data
        self.columns = list(data.keys())
    @property
    def empty(self):
        # empty if any column has zero length
        if not self.columns:
            return True
        return all(len(self._data[self.columns[0]]) == 0 for _ in [0])
    def to_csv(self, path, index=False):
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.columns)
            rows = zip(*[self._data[c] for c in self.columns])
            for r in rows:
                writer.writerow(r)
    def __getitem__(self, key):
        return Series(self._data[key])

def read_csv(path):
    with open(path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames
        data = {c: [] for c in cols}
        for r in reader:
            for c in cols:
                data[c].append(r[c])
    return DataFrame(data)

__all__ = ['DataFrame', 'read_csv', 'Series']