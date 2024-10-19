salary = float(input())

percent = 0
newSalary = 0

if salary >= 0 and salary <= 400.00:
    newSalary = salary+(salary*0.15)
    percent = 15
    
elif salary >= 400.01 and salary <= 800.00:
    newSalary = salary+(salary*0.12)
    percent = 12
    
elif salary >= 800.01 and salary <= 1200.00:
    newSalary = salary+(salary*0.10)
    percent = 10
    
elif salary >= 1200.01 and salary <= 2000.00:
    newSalary = salary+(salary*0.07)
    percent = 7
    
else:
    newSalary = salary+(salary*0.04)
    percent = 4


print(f'Novo salario: {newSalary:.2f}')
print(f'Reajuste ganho: {newSalary-salary:.2f}')
print(f'Em percentual: {percent} %')
