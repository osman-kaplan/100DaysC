
from art import logo

def sum_num(num1,num2):
    return num1 + num2

def substract_num(num1,num2):
    return num1 - num2

def divide_num(num1,num2):
    return num1 / num2

def multiply_num(num1,num2):
    return num1 * num2


operations_dict = {
    '+':sum_num,
    '-': substract_num,
    '/': divide_num,
    '*': multiply_num

}





def calculate():
    print(logo)
    num1= float(input('Num1 > '))
    should_continue = True  # Flag


    while should_continue:

        for oper in operations_dict.keys():
            print(oper)

        operation_input= input('Oper > ')

        num2= float(input('Num > '))



        operation= operations_dict[operation_input]

        result= (operation(num1,num2))

        print(f'{num1} {operation_input} {num2} ={result}')

        response_flow= input('(C)ontinue/(S)top/(D)elete ?> ')

        if response_flow.lower().startswith('c'):
            num1= result

        elif response_flow.lower().startswith('s'):
            should_continue =False
        elif response_flow.lower().startswith('d'):
            calculate()
        else:
            print('Invalid input')
        
calculate()  

    



