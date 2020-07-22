def write_fibonacci(file, stop, number1=0, number2=1):
    number3 = number1 + number2
    if number3 >= stop:
        return
    file.write(str(number2)+' ')
    write_fibonacci(file, stop, number2, number3) 


if __name__ == "__main__":
    fib_length = int(input("Enter max value for generating the fibonacci sequence:"))
    with open("fibonacci.txt", 'w') as file:
        write_fibonacci(file, fib_length)
