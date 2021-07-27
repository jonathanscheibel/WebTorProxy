## Instalação do ambiente:

**Download do sistema e criação do ambiente virtual:**

```
git clone https://github.com/jonathanscheibel/webtorproxy.git && cd webtorproxy
virtualenv -p python3 .venv
source .venv/bin/activate 
pip install --upgrade pip
pip install -r requirements.txt
```

**Inicialização do sistema [DESENVOLVIMENTO]:**
```
python wsgi
```

**Inicialização do sistema [TESTES]:**
```
XXXXXX
```

**Inicialização do sistema [PRODUCAO]:**
```
sh wsgi.sh
```
