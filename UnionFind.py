class UnionFind:

    # initialize based on the number of possible ids
    def __init__(self, n):
        self.arr = [-1] * n
        self.size = [0] * n
        self.count = 0

    # check if the id is valid
    def is_valid(self, x):
        return self.arr[x] != -1

    # make an id valid
    def set_parent(self, x):
        if self.arr[x] == -1:
            self.arr[x] = x
            self.size[x] = 1
            self.count += 1

    # get the parent of an id
    def root(self, x):
        while self.arr[x] != x:
            self.arr[x] = self.arr[self.arr[x]]
            x = self.arr[x]
        return x

    # union two ids
    def union(self, a, b):
        ra = self.root(a)
        rb = self.root(b)

        if ra != rb:
            if self.size[ra] < self.size[rb]:
                self.arr[ra] = self.arr[rb]
                self.size[rb] += self.size[ra]
            else:
                self.arr[rb] = self.arr[ra]
                self.size[ra] += self.size[rb]
            self.count -= 1