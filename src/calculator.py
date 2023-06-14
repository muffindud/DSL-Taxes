def throw_error(msg, env='cli'):
    if env == 'cli':
        print(msg)
        exit()
    elif env == 'gui':
        return msg


def main(brackets, targets, env='cli'):
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
                throw_error('Error: [' + key + '] does not have a bracket assigned.', env)
            elif targets[key]['bracket'] not in brackets.keys():
                throw_error('Error: Tax bracket [' + targets[key]['bracket'] + '] does not exist.', env)

    if env == 'cli':
        for key in targets.keys():
            print(key + ': ' '%.2f' % targets[key]['tax'])
    elif env == 'gui':
        return targets
