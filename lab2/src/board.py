import os


class BoardIndexError(Exception):
    pass


class BoardPutMarkerError(Exception):
    pass


class Board(object):
    def __init__(self, size, players_markers, empty_marker):
        assert size >= 3
        assert size % 2 == 1

        self._players_markers = players_markers
        self._empty_marker = empty_marker
        self._valid_markers = tuple(self._players_markers) + (self.empty_marker,)
        assert all((isinstance(marker, str) and len(marker) == 1 for marker in self._valid_markers))

        self._size = size
        self._board = [[empty_marker for i in xrange(size)] for i in xrange(size)]

    @property
    def size(self):
        return self._size

    @property
    def empty_marker(self):
        return self._empty_marker

    @property
    def valid_markers(self):
        return self._valid_markers

    @property
    def players_markers(self):
        return self._players_markers

    def get_index_range(self):
        return [0, self.size ** 2]

    def put(self, marker, x, y=None):
        self._validate_coords(x, y)

        if marker not in self._valid_markers:
            raise BoardPutMarkerError("Passed marker is not valid. Valid markers: {}".format(self._valid_markers))

        if y is None:
            x, y = self._get_xy_from_index(x)
        self._board[x][y] = marker

    def is_empty(self, x, y=None):
        self._validate_coords(x, y)

        if y is None:
            x, y = self._get_xy_from_index(x)

        return self._board[x][y] == self._empty_marker

    def _validate_coords(self, x, y):
        if not self.is_valid_coord(x, y):
            raise BoardIndexError("Passed coordinates are not valid.")

    def is_valid_coord(self, x, y=None):
        if y is None:
            return 0 <= x < self._size * self._size
        else:
            return (0 <= x < self._size) and (0 <= y < self._size)

    def formatted(self):
        newline = os.linesep + '-' * (self._size * 2 - 1) + os.linesep
        return newline.join(('|'.join((self._board[x][y] for x in xrange(self._size))) for y in xrange(self._size)))

    def _get_xy_from_index(self, index):
        x = index / self._size
        y = index % self._size
        return x, y

    def __getitem__(self, x):
        return self._board[x]
