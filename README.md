## Instalação do ambiente:

**Download do sistema e criação do ambiente virtual:**

```
git clone https://github.com/jonathanscheibel/notificacao.git && cd notificacao
virtualenv -p python3 .venv
source .venv/bin/activate 
pip install --upgrade pip
pip install -r requirements.txt
```

**Inicialização do sistema:**
> sh wsgi.sh
