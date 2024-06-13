# # Method 1
# def find_x(equation):
#     left_expr, right_value = equation.split("=")
#     right_value = int(right_value)

#     for x in range(1, 101):
#         left_eval = left_expr.replace("X", str(x))
#         try:
#             if eval(left_eval) == right_value:
#                 return x
#         except ZeroDivisionError:
#             continue

#     return None


# input_string = input()

# print(find_x(input_string))


# Method 2
def evaluate_expression(expr):
    def parse_term(term):
        factors = term.split("*")
        result = 1
        for factor in factors:
            if "/" in factor:
                numerator, denominator = map(int, factor.split("/"))
                result *= numerator / denominator
            else:
                result *= int(factor)
        return result

    def parse_expression(expression):
        terms = expression.split("+")
        result = 0
        for term in terms:
            if "-" in term:
                subterms = term.split("-")
                subtotal = parse_term(subterms[0])
                for subterm in subterms[1:]:
                    subtotal -= parse_term(subterm)
                result += subtotal
            else:
                result += parse_term(term)
        return result

    return parse_expression(expr)


def find_x(equation):
    left_expr, right_value = equation.split("=")
    right_value = int(right_value)

    for x in range(1, 101):
        left_eval = left_expr.replace("X", str(x))
        try:
            if evaluate_expression(left_eval) == right_value:
                return x
        except ZeroDivisionError:
            continue

    return None


input_string = input()

print(find_x(input_string))
