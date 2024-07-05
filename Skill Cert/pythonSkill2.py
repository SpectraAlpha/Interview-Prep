class Multiset:
    def __init__(self):
        self.elements = []

    def add(self, val):
        # adds one occurrence of val to the multiset
        self.elements.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if val in self.elements:
            self.elements.remove(val)

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.elements

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.elements)
