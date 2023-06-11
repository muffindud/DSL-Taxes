def main(brackets: dict, targets: dict):
    content = ""

    for bracket in brackets.keys():
        content += "tax_bracket = \"" + bracket + "\"\n"
        for bracket_range in brackets[bracket]:
            content += "    range " + str(bracket_range[0]) + " - > " + str(bracket_range[1]) + "\n"
        content += "\n"

    for target in targets.keys():
        content += "tax_compute \"" + target + "\"\n"
        content += "    bracket = \"" + targets[target]["bracket"] + "\"\n"
        content += "    income = " + str(targets[target]["income"]) + "\n"

        if targets[target]["standard_deduction"] != 0.0 and targets[target]["donation_deduction"] != 0.0:
            content += "\n    deductions\n"
            content += "        standard_deduction = " + str(targets[target]["standard_deduction"]) + "\n"
            content += "        donation_deduction = " + str(targets[target]["donation_deduction"]) + "\n"
        elif targets[target]["standard_deduction"] != 0.0 and targets[target]["donation_deduction"] == 0.0:
            content += "\n    deductions\n"
            content += "        standard_deduction = " + str(targets[target]["standard_deduction"]) + "\n"
        elif targets[target]["standard_deduction"] == 0.0 and targets[target]["donation_deduction"] != 0.0:
            content += "\n    deductions\n"
            content += "        donation_deduction = " + str(targets[target]["donation_deduction"]) + "\n"

        content += "\n"

    return content
