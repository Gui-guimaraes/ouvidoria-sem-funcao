'''
Grupo: Guilherme Guimarães, Jonathan Ferreira, Carlos Eduardo, Massimiliano Ribeiro, Gustavo Nóbrega de Carvalho, Riquelme Alves Trajano
'''

from operacoesbd import *

opcao = 0
reclamacoes = []

conexao = abrirBancoDados('localhost','root','senha','ouvidoria')

while opcao != 5:
    print('Ola! seja bem-vindo a ouvidoria')
    print('1 - Registrar reclamação')
    print('2 - Listar reclamações')
    print('3 - Pesquisar reclamação por código')
    print('4 - Remover reclamação')
    print('5 - Sair')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        # Registrar reclamação
        nome = input("Digite seu nome: ")
        assunto = input("Digite o assunto da reclamação: ")
        mensagem = input("Digite a mensagem da reclamação: ")
        inserirReclamacao = 'insert into sistema_ouvidoria (nome, assunto, mensagem) values (%s, %s, %s)'
        dados = (nome, assunto, mensagem)
        insertNoBancoDados(conexao, inserirReclamacao, dados)
        print()
        print('Reclamação registrada com sucesso!')
        print('Obrigado por nos ajudar a melhorar o atendimento!')
        print()
    elif opcao == 2:
        # Listar reclamações
        consultarListagem = 'select * from sistema_ouvidoria'
        listaReclamacao = listarBancoDados(conexao, consultarListagem)
        if len(listaReclamacao) == 0:
            print('Não há reclamações registradas')
        else:
            print()
            print('Listando reclamações...')
            for reclamacao in listaReclamacao:
                print('Código: ', reclamacao[0])
                print('Nome: ', reclamacao[1])
                print('Assunto: ', reclamacao[3])
                print('Mensagem: ', reclamacao[4])
                print()
    elif opcao == 3:
        # pesquisar reclamação por código
        print()
        consultarListagem = 'select * from sistema_ouvidoria'
        listaReclamacao = listarBancoDados(conexao, consultarListagem)
        if len(listaReclamacao) == 0:
            print('Não há reclamações registradas')
        else:
            print()
            print('Listando reclamações...')
            for reclamacao in listaReclamacao:
                print('Código: ', reclamacao[0])
                print('Nome: ', reclamacao[1])
                print('Assunto: ', reclamacao[3])
                print('Mensagem: ', reclamacao[4])
                print()
        print('Pesquisar reclamação por código')
        print()

        codigo = input('Digite o código da reclamação a ser pesquisada: ')
        consultarReclamacao = 'select nome, assunto, mensagem from sistema_ouvidoria where codigo_reclamacao = ' + codigo
        pesquisarReclamacao = listarBancoDados(conexao, consultarReclamacao)
        if len(pesquisarReclamacao) == 0:
            print('Não há reclamações registradas')
        else:
            print()
            print('Pesquisando reclamação...')
            for reclamacao in pesquisarReclamacao:
                print('Nome: ', reclamacao[0])
                print('Assunto: ', reclamacao[1])
                print('Mensagem: ', reclamacao[2])
        print()
    elif opcao == 4:
        # Remover reclamação
            print()
            # Remover reclamação
            print('listas de reclamações:')
            consultarListagem = 'select * from sistema_ouvidoria'
            listaReclamacao = listarBancoDados(conexao, consultarListagem)
            if len(listaReclamacao) == 0:
                print('Não há reclamações registradas')
            else:
                print()
                print('Listando reclamações...')
                for reclamacao in listaReclamacao:
                    print('Código: ', reclamacao[0])
                    print('Nome: ', reclamacao[1])
                    print('Assunto: ', reclamacao[3])
                    print('Mensagem: ', reclamacao[4])
                    print()
            
            
            codigo = input('Digite o código da reclamação a ser removida: ')
            remover_reclamacao = 'delete from sistema_ouvidoria where codigo_reclamacao = %s'
            dados = (codigo,)
            excluirBancoDados(conexao, remover_reclamacao, dados)
            print('Reclamação removida com sucesso!')
            print()

    elif opcao == 5:
        # Sair
        print()
        print('Obrigado por nos ajudar a melhorar o atendimento!')
        print('Até mais!')
        print()
encerrarBancoDados(conexao)