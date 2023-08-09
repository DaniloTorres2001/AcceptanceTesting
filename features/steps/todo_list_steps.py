# imports
import pytest

from behave import given,when,then
from todo_list import tasks, add_task, list_tasks, mark_complete, clear_tasks, edit_task

# Steps para "Agregar tarea"
tasks = [{'name': 'Tarea 1', 'completed': False}]

@given('que el usuario inicia la aplicación')
def step_impl(context):
  print('Iniciando aplicación')

@when('ingresa los detalles de la tarea')
def step_impl(context, nombre, prioridad, categoria, fecha):
  add_task(nombre, prioridad, categoria, fecha)

@then('la tarea debe ser agregada a la lista')
def step_impl(context):
  assert context.nombre in tasks, f"La tarea {context.nombre} no fue agregada"

# Steps para "Listar tareas"

@given('que existen tareas en la lista')
def step_impl(context):
  assert tasks, "No hay tareas para listar"

@when('el usuario selecciona listar tareas')
def step_impl(context):
  print('Listando tareas...')
  list_tasks()

@then('se deben mostrar todas las tareas con sus detalles')
def step_impl(context):
  print('Validando detalles...')
  # Código para validar detalles

# Steps para "Marcar tarea como completa"

@given('que existen tareas en la lista')
def step_impl(context):
  assert tasks, "No hay tareas para marcar"

@when('el usuario selecciona una tarea')
def step_impl(context):
  print('Seleccionando tarea...')

@when('la marca como completada')
def step_impl(context):
  tasks[0]['completed'] = True

@then('el estado de la tarea se actualiza a completada')
def step_impl(context):
  assert tasks[0]['completed'] == True

@given('que existen tareas en la lista')
def step_impl(context):
  # Crear tareas de prueba
  global tasks
  tasks = ['Tarea 1', 'Tarea 2']

@when('el usuario selecciona eliminar tareas')
def step_impl(context):
  print('Eliminando tareas...')

@when('confirma que desea eliminar')
def step_impl(context):
  print('Confirmado')

@then('la lista de tareas se vacía')
def step_impl(context):
  assert len(tasks) == 0, "La lista de tareas no está vacía"

@given('que existen tareas en la lista')
def step_impl(context):
  # Crear tareas de prueba
  global tasks
  tasks = [{'nombre': 'Tarea 1'}]

@when('el usuario selecciona editar una tarea')
def step_impl(context):
  print('Editando tarea...')

@when('modifica los detalles')
def step_impl(context, nombre):
  edit_task(0, nombre=nombre)

@then('la tarea se actualiza con los nuevos datos')
def step_impl(context):
  assert tasks[0]['nombre'] == context.nombre, "El nombre no se actualizó"