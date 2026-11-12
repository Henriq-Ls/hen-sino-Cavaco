"""Catálogo canônico de acordes e formas candidatas do cavaquinho.

As formas existentes foram importadas como candidatas na afinação Ré–Sol–Si–Ré.
Os dados por corda são a única representação da posição; notas e tuplas
compatíveis com a interface antiga são derivadas.
"""

AFINACAO_REFERENCIA = ("Ré", "Sol", "Si", "Ré")
AFINACAO_PITCHES = (2, 7, 11, 2)  # classes de nota, da 4ª à 1ª corda

NOMES_NOTA_POR_CLASSE = (
    "Dó", "Dó#", "Ré", "Ré#", "Mi", "Fá",
    "Fá#", "Sol", "Sol#", "Lá", "Lá#", "Si",
)
CLASSE_POR_CIFRA = {
    "C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5,
    "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11,
}
RAIZ_POR_CLASSE = {valor: raiz for raiz, valor in CLASSE_POR_CIFRA.items()}
NOME_RAIZ_POR_CIFRA = {
    "C": "Dó", "C#": "Dó sustenido", "D": "Ré", "D#": "Ré sustenido",
    "E": "Mi", "F": "Fá", "F#": "Fá sustenido", "G": "Sol",
    "G#": "Sol sustenido", "A": "Lá", "A#": "Lá sustenido", "B": "Si",
}
EQUIVALENTE_BEMOL_POR_RAIZ = {
    "C#": "Db", "D#": "Eb", "F#": "Gb", "G#": "Ab", "A#": "Bb",
}

RAIZES_CROMATICAS = tuple(
    {
        "cifra": raiz,
        "nome": NOME_RAIZ_POR_CIFRA[raiz],
        "classe": classe,
        "equivalente": EQUIVALENTE_BEMOL_POR_RAIZ.get(raiz),
    }
    for raiz, classe in CLASSE_POR_CIFRA.items()
)

TIPOS_ACORDE = (
    {"chave": "maior", "nome": "Maior", "sufixo": "", "intervalos": (0, 4, 7)},
    {"chave": "menor", "nome": "Menor", "sufixo": "m", "intervalos": (0, 3, 7)},
    {
        "chave": "dominante7",
        "nome": "Sétima dominante",
        "sufixo": "7",
        "intervalos": (0, 4, 7, 10),
    },
)
TIPOS_ACORDE_POR_CHAVE = {
    tipo["chave"]: tipo for tipo in TIPOS_ACORDE
}


def id_acorde(raiz, tipo):
    """Gera uma chave estável para uma raiz canônica e uma qualidade."""
    return f"{raiz.lower().replace('#', '_sustenido')}_{tipo}"


ACORDES_CANONICOS = []
ACORDES_POR_ID = {}
ACORDE_POR_CIFRA = {}
for _raiz_info in RAIZES_CROMATICAS:
    for _tipo in TIPOS_ACORDE:
        _raiz = _raiz_info["cifra"]
        _sufixo = _tipo["sufixo"]
        _equivalentes = []
        if _raiz_info["equivalente"]:
            _equivalentes.append(_raiz_info["equivalente"] + _sufixo)
        if _tipo["chave"] == "maior":
            _nome = f"{NOME_RAIZ_POR_CIFRA[_raiz]} maior"
        elif _tipo["chave"] == "menor":
            _nome = f"{NOME_RAIZ_POR_CIFRA[_raiz]} menor"
        else:
            _nome = f"{NOME_RAIZ_POR_CIFRA[_raiz]} com sétima dominante"
        _acorde = {
            "id": id_acorde(_raiz, _tipo["chave"]),
            "raiz": _raiz,
            "tipo": _tipo["chave"],
            "nome": _nome,
            "cifra": _raiz + _sufixo,
            "equivalentes": _equivalentes,
            "formas": [],
        }
        ACORDES_CANONICOS.append(_acorde)
        ACORDES_POR_ID[_acorde["id"]] = _acorde
        ACORDE_POR_CIFRA[_acorde["cifra"]] = _acorde
        for _equivalente in _equivalentes:
            ACORDE_POR_CIFRA[_equivalente] = _acorde

ACORDES_CANONICOS = tuple(ACORDES_CANONICOS)

# E# e B# existem aqui apenas como cifras alternativas para F e C. Eles não
# criam registros canônicos nem duplicam formas.
for _tipo in TIPOS_ACORDE:
    _sufixo = _tipo["sufixo"]
    ACORDE_POR_CIFRA["E#" + _sufixo] = ACORDES_POR_ID[
        id_acorde("F", _tipo["chave"])
    ]
    ACORDE_POR_CIFRA["B#" + _sufixo] = ACORDES_POR_ID[
        id_acorde("C", _tipo["chave"])
    ]

