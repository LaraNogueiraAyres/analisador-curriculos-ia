#📄 RecrutAI — Sistema Inteligente de Análise de Currículos

Um mini-projeto de Inteligência Artificial para seleção automatizada de candidatos, baseado em análise de hard skills, soft skills e ranking explicável.

##📌 Sobre o Projeto

O RecrutAI foi desenvolvido para apoiar equipes de RH na triagem inicial de currículos de desenvolvedores de software.
O sistema:

Lê a descrição de uma vaga

Analisa currículos automaticamente

Identifica competências técnicas e comportamentais

Gera um score de compatibilidade

Explica cada decisão da IA (skills encontradas e faltantes)

Produz um ranking ordenado dos melhores candidatos

É um protótipo funcional, simples de executar, e ideal para expansão futura.

##🧠 Funcionalidades

✔️ Extração automática de hard skills
✔️ Detecção de soft skills
✔️ Sistema de pesos configuráveis
✔️ Score de compatibilidade (0 a 1)
✔️ Explicação detalhada das decisões
✔️ Ranking dos candidatos
✔️ Arquitetura limpa e extensível

##📂 Estrutura do Projeto
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

##🗂 Exemplos de Arquivos
📄 job_profile.json
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
[
  {
    "nome": "João Silva",
    "texto_curriculo": "Desenvolvedor Node.js com 3 anos de experiência em APIs REST..."
  }
]

##▶️ Como Executar
1. Clone o repositório
git clone [https://github.com/seu-usuario/analisador-curriculos-ia.git](https://github.com/LaraNogueiraAyres/analisador-curriculos-ia)
cd analisador-curriculos-ia

2. (Opcional) Crie um ambiente virtual
python -m venv venv


Ativar:

Windows

venv\Scripts\activate


Linux/Mac

source venv/bin/activate

3. Instale as dependências
pip install -r requirements.txt

4. Execute o sistema
python src/main.py

##📊 Exemplo de Saída
1. João Silva
   Score total: 0.87 (Hard: 0.92, Soft: 0.75)
   Hard skills encontradas: node.js, javascript, sql
   Hard skills faltantes : docker
   Soft skills encontradas: comunicacao
   Soft skills faltantes : lideranca, proatividade
---------------------------------------------------------

##🧩 Como o Sistema Funciona
🔤 1. Normalização de Texto

minúsculas

remoção de acentos

limpeza de caracteres

🧩 2. Dicionário de Sinônimos

Exemplo:

"node.js": ["node.js", "nodejs", "node js"]

🧠 3. Avaliação de Skills

busca por termos no currículo

soma de pesos atribuídos pela vaga

🧮 4. Score Final
score_total = 0.7 * score_hard + 0.3 * score_soft

💬 5. Geração de Explicações

habilidades encontradas

habilidades ausentes

notas parciais e finais

##🚀 Possíveis Melhorias

Conversão para API (FastAPI)

Interface web (React, Vue, ou Flask + HTML)

Upload e leitura de currículos em PDF/Docx

Uso de embeddings para análise semântica

Treinamento de modelo supervisionado
