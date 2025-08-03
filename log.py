import os 

def log(mensagem):
    print(f'Mostrando variável de ambiente: {os.getenv('MINHA_VAR')}')
    print('Adicionando log via função', mensagem)
