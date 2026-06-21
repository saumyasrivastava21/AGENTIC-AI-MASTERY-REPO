import ast
import operator as op


_ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
}


def _eval_node(node):
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numbers are allowed.")

    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        operator_type = type(node.op)

        if operator_type not in _ALLOWED_OPERATORS:
            raise ValueError("Operator not allowed.")

        return _ALLOWED_OPERATORS[operator_type](left, right)

    if isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand)
        operator_type = type(node.op)

        if operator_type not in _ALLOWED_OPERATORS:
            raise ValueError("Unary operator not allowed.")

        return _ALLOWED_OPERATORS[operator_type](operand)

    raise ValueError("Invalid expression.")


def calculator_tool(expression: str) -> str:
    try:
        tree = ast.parse(expression, mode="eval")
        result = _eval_node(tree.body)
        return f"Calculation result: {result}"

    except Exception as e:
        return f"Calculator error: {str(e)}"