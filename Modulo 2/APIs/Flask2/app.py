from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['login']
        senha = request.form['senha']

        if nome == "admin" and senha == "123":
            return render_template('logado.html')
        else:
            return render_template('login.html', erro="Usuário ou senha inválidos")

    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)