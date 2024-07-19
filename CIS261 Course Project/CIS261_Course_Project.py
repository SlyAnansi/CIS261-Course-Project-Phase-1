#Ikere LeCompte, CIS261, Course Project Phase 1#
def get_employee_name():
    return input("Enter employee's name: ")

def get_total_hours():
    return float(input("Enter total hours worked: "))

def get_hourly_rate():
    return float(input("Enter hourly rate: "))

def get_tax_rate():
    return float(input("Enter income tax rate (in %): ")) / 100

def calculate_pay(total_hours, hourly_rate, tax_rate):
    gross_pay = total_hours * hourly_rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee_data(employee_data):
    print(f"\nEmployee Name: {employee_data['name']}")
    print(f"Total Hours: {employee_data['total_hours']}")
    print(f"Hourly Rate: {employee_data['hourly_rate']}")
    print(f"Gross Pay: {employee_data['gross_pay']}")
    print(f"Income Tax Rate: {employee_data['tax_rate'] * 100}%")
    print(f"Income Tax: {employee_data['income_tax']}")
    print(f"Net Pay: {employee_data['net_pay']}\n")
    
def display_totals(employees):
    total_employees = len(employees)
    total_hours = sum(e['total_hours'] for e in employees)
    total_gross_pay = sum(e['gross_pay'] for e in employees)
    total_income_tax = sum(e['income_tax'] for e in employees)
    total_net_pay = sum(e['net_pay'] for e in employees)
    
    print("\nSummary Totals:")
    print(f"Total Employees: {total_employees}")
    print(f"Total Hours: {total_hours}")
    print(f"Total Gross Pay: {total_gross_pay}")
    print(f"Total Income Tax: {total_income_tax}")
    print(f"Total Net Pay: {total_net_pay}")
employees = []

while True:
    user_input = input("Enter 'End' to stop or press Enter to continue:  ")
    if user_input.lower() == 'end':
        break
    
    name = get_employee_name()
    total_hours = get_total_hours()
    hourly_rate = get_hourly_rate()
    tax_rate = get_tax_rate()
    
    gross_pay, income_tax, net_pay = calculate_pay(total_hours, hourly_rate, tax_rate)
    employee_data = {
        'name': name,
        'total_hours': total_hours,
        'hourly_rate': hourly_rate,
        'tax_rate': tax_rate,
        'gross_pay': gross_pay,
        'income_tax': income_tax,
        'net_pay': net_pay
    }
    employees.append(employee_data)
    
    display_employee_data(employee_data)
    
display_totals(employees)