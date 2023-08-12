class tree:
    def __init__(self, Data):
        self.right = None
        self.left = None
        self.node = Data

    def show(self):
        if self.right:
            self.right.show()
        print(self.node)
        if self.left:
            self.left.show()

    def insert(self, new_data):
        if new_data > self.node:
            if self.right is None:
                self.right = tree(new_data)
            else:
                self.right.insert(new_data)
        elif new_data < self.node:
            if self.left is None:
                self.left = tree(new_data)
            else:
                self.left.insert(new_data)
