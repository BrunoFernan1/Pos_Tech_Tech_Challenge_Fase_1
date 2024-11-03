from flask import Flask
from flask_caching import Cache
from flasgger import Swagger
from bs4 import BeautifulSoup
import requests
import pandas as pd


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
Swagger(app)


@app.route('/')
def home():
    return "Pos Tech - Tech Challenger: Fase 1"


@app.route('/producao/<int:ano>', methods=['GET'])
@cache.cached(timeout=60)
def producao(ano):
    """Produção de vinhos, sucos e derivados do Rio Grande do Sul
    ---
    parameters:
        - in: formData
          name: ano
          type: string
          required: true
          description: "ano de produção"

    responses:
        200:
            description: Success
            schema:
                type: object
                properties:
                    Produto:
                        type: string
                        description: Tipo de produto
                    Quantidade (L.):
                        type: string
                        description: Quantidade em litros

    """

    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02'

    status = True
    while status:
        try:
            response = requests.get(url)
            break

        except:
            status = True

    soup = BeautifulSoup(response.text, 'html.parser')

    tabela = soup.find('table', class_='tb_dados')

    tabela_str = str(tabela)

    df = pd.read_html(tabela_str)[0]

    df_json = df.to_json(orient='records')

    return df_json


@app.route('/processamento/<int:ano>/<int:tipo_uva>', methods=['GET'])
@cache.cached(timeout=60)
def processamento(ano, tipo_uva):
    """Quantidade de uvas processadas no Rio Grande do Sul
    ---
    parameters:
        - in: formData
          name: ano
          type: string
          required: true
          description: "ano de processamento"
        - in: formData
          name: tipo_uva
          type: string
          required: true
          description: "1 = Viníferas | 2 = Americanas e híbridas | 3 = Uvas de mesa | 4 = Sem classificação"

    responses:
        200:
            description: Success
            schema:
                type: object
                properties:
                    Cultivar:
                        type: string
                        description: Tipo de cultivo
                    Quantidade (Kg):
                        type: string
                        description: Quantidade em kilogramas

    """

    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_03&subopcao=subopt_0{tipo_uva}'

    status = True
    while status:
        try:
            response = requests.get(url)
            break

        except:
            status = True

    soup = BeautifulSoup(response.text, 'html.parser')

    tabela = soup.find('table', class_='tb_dados')

    tabela_str = str(tabela)

    df = pd.read_html(tabela_str)[0]

    df_json = df.to_json(orient='records')

    return df_json


@app.route('/comercializacao/<int:ano>', methods=['GET'])
@cache.cached(timeout=60)
def comercializacao(ano):
    """Comercialização de vinhos e derivados no Rio Grande do Sul
    ---
    parameters:
        - in: formData
          name: ano
          type: string
          required: true
          description: "ano de comercialização"

    responses:
        200:
            description: Success
            schema:
                type: object
                properties:
                    Produto:
                        type: string
                        description: Tipo de produto
                    Quantidade (L.):
                        type: string
                        description: Quantidade em litros

    """

    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_04'

    status = True
    while status:
        try:
            response = requests.get(url)
            break

        except:
            status = True

    soup = BeautifulSoup(response.text, 'html.parser')

    tabela = soup.find('table', class_='tb_dados')

    tabela_str = str(tabela)

    df = pd.read_html(tabela_str)[0]

    df_json = df.to_json(orient='records')

    return df_json


@app.route('/importacao/<int:ano>/<int:tipo_derivado>', methods=['GET'])
@cache.cached(timeout=60)
def importacao(ano, tipo_derivado):
    """Importação de derivados de uva
    ---
    parameters:
        - in: formData
          name: ano
          type: string
          required: true
          description: "ano de importação"
        - in: formData
          name: tipo_derivado
          type: string
          required: true
          description: "1 = Vinhos de Mesa | 2 = Espumantes | 3 = Uvas frescas | 4 = Uvas passas | 5 = Suco de uva"

    responses:
        200:
            description: Success
            schema:
                type: object
                properties:
                    Países:
                        type: string
                        description: País
                    Quantidade (Kg):
                        type: string
                        description: Quantidade em kilogramas
                    Valor (US$):
                        type: string
                        description: Valores em dólares americanos

    """

    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao=subopt_0{tipo_derivado}'

    status = True
    while status:
        try:
            response = requests.get(url)
            break

        except:
            status = True

    soup = BeautifulSoup(response.text, 'html.parser')

    tabela = soup.find('table', class_='tb_dados')

    tabela_str = str(tabela)

    df = pd.read_html(tabela_str)[0]

    df_json = df.to_json(orient='records')

    return df_json


@app.route('/exportacao/<int:ano>/<int:tipo_derivado>', methods=['GET'])
@cache.cached(timeout=60)
def exportacao(ano, tipo_derivado):
    """Exportação de derivados de uva
    ---
    parameters:
        - in: formData
          name: ano
          type: string
          required: true
          description: "ano de exportação"
        - in: formData
          name: tipo_derivado
          type: string
          required: true
          description: "1 = Vinhos de Mesa | 2 = Espumantes | 3 = Uvas frescas | 4 = Suco de uva"

    responses:
        200:
            description: Success
            schema:
                type: object
                properties:
                    Países:
                        type: string
                        description: País
                    Quantidade (Kg):
                        type: string
                        description: Quantidade em kilogramas
                    Valor (US$):
                        type: string
                        description: Valores em dólares americanos

    """

    url = f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao=subopt_0{tipo_derivado}'

    status = True
    while status:
        try:
            response = requests.get(url)
            break

        except:
            status = True

    soup = BeautifulSoup(response.text, 'html.parser')

    tabela = soup.find('table', class_='tb_dados')

    tabela_str = str(tabela)

    df = pd.read_html(tabela_str)[0]

    df_json = df.to_json(orient='records')

    return df_json


if __name__ == '__main__':
    app.run(debug=True)
