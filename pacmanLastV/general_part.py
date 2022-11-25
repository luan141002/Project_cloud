from abc import ABC, abstractmethod


class Coin_search(ABC):

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def set_target(self):
        pass

    @abstractmethod
    def time_to_move(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def get_path_direction(self, target):
        pass

    @abstractmethod
    def find_next_cell_in_path(self, target):
        pass

    @abstractmethod
    def get_pix_pos(self):
        pass
