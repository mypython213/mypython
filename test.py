map = {
    0: '.',
    1: '|',
    2: 'z',
    3: ' ',
    4: ' ',
    5: ' '
}

unmap = {
    '.':0,
    ' ':3,
    '*':1,
    'z':2
}

import time

class Brick:
    cord = []
    ofset_x = 0
    ofset_y = 0
    falling = True
    def hide(self, m):
        for i in range(len (self.cord)):
            for j in range(len(self.cord[i])):
                m[i+self.ofset_y][j+self.ofset_x] = m[i+self.ofset_y][j+self.ofset_x] - self.cord[i][j]

    def step_land(self, m:[]):
        Have_space = True
        self.ofset_y += 1
        self.puts(m)
        self.hide(m)
        if len(m)<self.ofset_y+1:
            Have_space = False
        else:
            # self.ofset_y += 1
            for i in range(len (self.cord)):
                for j in range(len(self.cord[i])):
                    if (m[i+self.ofset_y][j+self.ofset_x] != 0) or (not Have_space):
                        Have_space = False
                        break
        if Have_space:
            pass
            # self.ofset_y += 1
        if not Have_space:
            self.ofset_y = self.ofset_y - 1
            self.falling = False
        return Have_space

    def puts(self, m:[]):

        while (len(m) < self.ofset_y):
            m.append([0] * (self.ofset_x))
        for i in range(len (self.cord)):
            if len(m)-1 < i+self.ofset_y:
                m.append([0]*self.ofset_x + self.cord[i])
            else:
                while len(m[i+self.ofset_y]) < len(self.cord[i]) + self.ofset_x:
                    m[i + self.ofset_y].append(0)
                # if len(m[i+self.ofset_y]) < len(self.cord[i]) + self.ofset_x:
                #     m[i + self.ofset_y].append(0)
                #     m[i + self.ofset_y].add(list ((0,)*(self.ofset_x + len(self.cord[i]))))

                for j in range(len(self.cord[i])):
                    # if len(m[i+self.ofset_y])-1 < j +self.ofset_x:
                    #     if j < self.ofset_x:
                    #         m[i + self.ofset_y].append(0)
                    #     else:
                    #         m[i+self.ofset_y].append(self.cord[i][j])
                    # else:
                    m[i+self.ofset_y][j+self.ofset_x] = m[i+self.ofset_y][j+self.ofset_x] + self.cord[i][j]

        # while len(m)<len(self.cord):
        #     m.append([])
        #
        #
        # for i in m:
        #     while len(m[i]) < len(self.cord[m.index]):
        #         m[i].append(self.cord[m.index])
        #     # for j in i
        #     #     if j == '*':
        #     #         m[i.index, j.index] = 1
        #     pass
    def tick(self):
        pass
    def load(self, ex:str):
        r = [[]]
        for i in ex:
            if i == '\n':
                r.append([])
            else:
                r[len(r) - 1].append(unmap[i])
        self.cord = r
        # return r


class World:
    bricks = []
    map = []
    def puts_all(self):
        for i in self.bricks:
            i.puts(self.map)

    def ris(self):
        f1 = open("dis.x", "w")
        for i in self.map:
            for j in i:
                f1.write(map[int(j)])
            f1.write("\n")


W1 = World()
B1 = Brick()
B1.ofset_x = 1
B1.load("""
*..
*..
******""")
B2 = Brick()
B2.ofset_y = 20
B2.ofset_x = 8
B2.load("""
***
.*.
.*.
..*""")
W1.bricks.append(B1)
W1.bricks.append(B2)
W1.puts_all()

W1.bricks[0].hide(W1.map)
#print( W1.bricks[0].step_land(W1.map))
W1.bricks[0].puts(W1.map)


W1.ris()
W1.bricks[0].hide(W1.map)

T = 0

while W1.bricks[0].step_land(W1.map):
    T+=1
    if T == 5:
        W1.bricks[0].ofset_x = W1.bricks[0].ofset_x - 1

    if T > 7:
        W1.bricks[0].ofset_x = W1.bricks[0].ofset_x + 1


    W1.bricks[0].puts(W1.map)
    W1.ris()
    # W1.ris()
    time.sleep(0.5)
    if T <17:
        W1.bricks[0].hide(W1.map)


B2.ofset_y = 0
B2.ofset_x = 6
W1.bricks[1].puts(W1.map)
W1.ris()
W1.bricks[1].hide(W1.map)

while W1.bricks[1].step_land(W1.map):
    W1.bricks[1].puts(W1.map)
    W1.ris()
    # W1.ris()
    time.sleep(0.5)
    W1.bricks[1].hide(W1.map)
