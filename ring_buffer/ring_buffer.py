class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.current_index = 0

    def append(self, item):
        # if the length of the data list is less than capacity, append normally
        if len(self.data) < self.capacity:
            self.data.append(item)

        # set the current_index to the item
        self.data[self.current_index] = item
        # increment the index for the next item
        self.current_index += 1
        # if the index becomes greater than the of capicity -1 (), reset the index to 0
        if self.current_index > self.capacity - 1:
            self.current_index = 0

    def get(self):
        return self.data
