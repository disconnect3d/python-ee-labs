from __future__ import print_function
from constants import Message
from utils import logger_injector


@logger_injector
class TickTackToe(object):
    def __init__(self, player1, player2, board):
        self._player1 = player1
        self._player2 = player2

        self._players_markers = {
            player1.marker: player1,
            player2.marker: player2
        }

        assert len(self._players_markers) == 2

        self._board = board
        self._player1._board = self._board
        self._player2._board = self._board

        self.winner = None

    def game_loop(self):
        self.logger.info("Game started with p1={}, p2={}".format(self._player1, self._player2))
        self._moves_done = 0
        self._min_moves_to_win = self._board.size * 2 - 1
        self._max_moves = self._board.size**2

        while True:
            self._make_player_valid_move(self._player1)

            print (self._board.formatted())
            if self.is_game_over():
                break

            self._make_player_valid_move(self._player2)
            print (self._board.formatted())
            if self.is_game_over():
                break

    def _make_player_valid_move(self, player):
        x, y = player.move()

        while True:
            if not self._board.is_valid_coord(x, y):
                player.inform(Message.INVALID_INPUT_COORDS)
            elif not self._board.is_empty(x, y):
                player.inform(Message.FIELD_NOT_EMPTY)
            else:
                break
            x, y = player.move()

        self._board.put(player.marker, x, y)

        self._moves_done += 1

    def is_game_over(self):
        if self._moves_done < self._min_moves_to_win:
            return False

        winner = self._check_winner()
        if winner != self._board.empty_marker:
            self.winner = winner
            return True

        if self._is_tie():
            return True

        return False

    def _check_winner(self):
        board = self._board
        size = board.size

        for row in xrange(size):
            if not board.is_empty(row, 0):
                first = board[row][0]
                if all((board[row][i] == first for i in xrange(1, size))):
                    return first

        for col in xrange(size):
            if not board.is_empty(0, col):
                first = board[0][col]
                if all((board[i][col] == first for i in xrange(1, size))):
                    return first

        first = board[0][0]
        if not first == board.empty_marker:
            if all(board[i][i] == first for i in xrange(1, size)):
                return first

        first = board[0][size-1]
        if not first == board.empty_marker:
            if all(board[i][size-1-i] == first for i in xrange(1, size)):
                return first

        return board.empty_marker

    def _is_tie(self):
        return self._moves_done == self._max_moves

    def get_result(self):
        if self.winner in self._players_markers:
            return "Won player {}".format(self._players_markers[self.winner])

        return "Tie!"
