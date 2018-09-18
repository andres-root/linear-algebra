

class Vector:
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates ust be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates


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
