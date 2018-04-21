# Fast Fuzzy Search

A fast fuzzy search algorithm implemented in Python.

Uses Phonex (Phonetic Indexing) to quickly find similar sounding words.
Support for languages depends on languages supported by the PyPhone library.

```python
from fast_fuzzy_search import FastFuzzySearch

ffs = FastFuzzySearch({'language':'english'})
ffs.add_term('hello world', id1)
ffs.add_term('hello friend', id2)

results = ffs.search('helu world')

print(results)
# [(id, text, score)]
```

Dependencies are only the [pyphone library](https://github.com/lingz/pyphone)
