class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.val = []
        for i in range(capacity):
            self.val.append([])
        self.stack = [i for i in range(capacity)]

    def get(self, key: int):
        for i in range(len(self.val)):
            if self.val[i][0] == key:
                self.stack.remove(i)
                self.stack.append(i)
                return self.val[i][1]
        return -1

    def put(self, key: int, value: int):
        self.val[self.stack[0]] = [key, value]
        self.stack.append(self.stack[0])
        self.stack.pop(0)


try:
    pass
except:
    pass

obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key, value)