# Visão antiga mantida para que a página atual continue funcionando sem edição.
RAIZES = (
    {"cifra": "C", "nome": "Dó"},
    {"cifra": "D", "nome": "Ré"},
    {"cifra": "E", "nome": "Mi"},
    {"cifra": "F", "nome": "Fá"},
    {"cifra": "G", "nome": "Sol"},
    {"cifra": "A", "nome": "Lá"},
    {"cifra": "B", "nome": "Si"},
)
CATEGORIAS = (
    {"chave": "maior", "nome": "Maior"},
    {"chave": "menor", "nome": "Menor"},
    {"chave": "sustenida", "nome": "Fundamental sustenida"},
    {"chave": "dominante7", "nome": "Dominante com sétima"},
)

_FORMAS_LEGADAS = (
    # raiz natural, linha antiga, cifra/nome exibidos, casas 4ª→1ª,
    # dedos 4ª→1ª, observação
    ("C", "maior", "C", "Dó maior", (2, 0, 1, 2), (2, 0, 1, 3), ""),
    ("D", "maior", "D", "Ré maior", (0, 2, 3, 4), (0, 1, 2, 3), ""),
    ("E", "maior", "E", "Mi maior", (2, 1, 0, 2), (2, 1, 0, 3), ""),
    ("F", "maior", "F", "Fá maior", (3, 2, 1, 3), (3, 2, 1, 4), ""),
    ("G", "maior", "G", "Sol maior", (0, 0, 0, 0), (0, 0, 0, 0), ""),
    ("A", "maior", "A", "Lá maior", (2, 2, 2, 2), (1, 1, 1, 1),
     "Pestana nas quatro cordas."),
    ("B", "maior", "B", "Si maior", (4, 4, 4, 4), (1, 1, 1, 1),
     "Pestana nas quatro cordas."),
    ("C", "menor", "Cm", "Dó menor", (1, 0, 1, 1), (1, 0, 2, 3), ""),
    ("D", "menor", "Dm", "Ré menor", (0, 2, 3, 3), (0, 1, 2, 3), ""),
    ("E", "menor", "Em", "Mi menor", (2, 0, 0, 2), (1, 0, 0, 2), ""),
    ("F", "menor", "Fm", "Fá menor", (3, 1, 1, 3), (3, 1, 2, 4), ""),
    ("G", "menor", "Gm", "Sol menor", (0, 3, 3, 5), (0, 1, 1, 3),
     "Pode usar meia pestana nas cordas 3 e 2."),
    ("A", "menor", "Am", "Lá menor", (2, 2, 1, 2), (2, 3, 1, 4),
     "Forma candidata; comparar com a imagem preferida pelo aluno."),
    ("B", "menor", "Bm", "Si menor", (0, 4, 3, 4), (0, 2, 1, 3), ""),
    ("C", "sustenida", "C#", "Dó sustenido maior",
     (3, 1, 2, 3), (3, 1, 2, 4), ""),
    ("D", "sustenida", "D#", "Ré sustenido maior",
     (1, 3, 4, 5), (1, 2, 3, 4), ""),
    ("E", "sustenida", "E#", "Mi sustenido maior",
     (3, 2, 1, 3), (3, 2, 1, 4), "Som enarmônico de Fá maior."),
    ("F", "sustenida", "F#", "Fá sustenido maior",
     (4, 3, 2, 4), (3, 2, 1, 4), ""),
    ("G", "sustenida", "G#", "Sol sustenido maior",
     (1, 1, 1, 1), (1, 1, 1, 1), "A nota Si# soa como Dó."),
    ("A", "sustenida", "A#", "Lá sustenido maior",
     (0, 3, 3, 3), (0, 1, 1, 1), "Som enarmônico de Si bemol maior."),
    ("B", "sustenida", "B#", "Si sustenido maior",
     (2, 0, 1, 2), (2, 0, 1, 3), "Som enarmônico de Dó maior."),
    ("C", "dominante7", "C7", "Dó com sétima dominante",
     (2, 3, 1, 5), (2, 3, 1, 4), ""),
    ("D", "dominante7", "D7", "Ré com sétima dominante",
     (0, 2, 1, 4), (0, 2, 1, 3), ""),
    ("E", "dominante7", "E7", "Mi com sétima dominante",
     (0, 1, 0, 2), (0, 1, 0, 2), ""),
    ("F", "dominante7", "F7", "Fá com sétima dominante",
     (3, 2, 1, 1), (3, 2, 1, 1),
     "Pode usar meia pestana nas cordas 2 e 1."),
    ("G", "dominante7", "G7", "Sol com sétima dominante",
     (0, 0, 0, 3), (0, 0, 0, 1), ""),
    ("A", "dominante7", "A7", "Lá com sétima dominante",
     (2, 2, 2, 5), (1, 1, 1, 4),
     "O dedo 1 pode fazer meia pestana nas cordas 4, 3 e 2."),
    ("B", "dominante7", "B7", "Si com sétima dominante",
     (1, 2, 0, 4), (1, 2, 0, 3), ""),
)


