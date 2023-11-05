print('\033[38;5;220mSIMPLE CALCULATOR\033[0m')
print('\033[96mThis is a basic calculator\033[0m')
print('''\033[95mENTER THE OPTIONS ACCORDING TO THE ACTIONS YOU WANT TO PERFORM \033[0m
    \033[94mTABLE GENERATOR\033[0m:\033[93m 1 \033[0m
    \033[94mADDITION\033[0m:\033[93m 2\033[0m
    \033[94mSUBTRACTION\033[0m:\033[93m 3\033[0m
    \033[94mMULTIPLICATION\033[0m:\033[93m 4\033[0m
    \033[94mDIVISION\033[0m:\033[93m 5\033[0m
    \033[94mEXPONENTIATION\033[0m:\033[93m 6\033[0m''')
print('(PRESS \033[91m exit\033[0m WHEN YOU NO LONGER NEED THE LOOP)')
exit_p = False

while True:
    while True:
        w = input('\033[38;5;154mEnter the value for the corresponding action:\033[0m ')
        if w.lower() == 'exit':
            exit_p = True
            break
        if w in ['1', '2', '3', '4', '5', '6']:
            break
        else:
            print('\033[91mEnter a valid value!!\033[0m')
    if exit_p:
        break

    if w == '1':
        print('\033[38;5;45mTABLE GENERATOR\033[0m')
        while True:
            try:
                x = input('Enter the number for the required table: ')
                if x.lower() == 'exit':
                    break
                x = int(x)
                for i in range(10):
                    print(f'{x} X {i + 1} = {x * (i + 1)}')
            except ValueError:
                print('\033[91mInvalid input\033[0m')
                break

    elif w == '2':
        print(' \033[38;5;45m ADDITION \033[0m')
        while True:
            try:
                numbers = input("Enter the numbers (separated by spaces): ")
                if numbers.lower() == 'exit':
                    break
                number_list = numbers.split()

                summation = 0
                for num_str in number_list:
                    num = int(num_str)
                    summation += num

                print(f'The sum is: \033[92m{summation}\033[0m' )
                continue
            except ValueError:
                print('\033[91mInvalid input\033[0m')
                continue

    elif w == '3':
        print('\033[38;5;45mSUBTRACTION\033[0m')
        while True:
            try:
                numbers = input("Enter the numbers (separated by spaces): ")
                if numbers.lower() == 'exit':
                    break

                number_list = numbers.split()

                subtraction = int(number_list[0])
                for num_str in number_list[1:]:
                    num = int(num_str)
                    subtraction -= num

                print(f'The subtraction result is: \033[92m{subtraction}\033[0m ')
                continue
            except ValueError:
                print('\033[91mInvalid input\033[0m')
                continue

    elif w == '4':
        print('\033[38;5;45mMULTIPLICATION\033[0m')
        while True:
            numbers = input("Enter the numbers (separated by spaces): ")
            if numbers.lower() == 'exit':
                break
            number_list = numbers.split()

            product = 1
            for num_str in number_list:
                num = int(num_str)
                product *= num

            print(f'The product is: \033[92m{product}\033[0m' )
            continue

    elif w == '5':
        print('\033[38;5;45mDIVISION\033[0m')
        while True:
            try:
                numbers = input("Enter the numbers (separated by spaces): ")
                if numbers.lower() == 'exit':
                    break
                number_list = numbers.split()

                dividend = int(number_list[0])
                for num_str in number_list[1:]:
                    divisor = int(num_str)
                    dividend /= divisor

                print(f'The division result is: \033[92m{dividend}\033[0m ')
                continue

            except ValueError:
                print('\033[91mInvalid input\033[0m')
                continue
                        
    elif w == '6':
        print('\033[38;5;45mEXPONENTIATION\033[0m')
        while True:
            try:
                base = input("Enter the base number: ")
                if base.lower() == 'exit':
                    break
                exponent = input("Enter exponent number: ")
                if exponent.lower() == 'exit':
                    break

                base = int(base)
                exponent = int(exponent)
                result = base ** exponent

                print(f'The result of {base} raised to the power of {exponent} is: \033[92m{result}\033[0m ')
                continue
            except ValueError:
                print('\033[91mInvalid input\033[0m')
                continue
