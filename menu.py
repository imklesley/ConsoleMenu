'''
Menu Padronizado. Função Cria menu com título, lista de submenus, lista de controles, explicação do menu
'''


def menu(titulo: str = 'Insira o título deste menu'.title().upper(),
         lista_de_itens_submenus: list = [], lista_itens_controle: list = [], explicar: bool = True,
         explicacao: str = 'Informe sua explicação para que seja adicionada ao menu.',
         pedir_resposta: bool = True, mostrar_lista_no_menu: bool = False, lista: list = []) -> int:
    """Exibe Menu Padrão e Retorna o valor inserido pelo usuário. A resposta do user já foi tratada evitando assim erros
    :param titulo: Uma string que será o título do menu.
    :param lista_de_itens_submenus: Uma lista com as opções de execução e/ou redirecionamento para outros menus.
    :param lista_itens_controle: Uma lista com as opções de controle, como por ex.: "Cancelar a operação".
    :param explicar: Um bool que irá informar ao algoritmo se o usuário quer ou não alguma mensagem explicando o menu.
    :param explicacao: Uma string que conterá o texto de explicação do menu.
    :param pedir_resposta: Um bool que irá permitir solicitar ou não uma resposta do usuário. Isso pq existe funções que não precisam de resposta imediata do menu
    :param mostrar_lista_no_menu: um bool para permitir que o menu exiba uma lista. Isso é para deixar a função de inserção das ações do submenu3 mais fácil de interagir.
    :return valor inteiro para o redirecionamento para outros menus. Obs.: Sempre será retornado o valor que o user inseriu menos 1

    Obs.1: Os nomes dos sub-menus não podem ter mais 64 caracteres. Caso tenha a grade será esticada. Não ficando uma aparência bacana
    Obs.2: A contagem segue o padrão de máquina. O primeiro valor vale 0, o segundo 1, etc.

    """
    print('\n\n\n\n\n\n')
    titulo_com_espacos = ''
    for i in titulo:
        if i != ' ':
            titulo_com_espacos += i
            titulo_com_espacos += ' '
        else:
            titulo_com_espacos += i

    print(f"┌{33 * '─'}{' G R A M B O T ':^}{32 * '─'}┐")
    print('│                                                                                │')
    print(f'│     {titulo_com_espacos.upper():<{75}}│')
    if explicar == True:
        print(f'│                                                                                │')
        print('│-------- H E L P -  M E --------------------------------------------------------│', end='')

        explicacao = explicacao.title()
        cont = 0
        print('\n│    ', end='')
        for i in range(len(explicacao)):
            if cont > 70 and explicacao[i] == ' ':
                print(' ', end=f'    │\n│   {explicacao[i]}')
                cont = 0
            elif cont > 70 and explicacao[i] != ' ':
                print('-', end=f'    │\n│    {explicacao[i]}')
                cont = 0
            else:
                print(explicacao[i], end='')
            cont += 1

        print((76 - cont) * ' ', end='')
        print('│')

        if not len(lista_de_itens_submenus) > 0:
            print(f'''│--------------------------------------------------------------------------------│
│                                                                                │''')

    if len(lista_de_itens_submenus) > 0:
        print(f'''│--------------------------------------------------------------------------------│
│                                                                                │''', )
        for i in range(len(lista_de_itens_submenus)):
            print(f'''│    [{i + 1:^5}]  -  {lista_de_itens_submenus[i].title():64}│''')

        print(f'''│                                                                                │''')
        print(f'''│                                                                                │''')

    if len(lista_itens_controle) > 0:
        print(f'''|{31 * '─'}  C O N T R O L E {31 * '─'}|''')
        print(f'''│                                                                                │''')
        for j in range(len(lista_itens_controle)):
            print(f'''│    [{-1 * (j + 1):^5}]  -  {lista_itens_controle[j].title():64}│                ''')
        print('│                                                                                │')
        print('│                                                                                │')
        print('└────────────────────────────────────────────────────────────────────────────────┘')
    else:
        print('│                                                                                │')
        print('│                                                                                │')
        print('└────────────────────────────────────────────────────────────────────────────────┘')
    if mostrar_lista_no_menu:
        print(f'Lista de Comandos: {lista}')
    if pedir_resposta == True:
        resposta = input('Informe a opção desejada: ')
        while True:
            try:
                if int(resposta) == 0:
                    resposta = input(
                        'Opção Inexistente, tente outra para prosseguir. Informe a opção desejada: '.title())
                elif int(resposta) >= 1 and int(resposta) <= len(lista_de_itens_submenus):
                    resposta = int(resposta) - 1
                    break
                elif int(resposta) < -len(lista_itens_controle) or int(resposta) > len(lista_de_itens_submenus):
                    resposta = input(
                        'Opção Inexistente, tente outra para prosseguir. Informe a opção desejada: '.title())
                else:
                    break
            except:
                resposta = input(
                    'Entrada Inválida. Somente as opções exibidas podem ser escolhidas. Tente Novamente. Informe a opção desejada: '.title())
                continue

        return int(resposta)
    else:
        return 1000000000  # valor inteiro do menu que nunca será válido