def _classe_alvo(acorde):
    raiz = CLASSE_POR_CIFRA[acorde["raiz"]]
    intervalos = TIPOS_ACORDE_POR_CHAVE[acorde["tipo"]]["intervalos"]
    return {(raiz + intervalo) % 12 for intervalo in intervalos}


def calcular_classes_forma(forma):
    """Calcula as classes de nota das quatro cordas, na ordem 4ª→1ª."""
    return tuple(
        (AFINACAO_PITCHES[indice] + corda["casa"]) % 12
        for indice, corda in enumerate(forma["cordas"])
    )


def notas_da_forma(forma):
    return tuple(
        NOMES_NOTA_POR_CLASSE[classe]
        for classe in calcular_classes_forma(forma)
    )


def _id_canonico_da_forma_legada(raiz, categoria):
    classe = CLASSE_POR_CIFRA[raiz]
    if categoria == "sustenida":
        classe = (classe + 1) % 12
        tipo = "maior"
    elif categoria in ("maior", "menor", "dominante7"):
        tipo = categoria
    else:
        raise ValueError(f"Categoria antiga desconhecida: {categoria}")
    raiz_canonica = RAIZ_POR_CLASSE[classe]
    return id_acorde(raiz_canonica, tipo)


_FORMA_LEGADA_POR_CELULA = {}
for _indice, _item in enumerate(_FORMAS_LEGADAS, start=1):
    _raiz, _categoria, _cifra, _nome, _casas, _dedos, _observacao = _item
    _acorde_id = _id_canonico_da_forma_legada(_raiz, _categoria)
    _acorde = ACORDES_POR_ID[_acorde_id]
    _forma_id = f"legada_{_raiz}_{_categoria}_{_indice:02d}"
    _forma = {
        "id": _forma_id,
        "cordas": tuple(
            {
                "numero": 4 - indice,
                "casa": casa,
                "dedo": _dedos[indice],
            }
            for indice, casa in enumerate(_casas)
        ),
        "calculado": False,
        "fonte": [],
        "testado_pelo_aluno": "nenhum",
        "escolhida": False,
        "origem_legada": {
            "raiz_coluna": _raiz,
            "linha": _categoria,
            "cifra": _cifra,
        },
        "observacao": _observacao,
    }
    if len(_forma["cordas"]) != 4 or any(
        corda["casa"] < 0 or corda["casa"] > 7
        for corda in _forma["cordas"]
    ):
        raise ValueError(f"Forma legada inválida: {_forma_id}")
    if set(calcular_classes_forma(_forma)) != _classe_alvo(_acorde):
        raise ValueError(
            f"A forma legada {_cifra} não confere com a cifra por cálculo."
        )
    _forma["calculado"] = True
    _acorde["formas"].append(_forma)
    _FORMA_LEGADA_POR_CELULA[(_raiz, _categoria)] = (
        _acorde,
        _forma,
        _cifra,
        _nome,
    )


def _visao_legada(raiz_coluna, categoria, acorde, forma, cifra, nome):
    notas = notas_da_forma(forma)
    cordas = tuple(
        {
            "numero": corda["numero"],
            "nota": notas[indice],
            "casa": corda["casa"],
            "dedo": corda["dedo"],
        }
        for indice, corda in enumerate(forma["cordas"])
    )
    categoria_nome = next(
        item["nome"] for item in CATEGORIAS if item["chave"] == categoria
    )
    detalhe = (
        "Notas conferidas por cálculo; a forma ainda não foi confirmada "
        "em fonte independente nem testada no instrumento."
    )
    return {
        "id": acorde["id"],
        "forma_id": forma["id"],
        "raiz": raiz_coluna,
        "tipo": acorde["tipo"],
        "categoria": categoria,
        "categoria_nome": categoria_nome,
        "cifra": cifra,
        "nome": nome,
        "equivalentes": list(acorde["equivalentes"]),
        "afinação": AFINACAO_REFERENCIA,
        "casas": tuple(corda["casa"] for corda in forma["cordas"]),
        "dedos": tuple(corda["dedo"] for corda in forma["cordas"]),
        "notas_resultantes": notas,
        "cordas": cordas,
        "status": "Candidata calculada",
        "status_detalhe": detalhe,
        "observação": forma["observacao"] or detalhe,
    }


