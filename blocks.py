from block import *
from position import *

#parameter and settings of L block
class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Position(0,2),Position(1,0),Position(1,1),Position(1,2)],
            1: [Position(0,1),Position(1,1),Position(2,1),Position(2,2)],
            2: [Position(1,0),Position(1,1),Position(1,2),Position(2,0)],
            3: [Position(0,0),Position(0,1),Position(1,1),Position(2,1)]
        }
        self.move(0,3)

#parameter and settings of J block
class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position(0,0),Position(1,0),Position(1,1),Position(1,2)],
            1: [Position(0,1),Position(0,2),Position(1,1),Position(2,1)],
            2: [Position(1,0),Position(1,1),Position(1,2),Position(2,2)],
            3: [Position(0,1),Position(1,1),Position(2,0),Position(2,1)]
        }
        self.move(0,3)

#parameter and settings of I block
class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(1,0),Position(1,1),Position(1,2),Position(1,3)],
            1: [Position(0,2),Position(1,2),Position(2,2),Position(3,2)],
            2: [Position(2,0),Position(2,1),Position(2,2),Position(2,3)],
            3: [Position(0,1),Position(1,1),Position(2,1),Position(3,1)]
        }
        self.move(-1,3)

#parameter and settings of O block
class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            1: [Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            2: [Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            3: [Position(0,0),Position(0,1),Position(1,0),Position(1,1)]
        }
        self.move(0,4)

#parameter and settings of S block
class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position(0,1),Position(0,2),Position(1,0),Position(1,1)],
            1: [Position(0,1),Position(1,1),Position(1,2),Position(2,2)],
            2: [Position(1,1),Position(1,2),Position(2,0),Position(2,1)],
            3: [Position(0,0),Position(1,0),Position(1,1),Position(2,1)]
        }
        self.move(0,3)

#parameter and settings of T block
class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position(0,1),Position(1,0),Position(1,1),Position(1,2)],
            1: [Position(0,1),Position(1,1),Position(1,2),Position(2,1)],
            2: [Position(1,0),Position(1,1),Position(1,2),Position(2,1)],
            3: [Position(0,1),Position(1,0),Position(1,1),Position(2,1)]
        }
        self.move(0,3)

#parameter and settings of Z block
class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position(0,0),Position(0,1),Position(1,1),Position(1,2)],
            1: [Position(0,2),Position(1,1),Position(1,2),Position(2,1)],
            2: [Position(1,0),Position(1,1),Position(2,1),Position(2,2)],
            3: [Position(0,1),Position(1,0),Position(1,1),Position(2,0)]
        }
        self.move(0,3)