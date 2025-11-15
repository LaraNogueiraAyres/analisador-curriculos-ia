📄 Sistema de Análise Inteligente de Currículos (RecrutAI)

Um mini-projeto de Inteligência Artificial para seleção inteligente de candidatos, utilizando análise automática de hard skills e soft skills e geração de ranking com explicações.

📌 Descrição do Projeto

Este sistema foi desenvolvido para auxiliar processos de Recrutamento e Seleção, permitindo que um gerente de RH avalie candidatos automaticamente com base em seus currículos.

A aplicação:

lê uma descrição da vaga (skills desejadas e pesos);

analisa currículos de candidatos;

identifica hard skills e soft skills;

calcula um score de compatibilidade com a vaga;

gera um ranking dos melhores candidatos;

fornece explicações detalhadas sobre a decisão da IA.

O objetivo é oferecer um protótipo funcional de IA explicável, simples de rodar e fácil de evoluir para API ou interface web.

🧠 Funcionalidades Principais

✔️ Extração automática de habilidades técnicas
✔️ Identificação de soft skills
✔️ Análise por pesos configuráveis
✔️ Score final entre 0 e 1
✔️ Justificativa completa (skills presentes/faltantes)
✔️ Ranking ordenado dos candidatos
✔️ Leitura e validação de arquivos JSON
✔️ Arquitetura preparada para expansão

🗂 Estrutura do Projeto
analisador-curriculos-ia/
├── README.md
├── requirements.txt
│
├── data/
│   ├── job_profile.json      # descrição da vaga
│   └── candidatos.json       # currículos dos candidatos
│
└── src/
    └── main.py               # código principal

🧩 Arquivos de Entrada
📄 job_profile.json

Define a vaga e suas skills desejadas:

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

📄 candidatos.json

Lista de candidatos:

[
  {
    "nome": "João Silva",
    "texto_curriculo": "Desenvolvedor Node.js com 3 anos de experiência..."
  }
]

▶️ Como Executar o Projeto
1. Clonar o repositório
git clone https://github.com/seu-usuario/analisador-curriculos-ia.git
cd analisador-curriculos-ia

2. Criar ambiente virtual (opcional, recomendado)
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

3. Instalar dependências
pip install -r requirements.txt

4. Executar o código
python src/main.py


A saída exibirá o ranking dos candidatos, por exemplo:

1. João Silva
   Score total: 0.87 (Hard: 0.92, Soft: 0.75)
   Hard skills encontradas: node.js, javascript
   Soft skills encontradas: comunicacao
--------------------------------------------------------

🔍 Como Funciona a IA

Normalização do texto

remove acentos

tudo minúsculo

Dicionário de sinônimos

ex.: "node js", "nodejs" → "node.js"

Detecção de skills

verifica presença de expressões mapeadas no texto

Cálculo de score

score_total = 0.7 * score_hard + 0.3 * score_soft


Geração de explicação

skills encontradas

skills faltantes

scores individuais

🚀 Evoluções Futuras

Transformar em API REST (FastAPI / Flask)

Interface Web (React/Vue)

Upload de arquivos PDF e extração via NLP

Embeddings para detecção semântica de habilidades

Modelo de machine learning treinável

📚 Tecnologias Utilizadas

Python 3.x

json

unicodedata

pathlib

Estrutura modular para expansão
