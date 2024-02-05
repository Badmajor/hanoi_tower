class UnsuitableBlock(BaseException):
    def __init__(self, message='Unsuitable block'):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class EmptyColumn(BaseException):
    def __str__(self):
        return 'Empty column'
