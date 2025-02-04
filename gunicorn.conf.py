import multiprocessing

# Define o número de workers (processos que lidam com requisições)
workers = multiprocessing.cpu_count() * 2 + 1  # Regra comum: 2 * núcleos + 1

# Define a aplicação Flask que será executada
wsgi_app = "main:app"  # Arquivo 'main.py' e a variável Flask chamada 'app'

# Define o diretório de trabalho do projeto
chdir = "/home/ubuntu/flask-app/my_flask_app/app"

# Define o endereço e porta onde a aplicação será servida
bind = "0.0.0.0:5000"

# Define se o processo rodará em segundo plano (modo daemon)
daemon = True  # True = roda em background, False = roda no terminal

# Arquivos de log
accesslog = "logs/access.log"  # Log de acessos
errorlog = "logs/error.log"    # Log de erros
loglevel = "info"              # Nível de log (debug, info, warning, error, critical)

# Tempo máximo de espera para uma requisição (evita processos travados)
timeout = 30

# Número de threads por worker (se usar `gthread` como worker class)
threads = 3
