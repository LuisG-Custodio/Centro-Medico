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
    flash('Los datos fueron agregados correctamente')
    return redirect(url_for('index'))

@app.route('/paciente')
def paciente():
    return render_template('AltaPacientes.html')

@app.route('/guardarPaciente', methods=['POST'])
def guardarPaciente():
    if request.method == 'POST':
        #pasamos a variables el contendio de los input
        Vnombre=request.form['txtnombre']
        Vexpediente=request.form['txtexpediente']
        VnombreDoc=request.form['txtnombreDoc']
        VefechaNac=request.form['txtFechaNac']
        Valergias=request.form['txtalergias']
        Venfermedades=request.form['txtenfermedades']
        Vantecedentes=request.form['txtantecedentes']
        
        #Conectar y ejecutar el insert
        CS= mysql.connection.cursor()
        CS.execute('insert into tb_pacientes(Nombre,Expediente,Nombre_Doctor,Fecha_Nacimiento,Alergias,Enfermedades,Antecedentes) values(%s,%s,%s,%s,%s,%s,%s)',(Vnombre,Vexpediente,VnombreDoc,VefechaNac,Valergias,Venfermedades,Vantecedentes))
        mysql.connection.commit()           
    flash('Los datos fueron agregados correctamente')
    return redirect(url_for('paciente'))

#ejecución del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)