from typing import Callable, List
import hashlib


def _hashfunc(b: bytes) -> str:
    return hashlib.md5(b).hexdigest()

class SimHash:
    value: List[int]
    def __init__(
        self,
        bit_size: int = 64,
        hashfunc: Callable[[bytes], str] = _hashfunc
    ) -> None:
        self._bit_size = bit_size
        self._hex_length = bit_size // 4
        self._hashfunc = hashfunc

    def __eq__(self, other: 'SimHash'):
        return self.value == other.value

    def build_from_features(self, features: List[str]) -> 'SimHash':
        value = [0] * self._bit_size
        for f in features:
            bit_array = self._to_bit_array(self._hashfunc(f.encode('utf-8'))[:self._hex_length])
            value = [value[i] + b for i, b in enumerate(bit_array)]
        self.value = [int(b > len(features) / 2) for b in value]
        return self

    def _to_bit_array(self, h: str) -> List[int]:
        bit_array = bin(int(h, base=16)).lstrip('0b')
        bit_array = '0' * (self._bit_size - len(bit_array)) + bit_array
        return [int(b) for b in bit_array]

