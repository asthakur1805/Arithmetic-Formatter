def arithmetic_arranger(problems,*args):
    
    # Error handling for more than five problems
    if len(problems) > 5:
      return 'Error: Too many problems.'
    
    operand1_list = list()
    operator_list = list()
    operand2_list = list()
    max_width_list = list()
    if len(args) == 1:
        result_list = list()
    
    # Traversing through the problems
    for problem in problems:
      problem_list = problem.split();
      operator = problem_list[1]
    
      # Error handling for operation other than addition and subtraction
      if operator not in ['+','-']:
        return "Error: Operator must be '+' or '-'."
      
      # Exception handling for traceback if the operands are not digits
      try:
        operand1 = int(problem_list[0])
        operand2 = int(problem_list[2])
      except:
        return "Error: Numbers must only contain digits."
    
      # Error handling for width more than four digits 
      if operand1 > 9999 or operand2 > 9999:
        return 'Error: Numbers cannot be more than four digits.'  
      
      operand1_list.append(operand1)
      operator_list.append(operator)
      operand2_list.append(operand2)
      
      operand1_width = get_width(operand1)
      operand2_width = get_width(operand2)
        
      if operand1_width >= operand2_width:
            max_width_list.append(operand1_width)
      else:
        max_width_list.append(operand2_width)
      
      # Result to be calculated only if optional boolean parameter True passed
      if len(args) == 1:
        if(operator=='+'):
            result_list.append(operand1+operand2)
        else:
            result_list.append(operand1-operand2)
    
    arranged_problems = ''
    
    # Generation of operand1 format string 
    for index in range(0,len(problems)-1):
        width = max_width_list[index]+2
        arranged_problems+=f'{operand1_list[index]:>{width}}    '
    width = max_width_list[len(problems)-1]+2
    arranged_problems+=f'{operand1_list[len(problems)-1]:>{width}}\n'
    
    # Generation of operand2 format string 
    for index in range(0,len(problems)-1):
        width = max_width_list[index]+1
        arranged_problems+=f'{operator_list[index]}{operand2_list[index]:>{width}}    '
    width = max_width_list[len(problems)-1]+1
    arranged_problems+=f'{operator_list[len(problems)-1]}{operand2_list[len(problems)-1]:>{width}}\n'
    
    # Generation of dashed line string
    for index in range(0,len(problems)-1):
        width = max_width_list[index]+2
        arranged_problems+=f'{"-"*width}    '
    width = max_width_list[len(problems)-1]+2
    
    # Generation of result format string only if optional boolean parameter True is passed 
    if len(args) == 1:
        arranged_problems+=f'{"-"*width}\n'
        for index in range(0,len(problems)-1):
            width = max_width_list[index]+2
            arranged_problems+=f'{result_list[index]:>{width}}    '
        width = max_width_list[len(problems)-1]+2
        arranged_problems+=f'{result_list[len(problems)-1]:>{width}}'
    else:
        arranged_problems+=f'{"-"*width}' 
    
    return arranged_problems
        
def get_width(num):
    count = 0
    while num != 0:
            num //= 10
            count = count + 1
    return count