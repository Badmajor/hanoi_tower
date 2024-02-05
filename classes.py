from collections import deque

from exceptions import UnsuitableBlock, EmptyColumn


class Block:
    def __init__(self, name: int):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.name < other.name
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, type(self)):
            return self.name > other.name
        return NotImplemented


class Column(deque):
    def __init__(self, maxlen: int=None,
                 iterable: list=None,
                 add_starts_block: bool=False):
        if add_starts_block:
            iterable = self.__starts_block(maxlen)
        iterable = iterable if iterable is not None else []
        super().__init__(iterable, maxlen)

    def append(self, obj: Block):
        if not self.is_empty() and self[-1] < obj:
            raise UnsuitableBlock
        super().append(obj)

    def is_empty(self) -> bool:
        return not bool(list(self))

    def __starts_block(self, maxlen: int) -> list[Block]:
        """Adding starts blocks."""
        starts_blocks = []
        for i in range(maxlen, 0, -1):
            starts_blocks.append(Block(i))
        return starts_blocks

    def __repr__(self):
        empty_places = [0] * (self.maxlen - len(self))
        return f'{list(self) + empty_places}'


class HanoiTower:
    def __init__(self, amount_blocks):
        self.amount_blocks = amount_blocks
        self.column_1 = Column(maxlen=amount_blocks, add_starts_block=True)
        self.column_2 = Column(maxlen=amount_blocks)
        self.column_3 = Column(maxlen=amount_blocks)
        self.columns = [self.column_1, self.column_2, self.column_3]

    def __repr__(self):
        columns = [
            self.column_1,
            self.column_2,
            self.column_3,
        ]

        message = ''
        for column in columns:
            message += f'{column} \n'
        return message
