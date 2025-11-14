from pathlib import Path   # <-- IMPORTAR Path AQUI
import json
import unicodedata
from typing import Dict, List, Tuple

# Caminhos base
BASE_DIR = Path(__file__).resolve().parent.parent  # .../analisador-curriculos-ia
DATA_DIR = BASE_DIR / "data"


# ---------- UTILITÁRIOS DE TEXTO ----------
def normalizar_texto(texto: str) -> str:
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(ch for ch in texto if unicodedata.category(ch) != "Mn")
    return texto



# ---------- DICIONÁRIOS DE SKILLS E SINÔNIMOS ----------

SINONIMOS_HARD = {
    "javascript": ["javascript", "js"],
    "node.js": ["node.js", "nodejs", "node js"],
    "typescript": ["typescript", "ts"],
    "sql": ["sql"],
    "postgresql": ["postgresql", "postgres"],
    "git": ["git", "controle de versao"],
    "docker": ["docker", "containers"],
    "aws": ["aws", "amazon web services"]
}

SINONIMOS_SOFT = {
    "trabalho em equipe": ["trabalho em equipe", "team player"],
    "comunicacao": ["boa comunicacao", "comunicacao", "comunicativo"],
    "proatividade": ["proativo", "proatividade", "iniciativa"],
    "resolucao de problemas": ["resolver problemas", "resolucao de problemas"],
    "lideranca": ["lideranca", "lider", "coordenei equipe", "gestao de pessoas"]
}


def contem_alguma(expressions: List[str], texto: str) -> bool:
    return any(exp in texto for exp in expressions)


# ---------- AVALIAÇÃO DE CANDIDATO ----------

def avaliar_hard_skills(
    texto_norm: str,
    hard_desejadas: Dict[str, int]
) -> Tuple[float, List[str], List[str]]:
    peso_total = sum(hard_desejadas.values())
    peso_encontrado = 0
    presentes = []
    ausentes = []

    for skill, peso in hard_desejadas.items():
        sinonimos = SINONIMOS_HARD.get(skill, [skill])
        if contem_alguma(sinonimos, texto_norm):
            peso_encontrado += peso
            presentes.append(skill)
        else:
            ausentes.append(skill)

    score = peso_encontrado / peso_total if peso_total > 0 else 0.0
    return score, presentes, ausentes


def avaliar_soft_skills(
    texto_norm: str,
    soft_desejadas: Dict[str, int]
) -> Tuple[float, List[str], List[str]]:
    peso_total = sum(soft_desejadas.values())
    peso_encontrado = 0
    presentes = []
    ausentes = []

    for skill, peso in soft_desejadas.items():
        sinonimos = SINONIMOS_SOFT.get(skill, [skill])
        if contem_alguma(sinonimos, texto_norm):
            peso_encontrado += peso
            presentes.append(skill)
        else:
            ausentes.append(skill)

    score = peso_encontrado / peso_total if peso_total > 0 else 0.0
    return score, presentes, ausentes


def avaliar_candidato(
    candidato: Dict,
    vaga: Dict
) -> Dict:
    texto = candidato["texto_curriculo"]
    texto_norm = normalizar_texto(texto)

    hard_desejadas = vaga.get("hard_skills_desejadas", {})
    soft_desejadas = vaga.get("soft_skills_desejadas", {})

    score_hard, hard_presentes, hard_ausentes = avaliar_hard_skills(texto_norm, hard_desejadas)
    score_soft, soft_presentes, soft_ausentes = avaliar_soft_skills(texto_norm, soft_desejadas)

    score_total = 0.7 * score_hard + 0.3 * score_soft

    explicacao = {
        "hard_skills_encontradas": hard_presentes,
        "hard_skills_faltantes": hard_ausentes,
        "soft_skills_encontradas": soft_presentes,
        "soft_skills_faltantes": soft_ausentes,
        "score_hard": round(score_hard, 2),
        "score_soft": round(score_soft, 2),
        "score_total": round(score_total, 2)
    }

    return {
        "nome": candidato["nome"],
        "score_total": score_total,
        "explicacao": explicacao
    }


# ---------- MAIN / RANKING ----------

def carregar_json(nome_arquivo: str):
    caminho = DATA_DIR / nome_arquivo
    with caminho.open("r", encoding="utf-8") as f:
        return json.load(f)



def main():
    vaga = carregar_json("job_profile.json")
    candidatos = carregar_json("candidatos.json")

    resultados = []
    for cand in candidatos:
        avaliacao = avaliar_candidato(cand, vaga)
        resultados.append(avaliacao)

    # Ordena por score_total desc
    resultados.sort(key=lambda x: x["score_total"], reverse=True)

    print(f"Vaga: {vaga.get('titulo', 'Sem título')}")
    print("=" * 60)
    print("RANKING DE CANDIDATOS\n")

    for i, r in enumerate(resultados, start=1):
        e = r["explicacao"]
        print(f"{i}. {r['nome']}")
        print(f"   Score total: {e['score_total']} (Hard: {e['score_hard']}, Soft: {e['score_soft']})")
        print(f"   Hard skills encontradas: {', '.join(e['hard_skills_encontradas']) or 'nenhuma'}")
        print(f"   Hard skills faltantes : {', '.join(e['hard_skills_faltantes']) or 'nenhuma'}")
        print(f"   Soft skills encontradas: {', '.join(e['soft_skills_encontradas']) or 'nenhuma'}")
        print(f"   Soft skills faltantes : {', '.join(e['soft_skills_faltantes']) or 'nenhuma'}")
        print("-" * 60)


if __name__ == "__main__":
    main()
