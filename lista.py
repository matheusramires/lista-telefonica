import psycopg2

db_host = 'IP'
db_name = 'nome_do_schema'
db_port = 'porta'
db_user = 'postgres'
db_password = 'senha_do_banco_de_dados'
connect = psycopg2.connect(host=db_host, dbname=db_name, port=db_port, user=db_user, password=db_password)
cur = connect.cursor()


#adiciona contatos
def adicionar_contatos():
    print('\033[1;96mDeseja adicionar contatos?\n	\033[1;92m 1 - SIM\n    \033[1;91m 2 - NÃO ')
    op = int(input('\n\033[1;96mOPÇÃO: '))

    if op == 1:
        nome = input('\033[1;94mNome: ')
        tel = str(input('\033[1;94mTelefone com DDD: '))
        sql = f"insert into contatos.lista (nome, tel) values ('{nome}','{tel}')"
        cur.execute(sql)
        connect.commit()
        print("\n\033[1;96mContato Salvo\n\n")
        print('\033[1;96mDeseja adicionar contatos?\n	\033[1;92m 1 - SIM\n    \033[1;91m 2 - NÃO ')
        op = int(input('\n\033[1;96mOPÇÃO:'))
    else:
        print('OK! Até mais!')
    connect.commit()

#ver todos os contatos
def ver_contatos():
    print()
    sql = 'SELECT id, nome, tel from contatos.lista order by nome'
    cur.execute(sql)
    result = cur.fetchall()
    contador = len(result)
    print(f'Contatos: {contador}')
    for row in result:
        print('\033[1;34mnome: '+row[1].upper()+ '	\033[1;33mtelefone: '+row[2])

#pesquisa contatos
def pesquisar_contato():

    nome1 = str(input('\nPesquisar: ')).lower()
    sql = "SELECT nome, tel from contatos.lista where nome like '{}%'".format(nome1)
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        print('\033[1;34mnome: ' + row[0].upper() + '	\033[1;33mtelefone: ' + row[1])

#exclui contato
def excluir_contato():
    nome1 = str(input('\nDigite o nome que você deseja excluir: ')).lower()
    print('\nVocê deseja excluir esse contato?\n')
    sql = "SELECT id, nome, tel from contatos.lista where nome like '{}%'".format(nome1)
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        print('\033[1;34mnome: ' + row[1].upper() + '	\033[1;33mtelefone: ' + row[2])
    print('\n\033[1;92m 1 - SIM\n\033[1;91m 2 - NÃO')
    op = int(input('\n\033[1;96mOPÇÃO: '))
    if op == 1:

        sql1 = f"DELETE FROM contatos.lista where id = {row[0]}"
        cur.execute(sql1)
        print('\nContato excluido.')
    else: print('Ok.')
    connect.commit()

#edita contatos
def editar_contato():
    print('\n\n\033[1;32m1 - Editar nome\n2 - Editar número\n')
    op3 = int(input('\033[1;96mOPÇÃO: '))
    if op3 == 1:
        nome1 = str(input('\nDigite o nome que você deseja editar: ')).lower()
        print('\nVocê deseja editar esse contato?\n')
        sql = "SELECT id, nome, tel from contatos.lista where nome like '{}%'".format(nome1)
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            print('\033[1;34mnome: ' + row[1].upper() + '	\033[1;33mtelefone: ' + row[2])
        print('\n\033[1;92m 1 - SIM\n\033[1;91m 2 - NÃO')
        op = int(input('\n\033[1;96mOPÇÃO: '))
        if op == 1:
            novo_nome = input("digite o novo nome: ")
            sql1 = f"UPDATE contatos.lista SET nome = '{novo_nome}' where id = {row[0]}"
            cur.execute(sql1)
            print('\nContato atualizado.')
        else:
            print('Ok.')
        connect.commit()
    elif op3 == 2:
        nome1 = str(input('\nDigite o nome que você deseja editar: ')).lower()
        print('\nVocê deseja editar esse contato?\n')
        sql = "SELECT id, nome, tel from contatos.lista where nome like '{}%'".format(nome1)
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            print('\033[1;34mnome: ' + row[1].upper() + '	\033[1;33mtelefone: ' + row[2])
        print('\n\033[1;92m 1 - SIM\n\033[1;91m 2 - NÃO')
        op = int(input('\n\033[1;96mOPÇÃO: '))
        if op == 1:
            novo_tel = input("digite o novo numero de telefone: ")
            sql1 = f"UPDATE contatos.lista SET tel = '{novo_tel}' where id = {row[0]}"
            cur.execute(sql1)
            print('\nContato atualizado.')
        else:
            print('Ok.')
            connect.commit()

try:
    print('\n\033[1;96mSelecione uma opção:\n'
          '        \033[1;32m1 - Pesquisar\n'
          '     	2 - Ver todos os Contatos\n'
          '     	3 - Adicionar Contato\n'
          '     	4 - Excluir Contato\n'
          '        5 - Editar Contato\n'
          '        0 - Sair')
    op1= int(input('\033[1;96mOPÇÃO: '))

    while op1 != 0:
        if op1 == 1:
            pesquisar_contato()
        elif op1 == 2:
            ver_contatos()
        elif op1 == 3:
            adicionar_contatos()
            break
        elif op1 == 4:
            excluir_contato()
            break
        elif op1 == 5:
            editar_contato()
            break
        else:
            print('ok')
    print('\n\033[1;96mSelecione uma opção:\n'
          '        \033[1;32m1 - Pesquisar\n'
          '     	2 - Ver todos os Contatos\n'
          '     	3 - Adicionar Contato\n'
          '     	4 - Excluir Contato\n'
          '        5 - Editar Contato\n'
          '        0 - Sair')
    op1 = int(input('\033[1;96mOPÇÃO: '))
except:
    print("\n\033[1;91mOps! Ocorreu algum erro!\n\n    Tente Novamente!")

cur.close()
connect.commit()
connect.close()