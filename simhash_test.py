from simhash import SimHash
import numpy as np

b = [f'{np.random.randint(1e+10):10d}' for _ in range(1000)]
h1 = SimHash(128).build_from_features(['hoge', 'fuga'])
# h2 = SimHash().build_from_features(['hoge', 'fuga', 'foo', 'aasdf', 'fhuihd', 'hudihfa', 'hidfhas' ,'dhuih'])
h2 = SimHash(128).build_from_features(b[:999])
h3 = SimHash(128).build_from_features(b)

print(np.abs(np.array(h2.value) - np.array(h3.value)).sum())
print(np.abs(np.array(h1.value) - np.array(h2.value)).sum())
print(np.abs(np.array(h1.value) - np.array(h3.value)).sum())