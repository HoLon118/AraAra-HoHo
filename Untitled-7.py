class Vegetable():
    def __init__(self, weight, max_num, profit):
        self.weight = weight
        self.max_num = max_num
        self.profit = profit
        self.load = 0

class Load():
    def __init__(self, goods, max_load):
        self.goods = goods
        self.max_load = max_load
        self.max_flag = 0
            
    def estimate_profit(self):
        load = 0
        p = 0
        for good in self.goods:
            load += good.weight
            if (load > self.max_load):
                print("it is over load.")
                return 0
            p += good.profit
        return p
        
    def increase_load(self):
        self.goods[0].load += 1
        for index, good in enumerate(self.goods):
            if(good.load > good.max_num):
                good.load = 0
                if(index < len(self.goods) - 1):
                    self.goods[index + 1] += 1
                else:
                    good.load = good.max_num
                    print("All goods are achieved max num")
                    self.max_flag = 1

apples = Vegetable(4, 11, 6)
bananas = Vegetable(5, 30, 10)
coconuts = Vegetable(7, 4, 10)
durian = Vegetable(15, 8, 23)
eggplants = Vegetable(3, 22, 5)
list_of_goods = [
    apples,
    bananas,
    coconuts,
    durian,
    eggplants
]
for good in list_of_goods:
    good.load = 1
car = Load(list_of_goods, 50)

profit = car.estimate_profit()
print(profit)