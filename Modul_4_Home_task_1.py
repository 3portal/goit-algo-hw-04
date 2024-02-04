with open('path', 'w') as fh:
    fh.write("Alex Korp,3000,\nNikita Borisenko,2000,\nSitarama Raju,1000")

def total_salary(path):
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            lines = file.readlines()
            salaries = [int(line.strip().split(',')[1]) for line in lines]
            total = sum(salaries)
            average = total/ len(salaries)
            return(total,average)
    except Exception as e:
        print(f"Error:{e}")
    return "Error"
    
total, average = total_salary(r'path')
print(f'Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}')