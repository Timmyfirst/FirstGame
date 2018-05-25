

class Linepart(object):

    def __init__(self, id, listpart, y):

        self._id = id
        self.list_part = listpart
        self._y = y

    def get_list_part(self):
        return self.list_part

    def get_y(self):
        return self._y

    def get_id(self):
        return self._id