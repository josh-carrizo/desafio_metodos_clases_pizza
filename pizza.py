from ingredientes import Ingredientes as ing

class Pizza:
    
    def __init__(self):
        self.ing_proteico_pizza = ""
        self.ing_vegetal_pizza1 = ""
        self.ing_vegetal_pizza2 = ""
        self.tipo_masa_pizza = ""
        self.es_valida = False
                
    
    @staticmethod    
    def validar_elemento(lista,elemento):
        if elemento in lista:
            print(f"{elemento} ha sido ingresado con éxito")
            return True
        elif elemento is not lista:
            print(f"{elemento} no se ha podido ingresar, por favor considere que puede escoger entre {lista}")
            return False
        else:
            print("No hemos podido procesar su orden, por favor intente nuevamente") 
            
    def generar_orden(self):
        print(f"""
              Bienvenid@!
              Vamos a personalizar una pizza según tus gustos!
              Recuerda:
                - Debes escoger un ingrediente proteico entre {ing.ing_proteicos}
                - Debes escoger 2 ingredientes vegetales entre {ing.ing_vegetales}
                - Puedes escoger entre Masa delgada o tradicional
                - El tamaño de la pizza será Familiar
                - El valor de la pizza es de $10.000.-CLP
              """)
            
        
        self.ing_proteico_pizza = (input("Ingrese el ingrediente proteico que desea agregar:\n")).lower()
        if not self.validar_elemento(ing.ing_proteicos, self.ing_proteico_pizza):
            return self.ing_proteico_pizza
        
        self.ing_vegetal_pizza1 = (input("Ingrese el primer ingrediente vegetal que desea agregar:\n")).lower()
        if not self.validar_elemento(ing.ing_vegetales, self.ing_vegetal_pizza1):
            return self.ing_vegetal_pizza1
        
        self.ing_vegetal_pizza2 = (input("Ingrese el segundo ingrediente vegetal que desea agregar:\n")).lower()
        if not self.validar_elemento(ing.ing_vegetales, self.ing_vegetal_pizza2):
            return self.ing_vegetal_pizza2
        
        self.tipo_masa_pizza = (input("Ingrese el tipo de masa que desea para su pizza:\n")).lower()
        if not self.validar_elemento(ing.tipo_masa, self.tipo_masa_pizza):
            return self.tipo_masa_pizza
                
        self.es_valida = True
        print("Tu pizza ha sido creada con éxito!")
        print(f'''
                {self.ing_proteico_pizza}
                {self.ing_vegetal_pizza1}
                {self.ing_vegetal_pizza2}
                {self.tipo_masa_pizza}
                {self.es_valida}
              
              ''')
# if __name__ == "__main__":
#     pizza = Pizza()
#     pizza.generar_orden()