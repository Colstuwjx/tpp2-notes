# coding=utf-8

# 1. parse cmds and args
# 2. do operations

# example
# 1. P 2
# 2. D #
# 3. W 2
# 4. N 1
# 5. E 2
# 6. S 1
# 7. U #


_code_select_pen = 'P'
_code_pen_down = 'D'
_code_pen_up = 'U'
_code_draw_west = 'W'
_code_draw_north = 'N'
_code_draw_east = 'E'
_code_draw_south = 'S'
_code_null = ''


def _doPenUp(*args):
    if len(args) != 0:
        raise Exception('no need input for {}, got {}'.format(
            _code_pen_up, args
        ))
    # do your job.
    print("did pen up")


def _doDrawWest(*args):
    if len(args) != 1:
        raise Exception('invalid input for {}'.format(
            _code_draw_west
        ))
    # do your job.
    print("did draw west with arg {}".format(args))


def _doDrawNorth(*args):
    if len(args) != 1:
        raise Exception('invalid input for {}'.format(
            _code_draw_north
        ))
    # do your job.
    print("did draw north with arg {}".format(args))


def _doDrawEast(*args):
    if len(args) != 1:
        raise Exception('invalid input for {}'.format(
            _code_draw_east
        ))
    # do your job.
    print("did draw east with arg {}".format(args))


def _doDrawSouth(*args):
    if len(args) != 1:
        raise Exception('invalid input for {}'.format(
            _code_draw_south
        ))
    # do your job.
    print("did draw south with arg {}".format(args))


def _doNothing(*args):
    # do nothing.
    pass


def _doSelectPen(*args):
    if len(args) != 1:
        raise Exception('invalid input for {}'.format(
            _code_select_pen
        ))
    # do your job.
    print("did select pen with arg {}".format(args))


def _doPenDown(*args):
    if len(args) != 0:
        raise Exception('no need input for {}, got {}'.format(
            _code_pen_down, args
        ))
    # do your job.
    print("did pen down")


_commands = [
    _doSelectPen, _doPenDown, _doPenUp,
    _doDrawWest, _doDrawNorth, _doDrawEast, _doDrawSouth,
    _doNothing,
]

_commands_table = {
    _code_select_pen: _doSelectPen,
    _code_pen_down: _doPenDown,
    _code_draw_west: _doDrawWest,
    _code_draw_north: _doDrawNorth,
    _code_draw_east: _doDrawEast,
    _code_draw_south: _doDrawSouth,
    _code_pen_up: _doPenUp,
    _code_null: _doNothing,
}


class Runnable(object):
    def __init__(self, code, func, *args):
        self.code = code
        self.func = func
        self.args = args

    def run(self):
        return self.func(*self.args)


class TurtlePainter(object):
    '''
    Turtle painter.
    it read cmds from stdin, parse and execute.
    '''

    def _parse_line(self, line):
        # read line and parse it.
        cmd_parts = line.split()
        cmd_length = len(cmd_parts)
        if cmd_length == 0:
            return Runnable(_code_null, _doNothing)
        cmd_code = cmd_parts[0]
        if cmd_code not in _commands_table.keys():
            raise Exception('invalid code {}'.format(cmd_code))
        cmd_func = _commands_table[cmd_code]
        cmd_args = cmd_parts[1:] if cmd_length >= 2 else []
        return Runnable(cmd_code, cmd_func, *cmd_args)

    def parse_and_exec(self, readable):
        content = readable.read()
        for line in content.split('\n'):
            block = self._parse_line(line)
            block.run()


if __name__ == '__main__':
    with open('test-cmd-input.txt', 'r') as fp:
        tp = TurtlePainter()
        tp.parse_and_exec(fp)
