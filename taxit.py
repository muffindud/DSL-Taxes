import sys
import re


def throw_error(error):
    print(error)
    exit()


def main(file):
    with open(file, 'r') as f:
        content = f.readlines()

    # Remove all newlines from each element of content
    content = [x.strip() for x in content]
    # Remove all empty elements from content
    content = list(filter(None, content))

    brackets = {}
    targets = {}

    bracket = ''
    target = ''
    line = 0
    in_bracket = False
    in_compute = False
    while line < len(content):
        # Capture the tax_bracket name
        if content[line][0:11] == 'tax_bracket':
            in_bracket = True
            in_compute = False
            target = ''
            # Append to brackets the words between the "" in the line
            try:
                bracket = re.findall(r'"([^"]*)"', content[line])[0]
            except:
                throw_error('Error: Invalid syntax: [' + content[line] + '].')
            brackets[bracket] = []

        # Capture the range of the tax_bracket only if a bracket is examined
        elif content[line][0:5] == 'range' and in_bracket:
            # Save the string between range and - in the line
            try:
                bracket_range = re.findall(r'range ([^ ]*) -', content[line])[0]
            except:
                throw_error('Error: Invalid syntax: [' + content[line] + '].')

            # Replace the amount to float
            if bracket_range == 'max':
                bracket_range = float('inf')
            else:
                bracket_range = float(bracket_range)

            # Capture the tax rate of the tax_bracket
            if content[line][-1] == '%':
                # Identify the rates that are in percentage
                # Save the string between the > and % in the line and remove spaces
                try:
                    bracket_rate = float(re.findall(r'> ([^%]*)', content[line])[0].replace(' ', '')) / 100
                except:
                    throw_error('Error: Invalid syntax: [' + content[line] + '].')
            else:
                # Identify the rates that are in decimal
                # Save the string after the > in the line and remove spaces
                try:
                    bracket_rate = float(re.findall(r'> ([^ ]*)', content[line])[0].replace(' ', ''))
                except:
                    throw_error('Error: Invalid syntax: [' + content[line] + '].')

            # Fix floating point error
            bracket_rate = round(bracket_rate, 16)

            # Append to brackets the bracket_range and bracket_rate
            brackets[bracket].append((bracket_range, bracket_rate))

        # Capture the target
        elif content[line][0:11] == 'tax_compute':
            in_bracket = False
            in_compute = True
            bracket = ''
            # Save the string between the "" in the line
            try:
                target = re.findall(r'"([^"]*)"', content[line])[0]
            except:
                throw_error('Error: Invalid syntax: [' + content[line] + '].')
            targets[target] = {'bracket': '', 'income': 0.0, 'standard_deduction': 0.0, 'donation_deduction': 0.0, 'tax': 0.0}

        # Capture the bracket of the target only if a target is examined
        elif content[line][0:7] == 'bracket' and in_compute:
            # Save the string between the "" in the line
            try:
                target_bracket = re.findall(r'"([^"]*)"', content[line])[0]
            except:
                throw_error('Error: Invalid syntax: [' + content[line] + '].')
            targets[target]['bracket'] = target_bracket

        # Capture the income of the target only if a target is examined
        elif content[line][0:6] == 'income' and in_compute:
            # Save the string after the = in the line and remove spaces
            try:
                target_income = float(re.findall(r'= ([^ ]*)', content[line])[0].replace(' ', ''))
            except:
                throw_error('Error: Invalid syntax: [' + content[line] + '].')
            target_income = float(target_income)
            targets[target]['income'] = target_income

        # Capture the standard deduction of the target only if a target is examined
        elif content[line][0:18] == 'standard_deduction' and in_compute:
            # Save the string after the = in the line and remove spaces
            try:
                target_standard_deduction = float(re.findall(r'= ([^ ]*)', content[line])[0].replace(' ', ''))
            except:
                throw_error('Error: Invalid syntax: [' + content[line] + '].')
            targets[target]['standard_deduction'] = target_standard_deduction

        # Capture the donation of the target only if a target is examined
        elif content[line][0:18] == 'donation_deduction' and in_compute:
            # Save the string after the = in the line and remove spaces
            try:
                target_donation = float(re.findall(r'= ([^ ]*)', content[line])[0].replace(' ', ''))
            except:
                throw_error('Error: Invalid syntax: [' + content[line] + '].')
            targets[target]['donation_deduction'] = target_donation

        elif content[line][0:5] == 'range' and not in_bracket:
            throw_error('Error: Cannot have a range outside of a tax_bracket.')

        elif content[line][0:7] == 'bracket' and not in_compute:
            throw_error('Error: Cannot assign a bracket outside of a tax_compute.')

        elif content[line][0:6] == 'income' and not in_compute:
            throw_error('Error: Cannot assign an income outside of a tax_compute.')

        elif content[line][0:18] == 'standard_deduction' and not in_compute:
            throw_error('Error: Cannot assign a standard_deduction outside of a tax_compute.')

        elif content[line][0:18] == 'donation_deduction' and not in_compute:
            throw_error('Error: Cannot assign a donation_deduction outside of a tax_compute.')

        elif content[line][0:10] != 'deductions':
            throw_error('Error: Invalid syntax: [' + content[line] + '].')

        line += 1

    # Sort the brackets by range
    for key in brackets.keys():
        brackets[key].sort(key=lambda x: x[0])

    # TODO: Check if the formula is correct
    for key in targets.keys():
        if targets[key]['bracket'] in brackets.keys():
            taxable = targets[key]['income'] - targets[key]['standard_deduction'] - targets[key]['donation_deduction']
            taxable = round(taxable, 16)
            i = 0
            while brackets[targets[key]['bracket']][i][0] < taxable:
                i += 1
            tax = brackets[targets[key]['bracket']][i][1] * taxable

            # Fix floating point error
            tax = round(tax, 2)
            targets[key]['tax'] = tax
        else:
            if targets[key]['bracket'] == '':
                throw_error('Error: [' + key + '] does not have a bracket assigned.')
            elif targets[key]['bracket'] not in brackets.keys():
                throw_error('Error: Tax bracket [' + targets[key]['bracket'] + '] does not exist.')

    for key in targets.keys():
        print(key + ': ' '%.2f' % targets[key]['tax'])


if __name__ == '__main__':
    main(sys.argv[1])
