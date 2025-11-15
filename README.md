Sistema de Análise Inteligente de Currículos

Mini-projeto de Inteligência Artificial para apoio ao recrutamento de candidatos na área de desenvolvimento de software.

1. Descrição do Projeto

Este sistema analisa currículos automaticamente, identificando hard skills, soft skills e calculando o nível de compatibilidade de cada candidato com uma vaga específica.
O protótipo desenvolvido:

lê a descrição de uma vaga (com pesos para cada skill);

analisa currículos textuais;

busca habilidades técnicas e comportamentais;

calcula um score de compatibilidade;

gera explicações sobre as decisões;

produz um ranking final ordenado.

O objetivo é demonstrar uma aplicação prática de IA explicável no contexto de Recursos Humanos.

2. Estrutura do Projeto
analisador-curriculos-ia/
├── README.md
├── requirements.txt
│
├── data/
│   ├── job_profile.json
│   └── candidatos.json
│
└── src/
    └── main.py

3. Arquivos de Entrada
3.1. job_profile.json

Define a vaga e os pesos atribuídos às habilidades.

Exemplo:

{
  "titulo": "Desenvolvedor Backend Node.js Pleno",
  "hard_skills_desejadas": {
    "javascript": 3,
    "node.js": 3,
    "typescript": 2,
    "sql": 2
  },
  "soft_skills_desejadas": {
    "trabalho em equipe": 2,
    "comunicacao": 2
  }
}

3.2. candidatos.json

Lista de currículos analisados.

Exemplo:

[
  {
    "nome": "João Silva",
    "texto_curriculo": "Desenvolvedor Node.js com 3 anos de experiência..."
  }
]

4. Como Executar
4.1. Criar ambiente virtual (opcional)
python -m venv venv
venv\Scripts\activate        (Windows)
source venv/bin/activate     (Linux/Mac)

4.2. Instalar dependências
pip install -r requirements.txt

4.3. Executar

Na raiz do projeto:

python src/main.py

5. Funcionamento da IA

O sistema segue as etapas:

5.1. Normalização de texto

tudo em minúsculo

remoção de acentos

remoção de caracteres especiais

5.2. Dicionários de sinônimos

Mapeiam diferentes formas de escrever uma mesma skill, por exemplo:

node.js → ["node.js", "nodejs", "node js"]

5.3. Avaliação de hard skills e soft skills

Cada skill procurada contribui com um peso específico.

5.4. Cálculo do score final
score_total = 0.7 * score_hard + 0.3 * score_soft

5.5. Geração da explicação

O sistema informa:

skills encontradas

skills ausentes

score parcial de hard skills

score parcial de soft skills

score final

5.6. Ranking

Os candidatos são ordenados do mais compatível ao menos compatível.

6. Exemplo de Saída
1. João Silva
   Score total: 0.87 (Hard: 0.92, Soft: 0.75)
   Hard skills encontradas: node.js, javascript
   Hard skills faltantes : docker
   Soft skills encontradas: comunicacao
   Soft skills faltantes : liderança, proatividade
--------------------------------------------------------

7. Possíveis Evoluções

API REST com FastAPI

Interface web com React/Vue

Upload de currículos em PDF

Extração automática com NLP

Embeddings para busca semântica

Explicabilidade mais sofisticada

8. Tecnologias Utilizadas

Python 3.x

json

unicodedata

pathlib
