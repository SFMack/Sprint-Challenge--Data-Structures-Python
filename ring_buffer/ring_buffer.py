class RingBuffer:
    def __init__(self, capacity):
            self.capacity = capacity
            self.data = []
            self.index = 0

    def append(self, item):
        # if the queue is full
        if len(self.data) == self.capacity:
            # replace the item at the current index with the passed in item
            self.data[self.index] = item
        else:
            # add to the end of the list
            self.data.append(item)

        # reset the index
        self.index = (self.index +1) % self.capacity

    def get(self):
        return self.data