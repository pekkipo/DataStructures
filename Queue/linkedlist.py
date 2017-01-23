class LinkedList:
    """
    You should implement the methods of this class which are currently
    raising a NotImplementedError!
    Don't change the name of the class or any of the methods.
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_start_to_list(self, node):

        if self.__root:  # if is not None
            node.set_next(self.__root)
        self.__root = node

    def remove_end_from_list(self):
        # basically iterate over the node
        # trying to find the penultimate node by checking the following node's next parameter

        marker = self.__root
        # deal with one node only
        if not marker.get_next():
            self.__root = None
            return marker

        # scheme [marker, following_node, following_node.get_next(), None]
        while marker:
            following_node = marker.get_next()
            if following_node:
                # if the next Node's next node is None -> marker is a second-to-last node
                if not following_node.get_next():
                    marker.set_next(None)
                    return following_node # the node that we deleted
            else:
                marker = marker.get_next()
        # - Iterate over each node
        # - Find both the second-to-last node and the last node
        # - Set the second-to-last node's next to be None
        # - Return the last node
        # :return: the removed Node.

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

    def size(self):
        marker = self.__root
        count = 0
        while marker:
            count += 1
            marker = marker.get_next()
        return count
