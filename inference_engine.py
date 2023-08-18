def infere_each(proposition: str, facts: list[str], inferred: dict):
    modified_proposition = proposition

    modified_proposition = modified_proposition.replace(' e ', ' and ')
    modified_proposition = modified_proposition.replace(' ou ', ' or ')

    for fact in facts:
        if fact in modified_proposition:
            modified_proposition = modified_proposition.replace(fact, 'True')
    for condition in conditions:
        if condition in modified_proposition:
            modified_proposition = modified_proposition.replace(condition, 'False')

    result = eval(modified_proposition)
    if result and (proposition not in facts):
        facts.append(proposition)

    return eval(modified_proposition)

def infere(conclusions, facts, inferred):
    for conclusion in conclusions:
        res = infere_each(conclusions[conclusion], facts, inferred)
        if inferred[conclusion] == False and res:
            print('restarting')
            inferred[conclusion] = True
            facts.append(conclusion)
            infere(conclusions, facts, inferred)
            break

if __name__ == '__main__':
    # escreva regras sem acento e sem letras maiusculas
    # ex: se chover entao nao vou para a faculdade

    rules = [
        'se vou tomar banho entao vou ficar limpo',
        'se estou fedido entao vou tomar banho',
        'se vou ficar limpo e quero sair entao vou para a faculdade',
        'se vou para a faculdade ou vou tomar banho entao vou para a festa'
    ]

    facts = [
        'vou tomar banho',
        'vou para a faculdade',
        'vou para a festa',
    ]

    conclusions = {}
    for rule in rules:
        conclusions[rule[rule.find('entao') + 6:]] = rule[3:rule.find(' entao')]

    inferred = {rule[rule.find('entao') + 6:]: False for rule in rules}

    conditions = [rule[3:rule.find(' entao')] for rule in rules]

    c = conditions.copy()
    for i, condition in enumerate(c):
        if ' e ' in condition:
            conditions.remove(condition)
            conditions = conditions + condition.split(' e ')
        if ' ou ' in condition:
            conditions.remove(condition)
            conditions = conditions + condition.split(' ou ')

    for condition in conditions:
        inferred[condition] = False

    for fact in facts:
        inferred[fact] = True

    scan = int(input('Inferência para frente ou para trás?\n1) Frente\n2) Trás\n'))
    if scan == 1:
        infere(conclusions, facts, inferred)
        print('(qualquer proposição não especificada como verdade será considerada falsa)')
        print('inferências feitas:')
        for s in inferred:
            print(s, '->', inferred[s])
    else:
        for conclusion in conclusions:
            if inferred[conclusion]:
                print('inferência:', conclusions[conclusion])
