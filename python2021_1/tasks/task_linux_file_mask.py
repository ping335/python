class MaskItem(object):
    READ = 0b100
    WRITE = 0b10
    EXECUTE = 0b1

    def __init__(self, mask=0):
        self.mask = mask

    def __repr__(self):
        mask = f'{self.mask:#b}' if self.mask else ''
        return f'{self.__class__.__name__}({mask})'

    def __str__(self):
        return '{}{}{}'.format(
            'r' if self.is_readable() else '-',
            'w' if self.is_writable() else '-',
            'x' if self.is_executable() else '-'
        )

    def is_executable(self):
        return bool(self.mask & self.EXECUTE)

    def is_readable(self):
        return bool(self.mask & self.READ)

    def is_writable(self):
        return bool(self.mask & self.WRITE)


class Mask(object):
    def __init__(self, author, group, other):
        self.author = author
        self.group = group
        self.other = other

    def __repr__(self):
        return '{}({!r}, {!r}, {!r})'.format(
            self.__class__.__name__, self.author, self.group, self.other
        )

    def __str__(self):
        return f'{self.author}{self.group}{self.other}'


if __name__ == '__main__':
    mask = Mask(
        MaskItem(MaskItem.READ | MaskItem.EXECUTE),
        MaskItem(MaskItem.READ | MaskItem.EXECUTE),
        MaskItem(MaskItem.READ | MaskItem.EXECUTE)
    )

    print(mask, repr(mask), repr(MaskItem()))
