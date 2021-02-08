# Set Up Stack With Size 10
stack = []
top_pointer = 0
null_pointer = 0
stack_limit = 10


def push(item):
    global top_pointer
    if top_pointer < stack_limit:
        top_pointer += 1
        stack.append(item)
    else:
        print("list full!")


def pop():
    item = None
    global top_pointer
    if top_pointer < null_pointer:
        print("list empty")
    else:
        item = stack[top_pointer]
        top_pointer -= 1
        return item
