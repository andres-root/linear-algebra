

# Sum a list of vectors
def sum(self, vectors):
    # TODO: Add valitadion for vector size
    return [sum(x) for x in zip(*vectors)]


# Substract a list of vectors
def sub(self, vectors):
    # TODO: Add valitadion for vector size
    return [reduce(lambda a, b: a - b, x) for x in zip(*vectors)]


# Multiply a vector by a scalar
def mult(self, scalar, vector):
    return [(scalar * x) for x in vector]
