def arithmetic_arranger(problems,*args):
    if len(problems) > 5:
      return 'Error: Too many problems.'
    operand1_list = list()
    operator_list = list()
    operand2_list = list()
    for problem in problems:
      problem_list = problem.split();
      operator = problem_list[1]
      if operator not in ['+','-']:
        return "Error: Operator must be '+' or '-'."
      try:
        operand1 = int(problem_list[0])
        operand2 = int(problem_list[2])
      except:
        return "Error: Numbers must only contain digits."
      if operand1 > 9999 or operand2 > 9999:
        return 'Error: Numbers cannot be more than four digits.'  
      operand1_list.append(operand1)
      operator_list.append(operator)
      operand2_list.append(operand2)
    