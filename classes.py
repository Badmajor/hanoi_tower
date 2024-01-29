from exceptions import UnsuitableBlock, EmptyColumn


class Block:
    def __init__(self, name: int):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return self.__str__()


class Column:
    def __init__(self, amount_blocks: int, first_block=False):
        self.empty_block = Block(0)
        self.blocks = [self.empty_block] * amount_blocks
        self.amount_blocks = amount_blocks
        if first_block:
            self.__add_starts_block()

    def add_block(self, obj: Block):
        if self.is_empty() or self.upper_block.name > obj.name:
            index = self.count_blocks()
            self.blocks[index] = obj
        else:
            raise UnsuitableBlock(f'Column: {self} -> Block: {obj}')

    def is_empty(self):
        return not bool(self.blocks[0].name)

    def _is_full(self):
        return bool(self.blocks[-1].name)

    @property
    def upper_block(self):
        if self.is_empty():
            return Block(0)
        upper_block = self.blocks[self.count_blocks() - 1]
        return upper_block

    def retrieve_block(self):
        if self.is_empty():
            raise EmptyColumn
        block = self.blocks.pop(self.count_blocks() - 1)
        self.blocks.append(self.empty_block)
        return block

    def __add_starts_block(self):
        """adding starts blocks"""
        for i in range(self.amount_blocks, 0, -1):
            self.blocks[self.amount_blocks - i] = Block(i)

    def __str__(self):
        return f'{self.blocks}'

    def count_blocks(self):
        if self.is_empty():
            return 0
        if self._is_full():
            return self.amount_blocks
        low, high = 0, self.amount_blocks -1
        while low <= high:
            mid = (low + high) // 2
            if self.blocks[mid].name:
                if self.blocks[mid + 1].name:
                    low = mid + 1
                else:
                    return mid + 1
            else:
                high = mid - 1

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