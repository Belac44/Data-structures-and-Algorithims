# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            

        if next in ")]}":
            if next == "}" and opening_brackets_stack[-1] == "{":
                opening_brackets_stack.pop()
                
            elif next == ")" and opening_brackets_stack[-1] == "(":
                opening_brackets_stack.pop()
                
            elif next == "]" and opening_brackets_stack[-1] == "[":
                opening_brackets_stack.pop()
                
            else:
                return f"{i+1}"
    
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return f"{len(text)}"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()