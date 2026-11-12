"""Gera e avalia formas candidatas sem dependência de Qt.

As saídas são sugestões calculadas; o script não atesta conforto nem validação
no instrumento.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
from pathlib import Path

try:
    from .referencias import (
        ACORDES_CANONICOS,
        ACORDES_POR_ID,
        ACORDE_POR_CIFRA,
        AFINACAO_PITCHES,
        CLASSE_POR_CIFRA,
        NOMES_NOTA_POR_CLASSE,
        TIPOS_ACORDE_POR_CHAVE,
    )
except ImportError:  # permite também `python ACORDES/gerador_formas.py`
    from referencias import (  # type: ignore[no-redef]
        ACORDES_CANONICOS,
        ACORDES_POR_ID,
        ACORDE_POR_CIFRA,
        AFINACAO_PITCHES,
        CLASSE_POR_CIFRA,
        NOMES_NOTA_POR_CLASSE,
        TIPOS_ACORDE_POR_CHAVE,
    )


SEQUENCIAS_CICLICAS = (
    ("G", "D", "Em", "C"),
    ("C", "Am", "F", "G"),
    ("D", "Bm", "A", "G"),
    ("C", "G", "Bm", "Em"),
    ("E", "C#m", "F#m", "B7", "A", "B"),
    ("G#m", "E", "B", "F#"),
    ("F#", "B", "D#m", "C#"),
    ("Dm", "Bb", "F", "Em", "G"),
)

ROTULOS_CORDAS = ("4ª", "3ª", "2ª", "1ª")
MAX_FORMAS_POR_ACORDE_NA_AVALIACAO = 8
AVISO_VALIDACAO = "sugestão calculada, sem teste no instrumento"


def _tons_do_acorde(acorde):
    raiz = CLASSE_POR_CIFRA[acorde["raiz"]]
    intervalos = TIPOS_ACORDE_POR_CHAVE[acorde["tipo"]]["intervalos"]
    return {(raiz + intervalo) % 12 for intervalo in intervalos}


def _casas_da_forma(forma):
    if "casas" in forma:
        return tuple(forma["casas"])
    return tuple(corda["casa"] for corda in forma["cordas"])


def _dedos_da_forma(forma):
    if "dedos" in forma:
        return tuple(forma["dedos"])
    return tuple(corda["dedo"] for corda in forma["cordas"])


def _dedos_validos(casas, dedos):
    """Um dedo só pode cobrir cordas vizinhas na mesma casa."""
    for dedo in set(dedos) - {0}:
        indices = [indice for indice, valor in enumerate(dedos) if valor == dedo]
        if len({casas[indice] for indice in indices}) != 1:
            return False
        if indices != list(range(min(indices), max(indices) + 1)):
            return False
    return True


def _melhor_digitacao(casas):
    pressionadas = [indice for indice, casa in enumerate(casas) if casa > 0]
    if not pressionadas:
        return (0, 0, 0, 0)

    melhores = []
    for dedos_pressionados in product((1, 2, 3, 4), repeat=len(pressionadas)):
        dedos = [0, 0, 0, 0]
        for indice, dedo in zip(pressionadas, dedos_pressionados):
            dedos[indice] = dedo
        dedos = tuple(dedos)
        if _dedos_validos(casas, dedos):
            quantidade = len(set(dedos) - {0})
            tem_pestana = any(dedos.count(dedo) > 1 for dedo in set(dedos) - {0})
            melhores.append((quantidade, tem_pestana, dedos))
    if not melhores:
        return None
    return min(melhores, key=lambda item: (item[0], item[1], item[2]))[2]


def _pestanas(casas, dedos):
    resultado = []
    for dedo in sorted(set(dedos) - {0}):
        indices = [indice for indice, valor in enumerate(dedos) if valor == dedo]
        if len(indices) > 1:
            resultado.append({
                "dedo": dedo,
                "casa": casas[indices[0]],
                "cordas": tuple(ROTULOS_CORDAS[indice] for indice in indices),
            })
    return tuple(resultado)


def _ordenacao_forma(forma):
    casas = forma["casas"]
    return (
        forma["abertura"],
        forma["dedos_usados"],
        bool(forma["pestanas"]),
        max(casas),
        sum(casas),
        casas,
        forma["dedos"],
    )


def enumerar_formas(acorde, max_casa=7):
    """Enumera posições completas de quatro cordas entre a casa zero e o limite."""
    if max_casa < 0:
        raise ValueError("max_casa precisa ser zero ou maior.")

    alvo = _tons_do_acorde(acorde)
    formas_atuais = {
        _casas_da_forma(forma)
        for forma in acorde["formas"]
    }
    notas_por_corda = tuple(
        tuple((afinação + casa) % 12 for casa in range(max_casa + 1))
        for afinação in AFINACAO_PITCHES
    )
    resultado = []

    for casas in product(range(max_casa + 1), repeat=4):
        notas = tuple(notas_por_corda[indice][casa]
                      for indice, casa in enumerate(casas))
        if set(notas) != alvo:
            continue

        dedos = _melhor_digitacao(casas)
        if dedos is None:
            continue
        pressionadas = [casa for casa in casas if casa > 0]
        abertura = (
            max(pressionadas) - min(pressionadas) if pressionadas else 0
        )
        pestanas = _pestanas(casas, dedos)
        contagem_notas = Counter(notas)
        repetidas = tuple(
            (NOMES_NOTA_POR_CLASSE[nota], quantidade)
            for nota, quantidade in sorted(contagem_notas.items())
            if quantidade > 1
        )
        forma = {
            "id": "calc_" + "_".join(map(str, casas)),
            "casas": tuple(casas),
            "dedos": tuple(dedos),
            "pestanas": pestanas,
            "abertura": abertura,
            "dedos_usados": len(set(dedos) - {0}),
            "cordas_soltas": tuple(
                ROTULOS_CORDAS[indice]
                for indice, casa in enumerate(casas)
                if casa == 0
            ),
            "nota_baixo": NOMES_NOTA_POR_CLASSE[notas[0]],
            "baixo_e_fundamental": (
                notas[0] == CLASSE_POR_CIFRA[acorde["raiz"]]
            ),
            "notas": tuple(NOMES_NOTA_POR_CLASSE[nota] for nota in notas),
            "notas_repetidas": repetidas,
            "calculado": True,
            "testado_pelo_aluno": "nenhum",
            "escolhida": False,
            "forma_atual": tuple(casas) in formas_atuais,
        }
        resultado.append(forma)

    return sorted(resultado, key=_ordenacao_forma)


def custo_troca(forma_a, forma_b):
    """Compara troca por dedos reposicionados, deslocamento e cordas alteradas.

    O total é a soma simples desses três indicadores; serve apenas para ordenar
    sugestões calculadas, não para afirmar conforto físico.
    """
    casas_a, casas_b = _casas_da_forma(forma_a), _casas_da_forma(forma_b)
    dedos_a, dedos_b = _dedos_da_forma(forma_a), _dedos_da_forma(forma_b)

    posicoes_a = {
        dedo: tuple(
            (indice, casas_a[indice])
            for indice, valor in enumerate(dedos_a)
            if valor == dedo
        )
        for dedo in set(dedos_a) - {0}
    }
    posicoes_b = {
        dedo: tuple(
            (indice, casas_b[indice])
            for indice, valor in enumerate(dedos_b)
            if valor == dedo
        )
        for dedo in set(dedos_b) - {0}
    }
    dedos_mudam = sum(
        posicoes_a.get(dedo) != posicoes_b.get(dedo)
        for dedo in set(posicoes_a) | set(posicoes_b)
    )
    menor_a = min((casa for casa in casas_a if casa > 0), default=0)
    menor_b = min((casa for casa in casas_b if casa > 0), default=0)
    deslocamento = abs(menor_a - menor_b)
    cordas_mudam = sum(a != b for a, b in zip(casas_a, casas_b))
    return {
        "dedos_mudam": dedos_mudam,
        "deslocamento_mao": deslocamento,
        "cordas_mudam": cordas_mudam,
        "total": dedos_mudam + deslocamento + cordas_mudam,
    }


def avaliar_sequencia(sequencia, formas_por_acorde, max_formas=8):
    """Escolhe uma forma fixa por acorde e inclui a volta ao primeiro acorde."""
    acordes = []
    for cifra in sequencia:
        acorde = ACORDE_POR_CIFRA.get(cifra)
        if acorde is None:
            raise ValueError(f"Cifra sem acorde canônico: {cifra}")
        acordes.append(acorde)

    ids_unicos = tuple(dict.fromkeys(acorde["id"] for acorde in acordes))
    opcoes = {}
    for acorde_id in ids_unicos:
        opcoes[acorde_id] = formas_por_acorde[acorde_id][:max_formas]
        if not opcoes[acorde_id]:
            raise ValueError(
                f"Nenhuma forma candidata para "
                f"{ACORDES_POR_ID[acorde_id]['cifra']}."
            )

    melhor = None
    for selecao in product(*(opcoes[acorde_id] for acorde_id in ids_unicos)):
        por_id = dict(zip(ids_unicos, selecao))
        trocas = []
        for indice, acorde in enumerate(acordes):
            proximo = acordes[(indice + 1) % len(acordes)]
            trocas.append({
                "de": sequencia[indice],
                "para": sequencia[(indice + 1) % len(sequencia)],
                **custo_troca(por_id[acorde["id"]], por_id[proximo["id"]]),
            })
        total = sum(troca["total"] for troca in trocas)
        chave_desempate = tuple(
            opcoes[acorde_id].index(por_id[acorde_id])
            for acorde_id in ids_unicos
        )
        chave = (total, chave_desempate)
        if melhor is None or chave < melhor["chave"]:
            melhor = {
                "chave": chave,
                "formas": por_id,
                "trocas": trocas,
                "custo_total": total,
            }

    return melhor


def _formatar_pestanas(pestanas):
    if not pestanas:
        return "não"
    return "; ".join(
        f"dedo {p['dedo']} na casa {p['casa']} "
        f"({', '.join(p['cordas'])})"
        for p in pestanas
    )


def _formatar_forma(forma, indice):
    casas = "-".join(map(str, forma["casas"]))
    dedos = "-".join(map(str, forma["dedos"]))
    soltas = ", ".join(forma["cordas_soltas"]) or "nenhuma"
    repetidas = ", ".join(
        f"{nota} ×{quantidade}"
        for nota, quantidade in forma["notas_repetidas"]
    ) or "nenhuma"
    atual = " [FORMA ATUAL]" if forma["forma_atual"] else ""
    return (
        f"{indice:>4}. casas {casas}; dedos {dedos}; "
        f"pestana {_formatar_pestanas(forma['pestanas'])}; "
        f"abertura {forma['abertura']}; cordas soltas {soltas}; "
        f"baixo {forma['nota_baixo']} "
        f"({'fundamental' if forma['baixo_e_fundamental'] else 'outra nota'}); "
        f"notas repetidas {repetidas}{atual}"
    )


def _relatorio_formas(formas_por_acorde, max_casa):
    linhas = [
        "FORMAS CANDIDATAS DE CAVAQUINHO — CASAS 0 A 7",
        f"Afinação de cálculo: Ré–Sol–Si–Ré (4ª→1ª). Limite: {max_casa}.",
        f"Estado de todas as entradas: {AVISO_VALIDACAO}.",
        "As posições exigem as quatro cordas, todos os tons do acorde e nenhuma "
        "nota alheia.",
        "Abertura = maior casa pressionada menos menor casa pressionada.",
        "A atribuição de dedos é uma hipótese geométrica; não comprova execução.",
        "",
    ]
    for acorde in ACORDES_CANONICOS:
        formas = formas_por_acorde[acorde["id"]]
        linhas.append(
            f"## {acorde['cifra']} — {acorde['nome']} "
            f"({len(formas)} formas candidatas)"
        )
        if not formas:
            linhas.append("Nenhuma forma encontrada sob os critérios atuais.")
        else:
            linhas.extend(
                _formatar_forma(forma, indice)
                for indice, forma in enumerate(formas, start=1)
            )
        linhas.append("")
    return "\n".join(linhas).rstrip() + "\n"


def _relatorio_sequencias(formas_por_acorde):
    linhas = [
        "SEQUÊNCIAS CÍCLICAS AVALIADAS",
        "Cada ciclo inclui a troca do último acorde de volta ao primeiro.",
        f"Estado: {AVISO_VALIDACAO}. O custo é uma soma heurística, não uma "
        "medida objetiva de conforto.",
        "Custo por troca = dedos reposicionados + diferença entre as menores "
        "casas pressionadas + cordas cuja casa muda.",
        "Cada acorde mantém a mesma forma durante todo o ciclo.",
        "",
    ]
    for numero, sequencia in enumerate(SEQUENCIAS_CICLICAS, start=1):
        resultado = avaliar_sequencia(sequencia, formas_por_acorde)
        linhas.append(f"## {numero}. {' – '.join(sequencia)}")
        linhas.append(f"Custo calculado do ciclo: {resultado['custo_total']}")
        linhas.append(
            "Combinação de menor custo heurístico entre os candidatos avaliados:"
        )
        cifras_unicas = tuple(dict.fromkeys(sequencia))
        for cifra in cifras_unicas:
            acorde_id = ACORDE_POR_CIFRA[cifra]["id"]
            forma = resultado["formas"][acorde_id]
            linhas.append(
                f"- {cifra}: casas "
                f"{'-'.join(map(str, forma['casas']))}; dedos "
                f"{'-'.join(map(str, forma['dedos']))}; "
                f"baixo {forma['nota_baixo']}."
            )
        linhas.append("Trocas, incluindo a volta:")
        for troca in resultado["trocas"]:
            linhas.append(
                f"- {troca['de']} → {troca['para']}: "
                f"dedos {troca['dedos_mudam']}, "
                f"deslocamento {troca['deslocamento_mao']} casas, "
                f"cordas {troca['cordas_mudam']}; "
                f"custo {troca['total']}."
            )
        linhas.append("")
    return "\n".join(linhas).rstrip() + "\n"


def gerar_relatorios(diretorio_saida=None, max_casa=7):
    """Gera os dois relatórios TXT pedidos e devolve um resumo das contagens."""
    if diretorio_saida is None:
        diretorio_saida = Path(__file__).resolve().parents[1] / "aprendizado_cavaquinho"
    else:
        diretorio_saida = Path(diretorio_saida)
    diretorio_saida.mkdir(parents=True, exist_ok=True)

    formas_por_acorde = {
        acorde["id"]: enumerar_formas(acorde, max_casa=max_casa)
        for acorde in ACORDES_CANONICOS
    }
    formas_path = diretorio_saida / "08_FORMAS_CANDIDATAS_0A7.txt"
    sequencias_path = diretorio_saida / "09_SEQUENCIAS_AVALIADAS.txt"
    formas_path.write_text(
        _relatorio_formas(formas_por_acorde, max_casa), encoding="utf-8"
    )
    sequencias_path.write_text(
        _relatorio_sequencias(formas_por_acorde), encoding="utf-8"
    )
    return {
        "formas_por_acorde": {
            acorde["cifra"]: len(formas_por_acorde[acorde["id"]])
            for acorde in ACORDES_CANONICOS
        },
        "formas_totais": sum(map(len, formas_por_acorde.values())),
        "arquivos": (str(formas_path), str(sequencias_path)),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Gera formas candidatas e avalia sequências cíclicas."
    )
    parser.add_argument(
        "--max-casa",
        type=int,
        default=7,
        help="maior casa incluída na busca (padrão: 7)",
    )
    args = parser.parse_args()
    resumo = gerar_relatorios(max_casa=args.max_casa)
    print(f"Formas candidatas geradas: {resumo['formas_totais']}")
    for cifra, quantidade in resumo["formas_por_acorde"].items():
        print(f"{cifra}: {quantidade}")
    for caminho in resumo["arquivos"]:
        print(caminho)


if __name__ == "__main__":
    main()
