from pizza import Pizza
from ingredientes import Ingredientes as ing


print("Valores de los atributos de clase:")
print("Ingredientes proteicos:", ing.ing_proteicos)
print("Ingredientes vegetales:", ing.ing_vegetales)
print("Tipos de masa:", ing.tipo_masa)

salsa_verificar = "salsa de tomate"
print(f"¿'{salsa_verificar}' está en las salsas disponibles?:", Pizza.validar_elemento(["salsa de tomate", "salsa bbq"], salsa_verificar))

pizza = Pizza()
pizza.generar_orden()


print(
    f'''
    "Ingredientes vegetales" = {pizza.ing_vegetal_pizza1} , {pizza.ing_vegetal_pizza2}
    "Ingrediente proteico" = {pizza.ing_proteico_pizza}
    "Tipo de masa" = {pizza.tipo_masa_pizza}
    "Tipo de salsa" = {salsa_verificar}
    
    "Es valida la pizza? = {pizza.es_valida}
    
    Pizza familiar 3 ingredientes: $10.000.- CLP

    ''' if pizza.es_valida == True else "Hubo un error durante la generacion de la orden"
)