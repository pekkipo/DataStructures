class LinkedList:
    """
    This class is the one you should be modifying!
    Don't change the name of the class or any of the methods.

    Implement those methods that current raise a NotImplementedError
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_to_list(self, node):

        if self.__root: # if is not None
            node.set_next(self.__root)
        self.__root = node

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, name):

        marker = self.__root

        while marker:
            if marker.name == name:
                return marker
            else:
                marker = marker.get_next()
        raise LookupError("{} wasn't found".format(name))


