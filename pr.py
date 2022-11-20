def calc(n, m, operation):
    match operation:
        case "+":
            return int(n) + int(m)
        case "-":
            return int(n) - int(m)
        case "*":
            return int(n) * int(m)
        case "/":
            return int(n) / int(m)
        case _:
            print("Error")


inv_polish = ["3", "4", "5", "+", "*", "6", "1", "2", "+", "/", "-"]
like_stack = []

for i in range(len(inv_polish)):
    if inv_polish[i].isdigit():
        like_stack.append(inv_polish[i])
    else:
        temp = calc(like_stack[-2], like_stack[-1], inv_polish[i])
        like_stack.pop()
        like_stack.pop()
        like_stack.append(temp)
print(int(like_stack[-1]))
