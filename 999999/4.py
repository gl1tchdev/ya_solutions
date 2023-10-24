class Employee:
    ind: int
    lang: str

    def __init__(self, index: int, lang: str):
        self.ind = index
        self.lang = lang


class Node(Employee):
    boss: Employee
    subs: list[Employee]

    def add_sub(self, employee: Employee):
        self.subs.append(employee)

    def set_boss(self, employee: Employee):
        self.boss = employee


def create_hierarchy(current_ind: int, current_em: Employee, langs, employees_data: list[int]):
    if employees_data[current_ind] == 0 or current_em.ind == employees_data[current_ind]:
        return
    employee = Node(employees_data[current_ind], langs[current_ind])
    create_hierarchy(current_ind+1, employee, langs, employees_data)
    # ...

created = []
with open('input.txt', 'r') as r, open('output.txt', 'w') as w:
    count_of_employees = int(r.readline().replace('\n', ' '))
    langs = r.readline().split(' ')
    employees_data = [int(s) for s in r.readline().split()]
    director = Node(employees_data[0], langs[0])
    create_hierarchy(1, director, langs, employees_data)
    # ...