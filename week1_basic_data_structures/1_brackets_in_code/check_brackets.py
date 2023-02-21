# python3

from collections import namedtuple
import glob
import os

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            

        if next in ")]}":
            if len(opening_brackets_stack) > 0:
                if next == "}" and opening_brackets_stack[-1] == "{":
                    opening_brackets_stack.pop()
                    
                elif next == ")" and opening_brackets_stack[-1] == "(":
                    opening_brackets_stack.pop()
                    
                elif next == "]" and opening_brackets_stack[-1] == "[":
                    opening_brackets_stack.pop()
                    
                else:
                    return f"{i+1}"
            else:
                return f"{i+1}"
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return f"{len(text.strip())}"

def test():
    files = os.listdir('./tests')
    length = len(files)
    for i in range(0, length-1, 2):
        with open(f'./tests/{files[i]}') as file:
            content = file.read()
            feedback = find_mismatch(content)
            with open(f"./tests/{files[i+1]}") as data:
                label = data.read()
                if label.strip() == feedback:
                    print(f"Input:{content} Output:{feedback}  True value:{label}")
                else:
                    print(f"Broken with {content} Label:{label} Output:{feedback}")
                    print(f"At pos {i}: Total: {length}")
                    break



def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    test()