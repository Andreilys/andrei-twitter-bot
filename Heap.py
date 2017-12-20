class MaxHeap():
    def __init__(self):
        self.list = [None]
        self.size = 0

    def peek(self,n):
        # look at first node
        return self.list[1:n+1]

    def insert(self, node):
        # push item onto heap
        self.list.append(node)
        self.size += 1
        self.sift_up(self.size)

    def delete_max(self):
        # remove the root and restructure heap
        key = self.list[1]
        self.list[1] = self.list.pop()
        self.size -= 1
        self.sift_down(1)
        return key

    def sift_down(self, idx):
        while idx * 2 <= self.size:
            key = self.list[idx]
            max_child_idx = self.max_child(idx)
            max_child = self.list[max_child_idx]
            if max_child > key:
                self.swap(idx, max_child_idx)
            idx = max_child_idx

    def sift_up(self, idx):
        while idx // 2 > 0:
            key = self.list[idx]
            parent_idx = idx // 2
            parent_key = self.list[parent_idx]
            if key[1] > parent_key[1]:
                self.swap(idx, parent_idx)
            idx = parent_idx

    def max_child(self, idx):
        l_idx = idx * 2
        r_idx = idx * 2 + 1
        if r_idx > self.size:
            return l_idx
        if self.list[r_idx] > self.list[l_idx]:
            return r_idx
        else:
            return l_idx

    def swap(self, idx_a, idx_b):
        key = self.list[idx_a]
        self.list[idx_a] = self.list[idx_b]
        self.list[idx_b] = key


if __name__ == '__main__':
    counts = MaxHeap()
    counts.insert(("the", 0.5))   # insert some tuples of count/word pairs
    counts.insert(("dog", 1.3))
    counts.insert(("apple", 0.9))
    counts.insert(("red", 0.2))
    print(counts.peek())
    #
    # counts.peek()               # => (5, "red")
    # counts.delete_max()         # => (5, "red")
    # counts.peek()               # => (3, "the")
