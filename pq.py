class PQ:
    def __init__(self, data, max_pq=False):
        self.pq = ['root'] + data
        self.mode = 'max' if max_pq else 'min'
        self.heapify()

    def heapify(self):
        for i in range(len(self.pq)//2, 0, -1):
            self.sink(i)

    def insert(self, val):
        self.pq.append(val)
        self.swim(len(self.pq)-1)

    def pop(self):
        # remove top element (swap top with last, then sink)
        top_element = self.pq[1]
        self.exchange(1, len(self.pq)-1)
        self.sink(1)
        self.pq.pop() # remove last element from the array
        return top_element

    def swim(self, k):
        if self.mode == 'min':
            # min pq: while parent (k//2) > children (k), swap since not in order.
            while k > 1 and self.pq[k//2] > self.pq[k]:
                self.exchange(k, k//2)
                k = k // 2
        else:
            while k > 1 and self.pq[k//2] < self.pq[k]:
                self.exchange(k, k//2)
                k = k // 2

    def sink(self, k):
        child = 2*k
        if self.mode == 'min':
            while child <= len(self.pq) - 1:    # while parent has an existing left child
                if child < len(self.pq) and self.pq[child] > self.pq[child] + 1:    # if right child is smaller than left child
                    child += 1
                if self.pq[k] <= self.pq[child]:
                    break
                self.exchange(k, child)
                k = child
        else:
            while child <= len(self.pq) - 1:
                if child < len(self.pq) and self.pq[child] < self.pq[child + 1]:
                    child += 1
                if self.pq[k] >= self.pq[child]:
                    break
                self.exchange(k, child)
                k = child

    def exchange(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

def main():
    data = [10, 20, 15, 4, 30, 14]
    pq = PQ(data)
    print(pq.pq)
    pq.insert(5)
    print(pq.pq)
    pq.insert(7)
    print(pq.pq)
    pq.insert(3)
    print(pq.pq)

main()
