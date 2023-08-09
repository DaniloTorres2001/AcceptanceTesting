Feature: Agregar tarea

  Scenario: Usuario agrega una nueva tarea
    Given que el usuario inicia la aplicación
    When ingresa los detalles de la tarea
      | nombre   | Comprar víveres |
      | prioridad | alta |
      | categoría | personal |
      | fecha     | 2023-03-01 |
    Then la tarea debe ser agregada a la lista

Feature: Listar tareas

  Scenario: Listar tareas existentes
    Given que existen tareas en la lista
    When el usuario selecciona listar tareas
    Then se deben mostrar todas las tareas con sus detalles

Feature: Marcar tarea como completa

  Scenario: Marcar una tarea como completada
    Given que existen tareas en la lista
    When el usuario selecciona una tarea
      And la marca como completada
    Then el estado de la tarea se actualiza a completada

Feature: Eliminar tareas

  Scenario: Usuario elimina todas las tareas
    Given que existen tareas en la lista
    When el usuario selecciona eliminar tareas
      And confirma que desea eliminar
    Then la lista de tareas se vacía

Feature: Editar tarea

  Scenario: Editar detalles de una tarea
    Given que existen tareas en la lista
    When el usuario selecciona editar una tarea
      And modifica los detalles
      | nombre   | Comprar víveres y artículos de limpieza |
    Then la tarea se actualiza con los nuevos datos