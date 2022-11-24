import time

class Tile():
    def __init__(self, r, g, b):
        self.color = [r, g, b]

    def add(self, t, n):
        r = self.color[0] + t.color[0] 
        g = self.color[1] + t.color[1]
        b = self.color[2] + t.color[2]

        c = [r, g, b]
        minval = min(c)
        diff = max(c) - minval
        c = [i-minval for i in c]
        c = [i/diff for i in c]
        c = [i * 255 for i in c]

        return Tile(*c)
        

    def drawTile(self):
        # print(self.color, end = '')
        return self.color


class Pascal():
    def __init__(self, n = 3):
        # self.arr = [
        #     [1],
        #     [1, 1],
        #     [1, 2, 1]
        # ]
        self.arr = [
            [Tile(254, 254, 254)],
            [Tile(254, 254, 254), Tile(254, 254, 254)],
            [Tile(100, 0, 0), Tile(0, 100, 0), Tile(0, 0, 100)]
        ]
        # print(type(self.arr[0][0]))
        self.n = n
        self.generate()

    def print_pascal(self):
        for i in self.arr:
            print(*i)

    def print_tiles(self):
        for i in self.arr:
            for j in i:
                j.drawTile()
            print()

    def generate(self):
        nt = 2
        if self.n <= 3:
            self.arr = self.arr[:self.n]

        else:
            ptr = 1
            while nt < self.n:
                # newarr = [1]
                newarr = [Tile(100, 0, 0)]
                while ptr < len(self.arr[-1]):
                    # newarr.append(self.arr[nt][ptr] + self.arr[nt][ptr-1])
                    newarr.append(self.arr[nt][ptr].add(self.arr[nt][ptr-1], self.n))
                    ptr += 1
                # newarr.append(1)
                newarr.append(Tile(0, 0, 100))
                self.arr.append(newarr)
                nt += 1
                ptr = 1

    def getTriangle(self):
        return self.arr


# if __name__ == '__main__':
#     start_time = time.time()
#     triangle = Pascal(10)
#     print("--- %s seconds ---" % (time.time() - start_time))
#     triangle.print_tiles()









