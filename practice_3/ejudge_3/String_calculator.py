nums = {
    "ONE": '1', "TWO": '2', "THR": '3', "FOU": '4', "FIV": '5', 
    "SIX": '6', "SEV": '7', "EIG": '8', "NIN": '9', "ZER": '0'
}

nums_reverse = {
    "1": "ONE", "2": 'TWO', "3": 'THR', "4": 'FOU', "5": 'FIV', 
    "6": 'SIX', "7": 'SEV', "8": 'EIG', "9": 'NIN', "0": 'ZER'
}

def main():
    expression = input()
    num_exp, type_exp = transform(expression)
    calculated_exp = calculate(num_exp, type_exp)
    final_exp = transform_back(calculated_exp, type_exp)

    print(final_exp)

def transform(exp):
    new_exp = ""
    
    index_exp = None

    for char in exp:
        if char in ['*', "/", "+", "-"]:
            type_exp = char
            index_exp = exp.index(char)

            break

    length = round(len(exp)/3)

    l, r = 0, 3
    for _ in range(length):
        if l == index_exp:
            l += 1
            r = l + 3
            new_exp += type_exp

        curr_num = exp[l:r]
        new_exp += nums[curr_num]

        l += 3
        r = l + 3

    return new_exp, type_exp

def calculate(exp, type_exp):
    first_num, second_num = exp.split(type_exp)

    match type_exp:
        case "*":
            return (int(first_num) * int(second_num))
        case "/":
            return (int(first_num) / int(second_num))
        case "+":
            return (int(first_num) + int(second_num))
        case "-":
            return (int(first_num) - int(second_num))

def transform_back(exp, type_exp):
    new_exp = ""
    exp = str(exp)
    for num in exp:
        if num == type_exp:
            new_exp += type_exp
        
        new_exp += nums_reverse[num]
    
    return new_exp

if __name__ == "__main__":
    main()
# -----------------------------------------------------------------------------------------------------------------
# upgraded version of my code 

WORD_TO_DIGIT = {
    "ONE": '1', "TWO": '2', "THR": '3', "FOU": '4', "FIV": '5', 
    "SIX": '6', "SEV": '7', "EIG": '8', "NIN": '9', "ZER": '0'
}

DIGIT_TO_WORD = {v: k for k, v in WORD_TO_DIGIT.items()}

OPERATORS = {'+', '-', '*', '/'}


def main():
    expression = input()
    
    # Convert word expression to numeric
    numeric_exp, operator = parse_expression(expression)
    
    # Calculate result
    result = evaluate(numeric_exp, operator)
    
    # Convert result back to word format
    word_result = to_word_expression(result, operator)
    
    print(word_result)


def parse_expression(exp):
    """Convert word-based expression to numeric format."""
    numeric = ""
    operator = None
    
    # Process in chunks of 3 characters
    i = 0
    while i < len(exp):
        chunk = exp[i:i+3]
        
        if chunk in WORD_TO_DIGIT:
            numeric += WORD_TO_DIGIT[chunk]
            i += 3
        elif exp[i] in OPERATORS:
            operator = exp[i]
            numeric += exp[i]
            i += 1
        else:
            i += 1
    
    return numeric, operator


def evaluate(expression, operator):
    """Evaluate the numeric expression."""
    left, right = expression.split(operator)
    left, right = int(left), int(right)
    
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b  # Integer division
    }
    
    return operations[operator](left, right)


def to_word_expression(result, operator):
    """Convert numeric result back to word format."""
    result_str = str(result)
    word_exp = ""
    
    for char in result_str:
        if char == '-':  # Handle negative numbers
            word_exp += '-'
        else:
            word_exp += DIGIT_TO_WORD[char]
    
    return word_exp


if __name__ == "__main__":
    main()