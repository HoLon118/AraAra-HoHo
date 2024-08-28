class StoreTemp():
    def __init__(self, length):
        self.length = length
        self.nums = [0] * length
        self.full = 0
    def add(self):
        """
        make first digit += 1.
        then do carry (if need to)
        """
        self.nums[0] += 1
        for i in range(self.length - 1):
            if (self.nums[i] == self.length):
                self.nums[i] = 0
                self.nums[i+1] += 1
        if (self.nums[-1] == self.length):
            self.nums = [0] * length
            self.full = 1
    def check(self):
        """
        if there is no repeat element.
        return 0.
        """
        t = []
        for i in self.nums:
            if str(i) in t:
                return 1
            else:
                t.append(str(i))
        return 0

    
stringArray = ["庭","院","深","深","深","幾","許"]
length = len(stringArray)
temp = StoreTemp(length)
store = []

while(temp.full != 1):
    t = []
    if temp.check() == 0:
        for i in temp.nums:
            t.append(stringArray[i])
        if t not in store:
            store.append(t)
    temp.add()

for i, s in enumerate(store): 
    print(i+1, "\t", s)