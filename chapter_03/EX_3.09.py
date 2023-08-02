"""
*3.9 (Financial application: payroll) Write a program that reads the following information and prints a payroll statement:
Employee’s name (e.g., Smith)
Number of hours worked in a week (e.g., 10)
Hourly pay rate (e.g., 9.75)
Federal tax withholding rate (e.g., 20%)
State tax withholding rate (e.g., 9%)
"""

# Enter employee's name
employee_name = input("Enter employee's name: ")

# Enter number of hours worked in a week
number_of_hours = int(input('Enter number of hours worked in a week: ').strip())

# Enter hourly pay rate
hourly_pay_rate = eval(input('Enter hourly pay rate: ').strip())

# compute Gross Pay in one week
gross_pay = number_of_hours * hourly_pay_rate

# Enter federal tax withholding rate
federal_tax_withholding_rate = eval(input('Enter federal tax withholding rate: ').strip())

# compute federal withholding
federal_withholding = gross_pay * federal_tax_withholding_rate

# Enter state tax withholding rate
state_tax_withholding = eval(input('Enter state tax withholding rate: ').strip())

# compute state tax
state_tax = state_tax_withholding * gross_pay

# compute total deduction
total_deduction = state_tax + federal_withholding

# compute net pay
net_pay = gross_pay - total_deduction

# display the results
print(f'''
Employee Name: {employee_name}
Hours Worked: {number_of_hours}
Pay Rate: ${hourly_pay_rate:.2f}
Gross Pay: ${gross_pay:.2f}
Deductions: 
\tFederal Withholding ({federal_tax_withholding_rate * 100}%): ${federal_withholding:.2f}
\tState Withholding ({state_tax_withholding * 100}%): ${state_tax:.2f}
\tTotal Deduction: ${total_deduction:.2f}
Net Pay: ${net_pay:.2f}
''')
