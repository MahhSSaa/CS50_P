class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Exceeds jar's capacity")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies in the jar")
        self.size -= n

    @property
    def capacity(self):
       return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not int(capacity) > 0:
            raise ValueError("Not a non-nagative integeer.")
        self._capacity = capacity

    @property
    def size(self):
       return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Invalide size")
        self._size = size
