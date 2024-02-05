from exceptions import UnsuitableBlock, EmptyColumn


class Block:
    def __init__(self, name: int):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.name < other.name
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, type(self)):
            return self.name > other.name
        return NotImplemented


class Column:
    def __init__(self, amount_blocks: int, first_block=False):
        self.blocks = []
        self.amount_blocks = amount_blocks
        if first_block:
            self.__add_starts_block()

    def add_block(self, obj: Block):
        if not self.is_empty() and self.blocks[-1] < obj:
            raise UnsuitableBlock
        self.blocks.append(obj)

    def is_empty(self):
        return not bool(self.blocks)

    def _is_full(self):
        return bool(len(self.blocks) == self.amount_blocks)

    @property
    def upper_block(self):
        if self.is_empty():
            return Block(0)
        upper_block = self.blocks[self.count_blocks() - 1]
        return upper_block

    def retrieve_block(self):
        if self.is_empty():
            raise EmptyColumn
        block = self.blocks.pop()
        return block

    def __add_starts_block(self):
        """adding starts blocks"""
        for i in range(self.amount_blocks, 0, -1):
            self.blocks.append(Block(i))

    def __str__(self):
        return f'{self.blocks + [0 for _ in range(self.amount_blocks - self.count_blocks())]}'

    def count_blocks(self):
        return len(self.blocks)

    def __repr__(self):
        return self.__str__()

class HanoiTower:
    def __init__(self, amount_blocks):
        self.amount_blocks = amount_blocks
        self.column_1 = Column(amount_blocks, first_block=True)
        self.column_2 = Column(amount_blocks)
        self.column_3 = Column(amount_blocks)
        self.columns = [self.column_1, self.column_2, self.column_3]


    def __str__(self):
        columns = [
            self.column_1,
            self.column_2,
            self.column_3,
        ]

        message = ''
        for column in columns:
            message += f'{column} \n'
        return message

    def __repr__(self):
        return self.__str__()