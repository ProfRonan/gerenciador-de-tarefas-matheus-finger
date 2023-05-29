"""
Modulo que implementa um gerenciador de tarefas
"""


lista_de_tarefas: list[dict[str]] = [
    {"prioridade": True, "tarefa": "Estudar Python"},
    {"prioridade": False, "tarefa": "Tomar banho"},
    {"prioridade": False, "tarefa": "Assistir série"},
]


def adicionar_tarefa(prioridade: bool, tarefa: str):
    """
    Adiciona uma tarefa na lista de tarefas
    Lança exceções caso a prioridade seja inválida ou a tarefa já exista

    Args:
        prioridade (bool): True se a tarefa tem prioridade alta, False caso contrário
        tarefa (str): string que representa a tarefa
    """
    # TODO: coloque o código aqui para adicionar um tarefa na lista
    # Caso a prioridade não seja True ou False, levante uma exceção
    # do tipo ValueError com a mensagem "Prioridade inválida"
    # Caso a tarefa já exista na lista, levante uma exceção do tipo ValueError
    # com a mensagem "Tarefa já existe"
    if prioridade != 0 and prioridade != 1:
        raise ValueError('Prioridade inválida')
    for i in lista_de_tarefas:
        if i['tarefa'].lower() == tarefa.lower():
            raise ValueError('Tarefa já existe')
    novo = {'prioridade': prioridade, 'tarefa': tarefa}
    lista_de_tarefas.append(novo)


def remove_tarefas(índices: tuple[int]):
    """
    Remove várias tarefas da lista de tarefas de uma vez, dado uma tupla de índices
    Lança exceções caso a tarefa não exista

    Args:
        índices (tuple[int]): tupla de inteiros que representam os índices das tarefas
                             que devem ser removidas da lista.
    """
    # TODO: coloque o código aqui para remover um tarefa na lista
    # Caso a tarefa não exista na lista, levante uma exceção do tipo ValueError
    # com a mensagem "Tarefa não existe"
    if not lista_de_tarefas:
        raise ValueError('Não há nada na lista para remover')
    if índices:
        for i in range(len(índices)-1, -1, -1):
            if índices[i] >= len(lista_de_tarefas):
                raise ValueError('Índice da tarefa inválido')
            if not lista_de_tarefas[i]:
                raise ValueError('Não há tarefas com esse índice')
            lista_de_tarefas.pop(índices[i])



def encontra_tarefa(tarefa: str) -> int:
    """
    Encontra o índice de uma tarefa na lista de tarefas
    Lança exceções caso a tarefa não exista

    Args:
        tarefa (str): string que representa a tarefa
    """
    # TODO: coloque o código aqui para encontrar um tarefa na lista
    # Caso a tarefa não exista na lista, levante uma exceção do tipo ValueError
    # com a mensagem "Tarefa não existe"
    for i in range(0, len(lista_de_tarefas)):
        if lista_de_tarefas[i]['tarefa'].lower() == tarefa.lower():
            return i
    raise ValueError('Tarefa não existe')


def ordena_por_prioridade():
    """
    Ordena a lista de tarefas por prioridade com as tarefas prioritárias no
    início da lista, seguidas pelas tarefas não prioritárias.
    As tarefas prioritárias devem ser ordenadas por ordem alfabética e as
    tarefas não prioritárias devem ser ordenadas por ordem alfabética.
    """
    # TODO: coloque o código aqui para ordenar a lista de tarefas por prioridade
    # com as tarefas prioritárias no início da lista, seguidas pelas tarefas
    # não prioritárias.
    # As tarefas prioritárias devem ser ordenadas por ordem alfabética e as
    # tarefas não prioritárias devem ser ordenadas por ordem alfabética.
    prior = []
    non_prior = []
    global lista_de_tarefas
    for i in lista_de_tarefas:
        if i['prioridade'] == 0:
            non_prior.append(i)
        else:
            prior.append(i)
    prior = sorted(prior, key=lambda d: d['tarefa']) 
    non_prior = sorted(non_prior, key=lambda d: d['tarefa']) 
    lista_de_tarefas = []
    for i in prior:
        lista_de_tarefas.append(i)
    for i in non_prior:
        lista_de_tarefas.append(i)


def get_lista_de_tarefas():
    """
    Retorna somente o texto das tarefas da lista de tarefas
    """
    texts = []
    for tarefa in lista_de_tarefas:
        texto = tarefa["tarefa"]
        prioridade = tarefa["prioridade"]
        texts.append(f"{'*' if prioridade else ''} {texto}")
    return tuple(texts)
