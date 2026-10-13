from config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data.get('id')    
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('email')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email) VALUES(%(nombre)s, %(apellido)s, %(email)s);"
        return connectToMySQL('usuarios_crud').query_db(query, datos)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        usuarios_en_bd = connectToMySQL('usuarios_crud').query_db(query)
        usuarios = []
        for usuario in usuarios_en_bd:
            usuarios.append(cls(usuario))
        return usuarios

    @classmethod
    def get_one(cls,datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        usuario_en_db = connectToMySQL('usuarios_crud').query_db(query,datos)

        return cls(usuario_en_db[0])
    
    @classmethod
    def update(cls, datos):
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL('usuarios_crud').query_db(query, datos)
    
    @classmethod
    def delete(cls, datos):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('usuarios_crud').query_db(query, datos)

