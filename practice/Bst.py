class Root:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Root(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_root):
        if data < cur_root.data:
            if cur_root.left is None:
                cur_root.left = Root(data)
            else:
                self._insert(data, cur_root.left)
        if data > cur_root.data:
            if cur_root.right is None:
                cur_root.right = Root(data)
            else:
                self._insert(data, cur_root.right)

    def print_t(self):
        if self.root:
            self._print(self.root)

    def _print(self, cur_root):
        if cur_root.left:
            self._print(cur_root.left)
        print(cur_root.data)
        if cur_root.right:
            self._print(cur_root.right)


P = BST()

i=1
for i in range(10):
    P.insert(i)

P.print_t()
