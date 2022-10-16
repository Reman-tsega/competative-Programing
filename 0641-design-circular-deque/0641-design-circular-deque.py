class MyCircularDeque:

    def __init__(self, k):
        self._size = 0
        self._front, self._rear = 0, 0
        self._capacity = k
        self._queue = [-1] * k

    def insertFront(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self._queue[self._front] = value
        else:
            self._front = (self._front - 1) % self._capacity
            self._queue[self._front] = value
        self._size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self._queue[self._rear] = value
        else:
            self._rear = (self._rear + 1) % self._capacity
            self._queue[self._rear] = value
        self._size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self._queue[self._front] = -1
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._rear = self._front
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self._queue[self._rear] = -1
        self._rear = (self._rear - 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._front = self._rear
        return True

    def getFront(self):
        return self._queue[self._front]

    def getRear(self):
        return self._queue[self._rear]

    def isEmpty(self):
        return self._size == 0

    def isFull(self):
        return self._size == self._capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()