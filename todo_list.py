import sys

tasks = [
  {
    'name': 'Comprar víveres',
    'priority': 'Alta',
    'category': 'Personal',
    'due_date': '2023-08-10'
  },
  {
    'name': 'Llamar al mecánico',
    'priority': 'Media',
    'category': 'Automóvil',
    'due_date': '2023-08-12'
  },
  {
    'name': 'Entregar informe de proyecto',
    'priority': 'Alta',
    'category': 'Trabajo',
    'due_date': '2023-08-11'
  },
  {
    'name': 'Sacar a pasear al perro',
    'priority': 'Baja',
    'category': 'Mascotas',
    'due_date': '2023-08-09'
  }
]


def add_task():
    task = {}

    print('Agregar Nueva Tarea')

    task['name'] = input('Nombre: ')

    task['priority'] = input('Prioridad (Alta/Media/Baja): ')

    task['category'] = input('Categoría: ')

    task['due_date'] = input('Fecha de Vencimiento: ')

    tasks.append(task)

    print('Tarea agregada!\n')


def list_tasks():
    print('Lista de Tareas')

    if len(tasks) == 0:
        print('No hay tareas pendientes')
        return

    for i, task in enumerate(tasks):
        number = i + 1
        marker = '✔' if task.get('complete') else '❌'

        print(
            f"{number}. [{marker}] {task['name']} ({task['priority']}) - Categoría: {task['category']} - Fecha Vencimiento: {task['due_date']}")

    print()


def mark_complete():
    list_tasks()

    if len(tasks) == 0:
        return

    task_to_mark = int(input('Ingrese el número de tarea a marcar como completa: ')) - 1

    if task_to_mark >= 0 and task_to_mark < len(tasks):
        tasks[task_to_mark]['complete'] = True

    print('Tarea marcada como completa')


def clear_tasks():
    confirm = input('¿Está seguro que desea eliminar todas las tareas? (S/N)')

    if confirm.upper() == 'S':
        tasks.clear()
        print('Lista de tareas eliminada')
    else:
        print('Cancelando eliminación')


def edit_task():
    list_tasks()

    if len(tasks) == 0:
        return

    task_to_edit = int(input('Ingrese el número de tarea a editar: ')) - 1

    if task_to_edit >= 0 and task_to_edit < len(tasks):

        task = tasks[task_to_edit]

        print('Editando tarea: ', task['name'])
        print('1. Nombre')
        print('2. Prioridad')
        print('3. Categoría')
        print('4. Fecha Vencimiento')
        print('5. Cancelar')

        option = input('Selecciona el campo a editar: ')

        if option == '1':
            task['name'] = input('Nombre nuevo: ')
        elif option == '2':
            task['priority'] = input('Nueva prioridad: ')
        elif option == '3':
            task['category'] = input('Nueva categoría: ')
        elif option == '4':
            task['due_date'] = input('Nueva fecha vencimiento: ')

    print('Tarea actualizada!')


def show_menu():
    print()
    print('Menú')
    print('1. Agregar Tarea')
    print('2. Listar Tareas')
    print('3. Marcar Tarea Completa')
    print('4. Eliminar Tareas')
    print('5. Editar Tarea')
    print('6. Salir')

    option = input('Selecciona una opción: ')

    if option == '1':
        add_task()
    elif option == '2':
        list_tasks()
    elif option == '3':
        mark_complete()
    elif option == '4':
        clear_tasks()
    elif option == '5':
        edit_task()
    elif option == '6':
        print('Saliendo...')
        sys.exit()
    else:
        print('Opción inválida')


# Loop principal

print('Bienvenido a la Lista de Tareas')
while True:
    show_menu()