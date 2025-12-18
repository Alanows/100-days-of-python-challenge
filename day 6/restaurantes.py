class Restaurant():
    
    def __init__(self,nombre_restaurante,tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0
        
    def describir_restaurante(self):
        print(f"el restaurante se llama {self.nombre_restaurante} y su tipo de cocina es {self.tipo_cocina}")
        
    
    def abrir_restaurante(self):
        print("el restaurante esta abierto")
        
    def establece_el_numero_servido(self,servidos):
        self.numero_servido = servidos
         
    def incrementar_numero_servido(self,increase):
        self.numero_servido += increase
    
    def resume_of_the_day(self):
        print(f" you served a total of {self.numero_servido} costumers")
        
class IceCreamTruck(Restaurant):
    def __init__(self,nombre_restaurante,tipo_cocina):
        super().__init__(nombre_restaurante,tipo_cocina)
        self.flavors = ['chocolate','vanilla','menta']
    
    def show_the_flavors(self):
        for i in self.flavors:
            print(f"we have {i} ice cream")

        
    


restaurant = Restaurant("luigi pizzaeria","cocina italinaa")
icecreamtruck = IceCreamTruck("ice helado",'heladeria')

icecreamtruck.show_the_flavors()

