from utils.helpers import *
from utils.validation import checking_division_by_0

def make_list(instructions):
    ''' Makes list with independant terms of entered expression '''
    list_calculus = []
    index = 0
    for char_index in range(len(instructions)):
        print("char_index: {}, value: {}".format(char_index, instructions[char_index]))
        if instructions[char_index] in VALID_OPERATORS+PARENTHESIS_SIMBOLS:
            if instructions[index:char_index] != '':
                list_calculus.append(int(instructions[index:char_index]))
            list_calculus.append(instructions[char_index])    # OK
            index = char_index + 1
        # LAST NUMBER
        if char_index == len(instructions) - 1 :
            if instructions[index:len(instructions)] != '':
                list_calculus.append(int(instructions[index:len(instructions)]))
    print("\nList_terms: "+str(list_calculus)+"\n")
    return list_calculus

def make_operation(number1, number2, operator):
    ''' Performs a single operation between two numbers '''
    if operator == ":" or operator == "/" :
        reduced_member = checking_division_by_0(number1, number2)
    elif operator == "*" :
        reduced_member = number1*number2
    elif operator == "+" :
        reduced_member = number1+number2
    else:                                   # operator == "-" 
        reduced_member = number1-number2
    return reduced_member

# EXAMPLE : [23, '+', 34, '-', 98, ':', 29, '/', 34, '/', 98]
def reduce_members(list_calculus):
    ''' Prioritize order of operations 
        *, :, / in order that appears before +, -
    '''
    while True:
        if "*" in list_calculus or ":" in list_calculus or "/" in list_calculus:
            for operator_index in range(1,len(list_calculus),2):
                print("Operator index - 1: {}, value: {}".format(operator_index-1, list_calculus[operator_index-1]))
                print("Operator index: {}, value: {}".format(operator_index, list_calculus[operator_index]))
                print("Operator index + 1: {}, value: {}".format(operator_index+1, list_calculus[operator_index+1]))
                if list_calculus[operator_index] in PRIORITY_OPERATORS :
                    temp = make_operation(list_calculus[operator_index-1],list_calculus[operator_index+1],list_calculus[operator_index])
                    list_calculus[operator_index-1] = temp
                    del list_calculus[operator_index:operator_index+1+1] # Plus extra, sublist structure: [initial:final)
                    print("Reduced_member: "+str(list_calculus)+"\n")
                    break
                else:
                    print(PRIORITY_MESSAGE)
                    pass
        else:
            for operator_index in range(1,len(list_calculus),2):
                print("Operator index - 1: {}, value: {}".format(operator_index-1, list_calculus[operator_index-1]))
                print("Operator index: {}, value: {}".format(operator_index, list_calculus[operator_index]))
                print("Operator index + 1: {}, value: {}".format(operator_index+1, list_calculus[operator_index+1]))
                temp = make_operation(list_calculus[operator_index-1],list_calculus[operator_index+1],list_calculus[operator_index])
                list_calculus[operator_index-1] = temp
                del list_calculus[operator_index:operator_index+1+1] # Plus extra, sublist structure: [initial:final)
                print("Reduced_member: "+str(list_calculus)+"\n")
                break
        if len(list_calculus) == 1:
            return list_calculus[0]
        else:
            pass
        
def calculate(main_list):
    ''' Reduce parenthesis expressions and final expression '''
    while True:
        start_parenthesis = 0
        end_parenthesis = 0
        for index in range(len(main_list)):
            if '(' in main_list:
                if main_list[index] == "(":
                    start_parenthesis = index
                if main_list[index] == ")":
                    end_parenthesis = index
                if end_parenthesis:
                    print("Parenthesis: {}".format(main_list[start_parenthesis+1:end_parenthesis]))
                    temp = reduce_members(main_list[start_parenthesis+1:end_parenthesis])
                    main_list[start_parenthesis] = temp
                    del main_list[start_parenthesis+1:end_parenthesis+1] # Plus extra, sublist structure: [initial:final)
                    print("Main_remaining_list_terms: "+str(main_list)+"\n") # h is just iindicator to identify when there was a parenthesis
                    break
            else:
                main_list = reduce_members(main_list)
                print("Final exact result: "+str(main_list)) # This is supposed to happen when there is just one term
                print("Type final result: {}\n".format(str(type(main_list)))) 
                if str(type(main_list)) == "<class 'int'>":
                    return main_list
                elif str(type(main_list)) == "<class 'float'>":
                    return round(main_list, 2)
                else:
                    pass