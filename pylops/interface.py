import ast

import __builtin__

BUILTIN_OPS = {
    getattr(__builtin__, name) for name in dir(__builtin__)
}

class Operation(ast.AST):
    pass


class Reduction(Operation):
    """we define a reduction as a binary operation over a 1-d array"""
    _fields = ['op', 'array']


class PointwiseOperation(Operation):
    """A Pointwise Operation takes multiple arrays of the same shape, and an operation which takes multiple inputs."""
    _fields = ['op', 'arrays']
