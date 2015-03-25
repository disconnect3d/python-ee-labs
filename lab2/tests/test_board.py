# coding=utf-8
import unittest
import itertools

from board import Board, BoardIndexError, BoardPutMarkerError


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.players_markers = ('x', 'o')
        self.empty_marker = ' '

        self.test_data = (
            (3, Board(3, self.players_markers, self.empty_marker)),
            (5, Board(5, self.players_markers, self.empty_marker)),
            (7, Board(7, self.players_markers, self.empty_marker))
        )

    def test_board_init_size_assert(self):
        for too_small_size in xrange(2, -10, -1):
            self.assertRaises(AssertionError, Board, too_small_size, self.players_markers, self.empty_marker)

        for not_parity_size in xrange(4, 16, 2):
            self.assertRaises(AssertionError, Board, not_parity_size, self.players_markers, self.empty_marker)

    def test_board_init_wrong_empty_marker_assert(self):
        for wrong_marker in self.__invalid_markers():
            self.assertRaises(AssertionError, Board, 3, self.players_markers, wrong_marker)

    def test_board_init_wrong_players_marker_assert(self):
        for wrong_marker in self.__invalid_markers():
            self.assertRaises(AssertionError, Board, 3, [wrong_marker], self.empty_marker)

    def test_valid_coord_xy_valid(self):
        for size, board in self.test_data:
            for x, y in self.__valid_xy_gen(size):
                self.assertTrue(board.is_valid_coord(x, y))

    def test_valid_coord_index_valid(self):
        for size, board in self.test_data:
            for expected_valid_index in self.__valid_index_gen(size):
                self.assertTrue(board.is_valid_coord(expected_valid_index))

    def test_valid_coord_invalid_xy(self):
        for size, board in self.test_data:
            for x, y in self.__invalid_xy_gen(size):
                self.assertFalse(board.is_valid_coord(x, y))

    def test_valid_coord_invalid_index(self):
        for size, board in self.test_data:
            for expected_invalid_index in self.__invalid_index_gen(size):
                self.assertFalse(board.is_valid_coord(expected_invalid_index))

    def test_is_empty_valid_xy(self):
        for size, board in self.test_data:
            for x, y in self.__valid_xy_gen(size):
                self.assertTrue(board.is_empty(x, y))

    def test_is_empty_invalid_xy(self):
        for size, board in self.test_data:
            for x, y in self.__invalid_xy_gen(size):
                self.assertRaises(BoardIndexError, board.is_empty, x, y)

    def test_is_empty_valid_index(self):
        for size, board in self.test_data:
            for index in self.__valid_index_gen(size):
                self.assertTrue(board.is_empty(index))

    def test_is_empty_invalid_index(self):
        for size, board in self.test_data:
            for index in self.__invalid_index_gen(size):
                self.assertRaises(BoardIndexError, board.is_empty, index)

    def test_put_valid_xy(self):
        for size, board in self.test_data:
            for x, y in self.__valid_xy_gen(size):
                marker = self.players_markers[0]
                self.assertTrue(board.is_empty(x, y))

                board.put(marker, x, y)

                self.assertFalse(board.is_empty(x, y))
                self.assertEqual(marker, board[x][y])

    def test_put_invalid_xy(self):
        for size, board in self.test_data:
            for x, y in self.__invalid_xy_gen(size):
                self.assertRaises(BoardIndexError, board.put, self.players_markers[0], x, y)

    def test_put_valid_index(self):
        for size, board in self.test_data:
            for index in self.__valid_index_gen(size):
                marker = self.players_markers[0]
                self.assertTrue(board.is_empty(index))
                board.put(marker, index)
                self.assertFalse(board.is_empty(index))
                x, y = board._get_xy_from_index(index)
                self.assertEqual(marker, board[x][y])

    def test_put_invalid_index(self):
        for size, board in self.test_data:
            for index in self.__invalid_index_gen(size):
                self.assertRaises(BoardIndexError, board.put, self.players_markers[0], index)

    def test_put_invalid_marker(self):
        for size, board in self.test_data:
            for x, y in self.__valid_xy_gen(size):
                for invalid_marker in self.__invalid_markers():
                    self.assertRaises(BoardPutMarkerError, board.put, invalid_marker, x, y)

            for index in self.__valid_index_gen(size):
                for invalid_marker in self.__invalid_markers():
                    self.assertRaises(BoardPutMarkerError, board.put, invalid_marker, index)

    def __valid_xy_gen(self, size):
        return ((x, y) for x in xrange(size) for y in xrange(size))

    def __valid_index_gen(self, size):
        return xrange(size ** 2 - 1)

    def __invalid_xy_gen(self, size):
        return itertools.chain(((-x, -y) for x in xrange(1, size) for y in xrange(1, size)),
                               ((x, y) for x in xrange(size, 2 * size) for y in xrange(size, 2 * size)))

    def __invalid_index_gen(self, size):
        return itertools.chain(xrange(-1, -15, -1),
                               xrange(size ** 2, 2 * (size ** 2)))

    def __invalid_markers(self):
        return None, 1, 2.2, u'łżźć', u's', 'as'


if __name__ == '__main__':
    unittest.main()
