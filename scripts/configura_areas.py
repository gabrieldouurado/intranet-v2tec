import json
import logging
from pathlib import Path
from uuid import uuid4

import requests

# Define como faremos o log das ações
logging.basicConfig()
logger = logging.getLogger("v2tec.intranet.configura_area")
logger.setLevel(logging.INFO)

# Constantes utilizadas no script
PASTA_ATUAL = Path(__file__).parent.resolve()
PASTA_DADOS = PASTA_ATUAL / "dados"
PASTA_TEMPLATES = PASTA_ATUAL / "templates"
PORTAL_URL = "http://localhost:8080/Plone"
BASE_URL = f"{PORTAL_URL}/++api++"
USUARIO = "admin"
SENHA = "admin"

# Cria a pasta de dados caso ela não exista ainda
if not PASTA_DADOS.exists():
    PASTA_DADOS.mkdir(parents=True, exist_ok=True)
    logger.info(f"Criada a pasta {PASTA_DADOS}")

# Carrega os templates, na ordem em que serão utilizados
BLOCOS = ("titulo", "descricao", "listagem", "pesquisa")
TEMPLATES = []

for bloco in BLOCOS:
    arquivo_template = PASTA_TEMPLATES / f"area_bloco_{bloco}.json"
    # Carregamos como texto para depois substituir o placeholder ##UUID## pelo valor real
    TEMPLATES.append(arquivo_template.read_text())

# Cabeçalhos HTTP
headers = {"Accept": "application/json"}

session = requests.Session()
session.headers.update(headers)

# Autenticar o usuário admin utilizando um Token JWT
# Ref: https://6.docs.plone.org/plone.restapi/docs/source/usage/authentication.html
login_url = f"{BASE_URL}/@login"
response = session.post(login_url, json={"login": USUARIO, "password": SENHA})

## Checar se temos uma resposta válida
if not response.status_code == 200:
    raise ValueError("Usuário ou senha incorretos")
data = response.json()
token = data["token"]
session.headers.update({"Authorization": f"Bearer {token}"})

# Buscar todos os conteúdos do tipo "Area" no portal
## Ref: https://6.docs.plone.org/plone.restapi/docs/source/endpoints/searching.html#search
search_url = f"{BASE_URL}/@search?portal_type=Area&sort_on=path&fullobjects=1"
response = session.get(search_url)
data = response.json()
total_areas = data["items_total"]
logger.info(f"O portal conta com {total_areas} áreas")

# Salvar os dados recebidos do portal em um arquivo json
arquivo_dados = PASTA_DADOS / "areas.json"
with open(arquivo_dados, "w") as fh:
    json.dump(data, fh, indent=2)
    logger.info(f"Dados da listagem salvos em {arquivo_dados}")

ALTERACOES = {}

for item in data["items"]:
    uuid = item["UID"]
    relative_path = item["@id"].replace(PORTAL_URL, "")
    path = f"{BASE_URL}{relative_path}"
    logger.info(f"Processando {path}")
    blocks = {}
    blocks_layout: dict[str, list[str]] = {"items": []}

    for template in TEMPLATES:
        # Substituir o placeholder ##UUID## pelo valor real
        template_json = template.replace("##UUID##", uuid)
        bloco = json.loads(template_json)
        bloco_uuid = str(uuid4())
        blocks[bloco_uuid] = bloco
        blocks_layout["items"].append(bloco_uuid)
    # Agora temos os dados do bloco e do layout, podemos atualizar a área
    response = session.get(path)
    if response.status_code == 404:
        logger.info(f"Ignorando {path}: Conteúdo não encontrado")
        continue
    payload = {"blocks": blocks, "blocks_layout": blocks_layout}
    ALTERACOES[path] = payload

logger.info(f"Total de áreas a serem atualizadas: {len(ALTERACOES)}")

for path, payload in ALTERACOES.items():
    logger.info(f"Atualizando {path}")
    response = session.patch(path, json=payload)
    if response.status_code > 300:
        logger.error(f"Erro ao atualizar '{path}': {response.status_code}")
    else:
        logger.info(f"Área '{path}' atualizada com sucesso")