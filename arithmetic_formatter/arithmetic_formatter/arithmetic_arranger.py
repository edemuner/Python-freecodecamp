def arithmetic_arranger(operations, answer=False):
    if len(operations) > 5:
        return 'Error: Too many problems.'

    firsters = []
    seconders = []
    operators = []
    results = []

    # this block splits each of the operation strings and places the first and second numbers
    # of each operation in separate lists, as well as the operators signs and results
    # verificar a possibilidade de usar o split com espaços e dar o encaminhamento devido ao conjunto de caracteres, com o objetivo de economizar código, 
    # para que não seja preciso checar a existência dos operadores com repetidos ifs

    for operation in operations:
        pieces = operation.split()
        first = pieces[0].strip()
        operator = pieces[1].strip()
        second = pieces[2].strip()

        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not first.isnumeric() or not second.isnumeric():
            return 'Error: Numbers must only contain digits.'
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."
        firsters.append(first)
        seconders.append(second)
        operators.append(operator)
        if answer:
            if operator == "+":
                results.append(str(int(first) + (int(second))))
            elif operator == "-":
                results.append(str(int(first) - (int(second))))

    # this block takes the bigger (in digits) number in each operation and sets a variable
    # representing the length of this number + 2, in order to get the
    # necessary space for each operation's columnspan
    columnspan = []
    for i in range(len(firsters)):
        if len(firsters[i]) > len(seconders[i]):
            columnspan.append(len(firsters[i]) + 2)
        else:
            columnspan.append(len(seconders[i]) + 2)

    # this block concatenates the string to be returned, subtracting from the columnspan reserved for each operation
    # the number of digits necessary in order to get everything aligned
    final = str()
    for i in range(len(firsters)):
        if i != 0: final += "    "
        final += (columnspan[i] - len(firsters[i])) * " " + firsters[i]
    final += "\n"
    for i in range(len(seconders)):
        if i != 0: final += "    "
        final += operators[i] + (columnspan[i] - len(seconders[i]) - 1) * " " + seconders[i]
    final += "\n"
    for i in range(len(firsters)):
        if i != 0: final += "    "
        final += columnspan[i] * "-"
    if answer:
        final += "\n"
        for i in range(len(results)):
            if i != 0: final += "    "
            final += (columnspan[i] - len(results[i])) * " " + results[i]

    return final


# TESTES

operations = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
more_operations = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
first = arithmetic_arranger(operations)
print()
second = arithmetic_arranger(more_operations, True)

# actual = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
# expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"


print(second)
