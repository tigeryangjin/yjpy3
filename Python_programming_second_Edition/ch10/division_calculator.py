print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("First number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("除数不能为0！")
    except ValueError:
        print("非数字不能相除")
    else:
        print(answer)
