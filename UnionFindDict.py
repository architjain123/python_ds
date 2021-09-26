class UnionFindDict:

    # initialize based on the number of possible ids
    def __init__(self):
        self.dct = {}
        self.size = {}
        self.count = 0

    # check if the id is valid
    def is_valid(self, x):
        return x in self.dct[x]

    # make an id valid
    def set_parent(self, x):
        if x not in self.dct:
            self.dct[x] = x
            self.size[x] = 1
            self.count += 1

    # get the parent of an id
    def root(self, x):
        while self.dct[x] != x:
            self.dct[x] = self.dct[self.dct[x]]
            x = self.dct[x]
        return x

    # union two ids
    def union(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra != rb:
            if self.size[ra] < self.size[rb]:
                self.dct[ra] = self.dct[rb]
                self.size[rb] += self.size[ra]
            else:
                self.dct[rb] = self.dct[ra]
                self.size[ra] += self.size[rb]
            self.count -= 1