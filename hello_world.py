from flask import Flask

# Cria uma instância do Flask
app = Flask(__name__)

# Define a rota padrão para o caminho '/'
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Executa o aplicativo se este arquivo for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)
