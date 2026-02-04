def tqdm(iterable, desc=None):
    for item in iterable:
        yield item

__all__ = ['tqdm']