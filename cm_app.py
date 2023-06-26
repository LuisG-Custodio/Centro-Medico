#importación del framework
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#inicialización del APP
app= Flask(__name__)
#conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='centro_medico'
app.secret_key= 'mysecretkey'
mysql= MySQL(app)

#declaración de ruta / http://localhost:5000
@app.route('/')
def index():
    return render_template('AltaMedicos.html')

# ruta / http://localhost:5000/guardar | tipo POST para Insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        #pasamos a variables el contendio de los input
        Vnombre=request.form['txtnombre']
        Vcedula=request.form['txtcedula']
        Vcorreo=request.form['txtcorreo']
        Vespecialidad=request.form['txtespecialidad']
        
        #Conectar y ejecutar el insert
        CS= mysql.connection.cursor()
        CS.execute('insert into tb_medicos(Nombre,Cedula,Correo,Especialidad) values(%s,%s,%s,%s)',(Vnombre,Vcedula,Vcorreo,Vespecialidad))
        mysql.connection.commit()           
    flash('Los datos del album fueron agregados correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar():
    return "Se elimino en la BD"

#ejecución del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)