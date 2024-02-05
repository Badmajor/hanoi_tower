import time

from classes import HanoiTower
from settings import DELAY


def move_block(source_column: int, target_column: int):
    """Moving one block"""
    block = tower.columns[source_column].retrieve_block()
    tower.columns[target_column].add_block(block)
    print(f'Block: {block} | {source_column + 1} -> {target_column + 1}')
    print(tower)
    time.sleep(DELAY)

def move_tower(amount_blocks: int,
               source_column: int,
               target_column: int,
               auxiliary_column: int):
    if amount_blocks > 0:
        move_tower(amount_blocks - 1, source_column, auxiliary_column, target_column)
        move_block(source_column, auxiliary_column)
        move_tower(amount_blocks -1, target_column, source_column, auxiliary_column)


def main():
    amount_blocks = int(input('Введи количество фишек:'))
    global tower
    tower = HanoiTower(amount_blocks)
    move_tower(amount_blocks, 0, 1, 2)



if __name__ == '__main__':
    main()
