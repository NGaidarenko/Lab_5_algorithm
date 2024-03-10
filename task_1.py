def check_brackets(data):
    stack = []
    for i, char in enumerate(data):
        if char == '(':
            stack.append(('(', i))
        elif char == ')':
            if not stack:
                return i
            stack.pop()

    if stack:
        return stack[-1][1]
    return 0


data = input("Введите скобочное выражение: ")
result = check_brackets(data)
if result == 0:
    print("Скобочное выражение правильное.")
else:   
    print(f"Ошибка в позиции {result}.")
