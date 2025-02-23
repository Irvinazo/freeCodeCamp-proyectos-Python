def arithmetic_arranger(problems, show_answers=False):

    #1 Length of problems must not be greater than 5
    if len(problems)>5:
        problems = "Error: Too many problems."
        return problems
    
    #2 The operators * and / must not be inside the string
    for problem in problems:
        for char in problem:
            if (char == '*') or (char == "/"):
                problems = "Error: Operator must be '+' or '-'."
                return problems
    
    #3 The operands must be numbers, not other kind of characters
        operands_in_problem = problem.split(' ')
        if operands_in_problem[0].isdigit()!=True or \
        operands_in_problem[2].isdigit()!=True:  
            problems = "Error: Numbers must only contain digits."
            return problems
    
    #4 The numbers cannot be more than four digits
        else: 
            for char in operands_in_problem:
                if len(char)>4:
                    problems = "Error: Numbers cannot be more than four digits."
                    return problems

    # Let's create three different lists, each of them having the above, 
    # operand and below numbers for the operation
    above_numbers = [problem.split(' ')[0] for problem in problems]
    operand_sign = [problem.split(' ')[1] for problem in problems]
    below_numbers = [problem.split(' ')[2] for problem in problems]

    # Let's create spaces for the first line
    spaces_first_line = [' '*2 \
                        if len(above_numbers[i])>=len(below_numbers[i]) \
                        else ' '*(2+len(below_numbers[i])-len(above_numbers[i])) \
                        for i in range(len(above_numbers))]
    #Now we concatente the spaces with the above numbers
    first_line = list(map(str.__add__, spaces_first_line, above_numbers))
    #Finally, as there must be four spaces between the operations, we add them
    first_line_str = '    '.join(first_line)
    
    # Now we create spaces for the second line, and repeat the process
    spaces_second_line = [' '*(1+len(above_numbers[i])- \
    len(below_numbers[i])) if len(above_numbers[i])>=len(below_numbers[i]) \
    else ' ' for i in range(len(above_numbers))]

    second_line_ = list(map(str.__add__,operand_sign,spaces_second_line))
    second_line = list(map(str.__add__,second_line_,below_numbers))
    second_line_str = '    '.join(second_line)

    # Now, we create the separating lines for the third line
    lines_third_line = ['-'*(2+max(len(above_numbers[i]), \
    len(below_numbers[i]))) for i in range(len(above_numbers))]
    third_line_str = '    '.join(lines_third_line)

    #Finally, we'll create an answer line if second parameter is set to true
    aux_1 = [int(num) for num in above_numbers]
    aux_2 = [int(num) for num in below_numbers]
    
    answers_third_line = [str(aux_1[i]+aux_2[i]) if operand_sign[i]=='+' else str(aux_1[i]-aux_2[i]) for i in range(len(aux_1))]
    
    spaces_third_line = [' '*(len(lines_third_line[i])-len(answers_third_line[i])) for i in range(len(above_numbers))]
    fourth_line_str = list(map(str.__add__,spaces_third_line,answers_third_line))
    fourth_line_str = '    '.join(fourth_line_str)
    
    if show_answers == True:
        problems = f'{first_line_str}\n{second_line_str}\n{third_line_str}\n{fourth_line_str}'
        return problems
    else:
        problems = f'{first_line_str}\n{second_line_str}\n{third_line_str}'
        return problems

