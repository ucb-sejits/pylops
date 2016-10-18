import inspect
import ast

def get_func_ast(func):
    source = inspect.getsource(func)
    parsed = ast.parse(source)
    if len(parsed.body) == 1 and isinstance(parsed.body[0], ast.FunctionDef):
        return parsed.body[0]
    # go lambda hunting
    raise NotImplementedError("We don't support lambdas yet")
