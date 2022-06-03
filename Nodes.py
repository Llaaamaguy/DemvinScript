class VarNode:
    def __init__(self, varName, varValue):
        self.varName = varName
        self.varValue = varValue

    def __repr__(self):
        return str(self.varValue)

    def __str__(self):
        return str(self.varValue)


class StrNode:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return self.string

    def __str__(self):
        return self.string


class IntNode:
    def __init__(self, value):
        self.value = int(value)

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

    def eval(self):
        return self.value


class FloatNode:
    def __init__(self, value):
        self.value = float(value)

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

    def eval(self):
        return self.value


class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()


class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()


class TrueDivNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() / self.right.eval()


class FloorDivNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() // self.right.eval()


class ListNode:
    def __init__(self, vals):
        self.vals = vals

    def __repr__(self):
        return str(self.vals)

    def __str__(self):
        return str(self.vals)

    def __iter__(self):
        for i in self.vals:
            yield i


