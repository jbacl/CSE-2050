# This file empty on purpose
class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
    
    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority and self.item == other.item

class PQ_UL:
    def __init__(self):
        self._L = []

    def __len__(self):
        return len(self._L)

    def insert(self, item, priority):
        self._L.append(Entry(item, priority))

    def find_min(self):
        min_idx = 0
        for idx in range(len(self)):
            if self._L[idx] < self._L[min_idx]:
                min_idx = idx
        return self._L[min_idx]

    def remove_min(self):
        min_idx = 0
        for idx in range(len(self)):
            if self._L[idx] < self._L[min_idx]:
                min_idx = idx
        return self._L.pop(min_idx)

class PQ_OL:
    def __init__(self):
        self._L = []

    def __len__(self):
        return len(self._L)

    def insert(self, item, priority):
        self._L.append(Entry(item, priority))
        self._L.sort(key = lambda e: e.priority)

    def find_min(self):
        return self._L[0]

    def remove_min(self):
        return self._L.pop(0)