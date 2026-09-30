from flask import Flask,render_template,redirect,request

from controllers.usuario import Usuario

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/usuario/nuevo',methods=['POST'])
def crear():
    datos = {
        "nombre":request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email']
    }
    Usuario.save(datos)
    return redirect('/usuarios')

@app.route('/usuarios')
def usuarios():
    usuarios = Usuario.get_all()
    return render_template("resultados.html",todos_usuarios = usuarios)

@app.route('/usuarios/<int:usuario_id>')
def detalle(usuario_id):
    datos = {
        'id': usuario_id
    }
    usuario = Usuario.get_one(datos)
    return render_template("detalle.html",usuario = usuario)

@app.route('/usuarios/editar/<int:usuario_id>')
def editar(usuario_id):
    datos = {
        'id': usuario_id
    }
    usuario = Usuario.get_one(datos)
    return render_template("editar.html", usuario = usuario)

@app.route('/usuarios/actualizar/<int:usuario_id>', methods=['POST'])
def actualizar(usuario_id):
    datos = {
        'id': usuario_id,
        "nombre":request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email']
    }
    Usuario.update(datos)
    return redirect(f"/usuarios/{usuario_id}")

@app.route('/usuarios/borrar/<int:usuario_id>')
def borrar(usuario_id):
    datos = {
        'id': usuario_id,
    }
    Usuario.delete(datos)
    return redirect('/usuarios')

if __name__=="__main__":
    app.run(debug=True)