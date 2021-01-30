company_users = {}
while True:
    data = input()
    if data == "End":
        break
    company, employee_id = data.split(" -> ")
    if company not in company_users:
        company_users[company] = []
    if employee_id not in company_users[company]:
        company_users[company].append(employee_id)

for company, employee_id in sorted(company_users.items(), key=lambda x: x[0]):
    print(company)
    for e_id in employee_id:
        print(f"-- {e_id}")