MATRIZ_ACORDES = {
    (raiz, categoria): _visao_legada(
        raiz, categoria, *_FORMA_LEGADA_POR_CELULA[(raiz, categoria)]
    )
    for raiz, categoria, *_resto in _FORMAS_LEGADAS
}
ACORDES_MATRIZ = tuple(MATRIZ_ACORDES.values())
ACORDE_BM_EXEMPLO = MATRIZ_ACORDES[("B", "menor")]

CATEGORIAS_GRADE = (
    {"chave": "maior", "nome": "Maior", "tipo": "maior", "alteracao": 0},
    {"chave": "menor", "nome": "Menor", "tipo": "menor", "alteracao": 0},
    {
        "chave": "sustenida",
        "nome": "Raiz sustenida",
        "tipo": "maior",
        "alteracao": 1,
    },
    {
        "chave": "sustenida_menor",
        "nome": "Raiz sustenida menor",
        "tipo": "menor",
        "alteracao": 1,
    },
    {
        "chave": "dominante7",
        "nome": "Sétima dominante",
        "tipo": "dominante7",
        "alteracao": 0,
    },
    {
        "chave": "sustenida_dominante7",
        "nome": "Raiz sustenida com sétima",
        "tipo": "dominante7",
        "alteracao": 1,
    },
)

_RAIZES_NATURAIS_PITCH = (
    ("C", 0), ("D", 2), ("E", 4), ("F", 5), ("G", 7), ("A", 9), ("B", 11),
)


def _cifra_de_celula(raiz_coluna, tipo, alteracao):
    if not alteracao:
        raiz_exibida = raiz_coluna
    elif raiz_coluna in ("E", "B"):
        raiz_exibida = raiz_coluna + "#"
    else:
        classe = (CLASSE_POR_CIFRA[raiz_coluna] + 1) % 12
        raiz_exibida = RAIZ_POR_CLASSE[classe]
    return raiz_exibida + TIPOS_ACORDE_POR_CHAVE[tipo]["sufixo"]


GRADE_APRESENTACAO = tuple(
    tuple(
        {
            "linha": linha["chave"],
            "coluna_raiz": raiz_coluna,
            "cifra": _cifra_de_celula(
                raiz_coluna, linha["tipo"], linha["alteracao"]
            ),
            "acorde_id": id_acorde(
                RAIZ_POR_CLASSE[
                    (CLASSE_POR_CIFRA[raiz_coluna] + linha["alteracao"]) % 12
                ],
                linha["tipo"],
            ),
            "alias": linha["alteracao"] == 1 and raiz_coluna in ("E", "B"),
        }
        for raiz_coluna, _classe in _RAIZES_NATURAIS_PITCH
    )
    for linha in CATEGORIAS_GRADE
)
CELULAS_GRADE = {
    (celula["linha"], celula["coluna_raiz"]): celula
    for linha in GRADE_APRESENTACAO
    for celula in linha
}
ALIASES_GRADE = {
    celula["cifra"]: celula["acorde_id"]
    for linha in GRADE_APRESENTACAO
    for celula in linha
}
GRADE_ACORDES = {
    "colunas": tuple(raiz for raiz, _classe in _RAIZES_NATURAIS_PITCH),
    "linhas": CATEGORIAS_GRADE,
    "celulas": GRADE_APRESENTACAO,
}


def validar_catalogo():
    """Confere cardinalidade, consistência das formas e unicidade escolhida."""
    if len(ACORDES_CANONICOS) != 36:
        raise ValueError("O catálogo precisa ter 36 acordes canônicos.")
    if len(GRADE_APRESENTACAO) != 6 or any(
        len(linha) != 7 for linha in GRADE_APRESENTACAO
    ):
        raise ValueError("A grade derivada precisa ter seis linhas e sete colunas.")
    if len({celula["acorde_id"] for linha in GRADE_APRESENTACAO
            for celula in linha}) != 36:
        raise ValueError("A grade deve apontar para 36 acordes sonoros distintos.")
    todas_as_formas = []
    for acorde in ACORDES_CANONICOS:
        formas = acorde["formas"]
        if sum(bool(forma["escolhida"]) for forma in formas) > 1:
            raise ValueError(f"Mais de uma forma escolhida para {acorde['cifra']}.")
        for forma in formas:
            if len(forma["cordas"]) != 4:
                raise ValueError(f"A forma {forma['id']} precisa ter 4 cordas.")
            if forma["calculado"] and set(calcular_classes_forma(forma)) != (
                _classe_alvo(acorde)
            ):
                raise ValueError(f"A forma {forma['id']} não confere por cálculo.")
            todas_as_formas.append(forma["id"])
    if len(todas_as_formas) != 28 or len(set(todas_as_formas)) != 28:
        raise ValueError("As 28 formas legadas precisam ser preservadas.")
    if len(MATRIZ_ACORDES) != 28:
        raise ValueError("A visão de compatibilidade deve conter 28 células.")
    return True


validar_catalogo()
