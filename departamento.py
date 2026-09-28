class Departamento:

    def __init__(self, id_departamento :str, nombre:str, piso:int):
        self.id_departamento=id_departamento
        self.nombre=nombre 
        self.piso=piso 

    @property
    def id_departamento(self)->str:
        return self._id_departamento

    @id_departamento.setter 
    def id_departamento(self,id_departamento:str)-> None:
        self._id_departamento=id_departamento

    @property
    def nombre(self)->str:
        return self.nombre 

    @nombre.setter 
    def nombre(self,nombre:str)->None:
        self._nombre=nombre 

    @property
    def piso(self)->int:
        return self._piso 

    @piso.setter 
    def piso (self,piso:int)->None:
        self._piso=piso

    def __str__(self)->str:
        return f"Informacion del departmaneto:\nid_departamento: {self.id_departamento}\nNombre: {self.nombre}\nEdad: {self.piso}\npiso: "

    def __repr__(self)->str:
        return f"id_departamento(id_departamento='{self.id_departamento}', nombre='{self.nombre}', piso={self.piso}' "
            