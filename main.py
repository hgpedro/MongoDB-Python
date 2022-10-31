from datetime import datetime
from PIL import Image
import webbrowser
import pymongo
import time

client = pymongo.MongoClient("mongodb+srv://db_user:r6j6lFL5uakNBfW1@cluster0.1cijj.mongodb.net/python?retryWrites=true&w=majority")
db = client.get_database("python")

while True:

    collection7 = db.get_collection("operacaobasicavariavel")
    operacaobasicavariavel = collection7.find({})

    collection8 = db.get_collection("potenciaeraciacaovariavel")
    potenciaeraciacaovariavel = collection8.find({})

    collection9 = db.get_collection("expressaonumericavariavel")
    expressaonumericavariavel = collection9.find({})

    collection10 = db.get_collection("multiplosdivisoresvariavel")
    multiplosdivisoresvariavel = collection10.find({})

    collection11 = db.get_collection("operacaobasicapolinomiovariavel")
    operacaobasicapolinomiovariavel = collection11.find({})

    collection12 = db.get_collection("fracoesdecimaisedizimasvariavel")
    fracoesdecimaisedizimasvariavel = collection12.find({})

    collection13 = db.get_collection("notacaocientificavariavel")
    notacaocientificavariavel = collection13.find({})

    # Banco de dados para os dias
    for col7 in operacaobasicavariavel:
        d1 = col7["d1"]  

    for col8 in potenciaeraciacaovariavel:
        d2 = col8["d2"]  
        
    for col9 in expressaonumericavariavel:
        d3 = col9["d3"] 

    for col10 in multiplosdivisoresvariavel:
        d4 = col10["d4"]

    for col11 in operacaobasicapolinomiovariavel:
        d5 = col11["d5"]

    for col12 in fracoesdecimaisedizimasvariavel:
        d6 = col12["d6"]

    for col13 in notacaocientificavariavel:
        d7 = col13["d7"]
        
            
    collection7 = db.get_collection("operacaobasicavariavel")
    operacaobasicavariavel = collection7.find({})

    collection8 = db.get_collection("potenciaeraciacaovariavel")
    potenciaeraciacaovariavel = collection8.find({})

    collection9 = db.get_collection("expressaonumericavariavel")
    expressaonumericavariavel = collection9.find({})

    collection10 = db.get_collection("multiplosdivisoresvariavel")
    multiplosdivisoresvariavel = collection10.find({})

    collection11 = db.get_collection("operacaobasicapolinomiovariavel")
    operacaobasicapolinomiovariavel = collection11.find({})

    collection12 = db.get_collection("fracoesdecimaisedizimasvariavel")
    fracoesdecimaisedizimasvariavel = collection12.find({})

    collection13 = db.get_collection("notacaocientificavariavel")
    notacaocientificavariavel = collection13.find({})

    # Banco de dados liberação para revisão
    for cole7 in operacaobasicavariavel:
        revisãooperaçãobasica = cole7["variavelrevisao"]

    for cole8 in potenciaeraciacaovariavel:
        revisãopotenciaerad = cole8["variavelrevisao"]

    for cole9 in expressaonumericavariavel:
        revisãoexpressaonum = cole9["variavelrevisao"]
        
    for cole10 in multiplosdivisoresvariavel:
        revisãomultiplosdivisores = cole10["variavelrevisao"]
            
    for cole11 in operacaobasicapolinomiovariavel:
        revisãooppolinomios = cole11["variavelrevisao"]
            
    for cole12 in fracoesdecimaisedizimasvariavel:
        revisãofracoes = cole12["variavelrevisao"]

    for cole13 in notacaocientificavariavel:
        revisãonotcient = cole13["variavelrevisao"]

    Menu = input("""
 • 1- Instruções de uso do programa
 • 2- Estudar uma nova matéria
 • 3- Revisão 24h
 • 4- Revisão 7Dias
 • 5- Revisão 30Dias
 • 6- Fontes de pesquisa
 • 7- Sair
 • 8- RESETAR O PROGRAMA
 • Digite a opção desejada: """)
    print("")

    if Menu.isdigit():
        Menu = int(Menu)

        if Menu == 1:
            # Mostrar instruções
            print("""
        Bem vindo ao GoMat! 

    Um programa feito para te ajudar nas matérias básicas da Matemática! Vamos começar?
    - Para estudar um novo tópico entre na opção 2, lá você encontrará resumos mais completos e ao final, exercícios relacionados 
    a matéria estudada. Não se preocupe que terá acesso ao gabarito e sua pontuação. Ao final você receberá uma indicação para a 
    revisão 1, que deverá ser feita 24h depois;
    - Após 24h de finalizar o estudo de uma matéria nova, entre na opção 3. Lá você encontrará resumos mais breves com exercícios no 
    final para melhor fixação do tópico. Novamente terá acesso ao gabarito, pontuação e a indicação para a revisão 2 que deverá ser 
    feita 6 dias após a finalização da Revisão 1;
    - Entre na opção 3 após os 6 dias para a revisão 2. Tudo no mesmo modelo da revisão 1, com exercícios, gabarito, pontuação e a 
    indicação para a revisão 3, a última, que deve ser feita 23 dias apos a revisão 2;
    - Na opção 5, você terá acesso a última revisão nos mesmos moldes das outras revisões para finalizar o seu ciclo, lembre-se de 
    fazê-lá 23 dias após a revisão 2;
    - Para ter acesso as fontes de pesquisa, entre na opção 6;
    - Caso queira sair do programa, escolha a opção 7;
    - Caso o usuário escolha a opção 8, as variáveis vão resetar e o programa começará do zero novamente; 
    - Indicamos sempre ao usuário seguir as indicações de revisões para melhor aprendizado e fixação da matéria;
    - Indicamos também que o usuário utilize uma agenda ou calendário para não perder os dias das revisões e para melhor organização.
    Vamos estudar?

        Equipe GoMat""")

        elif Menu == 2:
            # Novo menu com opções de matérias
            while True:
                materias = input("""
 • 1- Operações básicas
 • 2- Potenciação e radiciação
 • 3- Expressões numéricas
 • 4- Múltiplos, divisores, MDC e MMC
 • 5- Operações básicas com polinômios
 • 6- Frações, decimais e dizimas
 • 7- Notação cientifíca
 • 8- Voltar ao menu principal
 • Digite a opção desejada: """)
                print()

                if materias.isdigit():
                    materias = int(materias)

                    if materias == 1:
                        collection0 = db.get_collection("operacaobasica")
                        operaçaobasica = collection0.find({})

                        for col0 in operaçaobasica:
                            print(f" > {col0['nome']} < ")
                            print(col0['def'])                        
                            print(col0['adicao'])
                            print(col0['subtracao'])
                            print(col0['multiplicacao'])
                            print(col0['divisao'])

                        while True:
                            decisão = input("• Gostaria de ver uma vídeo aula(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                decisãoautomatica = input ("• Gostaria de abrir a vídeo aula automaticamente(s/n)? ")
                                if decisãoautomatica == "s" or decisãoautomatica == "S" or decisãoautomatica == "Sim" or decisãoautomatica == "sim":
                                    url = 'https://www.youtube.com/watch?v=h3sFlP8Rmqc'
                                    webbrowser.open_new(url)
                                    break
                                elif decisãoautomatica == "n" or decisãoautomatica == "N" or decisãoautomatica == "Não" or decisãoautomatica == "não":
                                    print("• Link da vídeo aula: https://www.youtube.com/watch?v=h3sFlP8Rmqc")
                                    break
                                else:
                                    continue
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue

                        print()
                        input("> Pressione enter para fazer os exercícios ...")
                        print()

                        OperBásica = ["• 5 + 7", "• −5 + 7", "• −2 + 4 − 5 + 6 − 8 + 13", 
                        "• 18 ÷ 9", "• (9) * (−7)", "• (−3) * (−5)", "• −20 ÷ (5)"]
                        gabarito2 = [12, 2, 8, 2, -63 , 15, -4]
                        respostas = []
                        Pontuação = 0

                        n = 0
                        y = 0
                        while True:
                            while y != 7:

                                while True:
                                    try:
                                        print(OperBásica[y])
                                        resposta = int(input("Digite a resposta para a operação: "))
                                        respostas.append(resposta)
                                        dado = respostas[y]
                                        dado1 = gabarito2[y]
                                        if dado == dado1:
                                            Pontuação += 1
                                            y += 1
                                        else:
                                            y += 1
                                        break 
                                    except ValueError:
                                        print("apenas números são aceitos")
                                        continue
                            break
                        print()
                        print("Gabarito: ")
                        for k in range(0,7):
                            print(f"[Questão {k + 1}: {gabarito2[k]}]", end=" ")
                            print()
                        print()


                        print("Suas respostas: ")
                        for c in range(0,7):
                            variavelsoma = respostas[c]
                            print(f"[Questão {c + 1}: {variavelsoma}]", end=" ")
                            print()
                        print()

                        print(f"Sua pontuação é {Pontuação}/{len(gabarito2)}")
                        print()

                        d1 = datetime.now()
                        revisãooperaçãobasica = 1
                        collection7.update_one(
                            {'nome':'dia1'},{'$set':{"d1" : d1}})
                        collection7.update_one(
                        {'nome':'dia1'},{'$set':{"variavelrevisao" : revisãooperaçãobasica}})

                    elif materias == 2:

                        collection1 = db.get_collection("potenciaeraciacao")
                        potenciaeraciacao = collection1.find({})

                        for col1 in potenciaeraciacao:
                            print(f" > {col1['Nome']} < ")
                            print(col1['Pot'])
                            print(col1['Rad'])

                        while True:
                            decisão = input("• Gostaria de ver exemplos de radiciação(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                im = Image.open('exemplosdeimagens/definicaoradiciacao.png')
                                im.show()
                                break
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue

                        while True:
                            decisão = input("• Gostaria de ver as propriedades de potenciação(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                im = Image.open('exemplosdeimagens/exemplopotenciacao.png')
                                im.show()
                                break
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue
                        
                        while True:
                            decisão = input("• Gostaria de ver as propriedades de radiciação(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                im = Image.open('exemplosdeimagens/exemploradiciacao.png')
                                im.show()
                                break
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue

                        while True:
                            decisão = input("• Gostaria de ver uma vídeo aula(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                decisãoautomatica = input ("• Gostaria de abrir a vídeo aula automaticamente(s/n)? ")
                                if decisãoautomatica == "s" or decisãoautomatica == "S" or decisãoautomatica == "Sim" or decisãoautomatica == "sim":
                                    url = 'https://www.youtube.com/watch?v=woWpGJ4ca6U'
                                    webbrowser.open_new(url)
                                    break
                                elif decisãoautomatica == "n" or decisãoautomatica == "N" or decisãoautomatica == "Não" or decisãoautomatica == "não":
                                    print("• Link da vídeo aula: https://www.youtube.com/watch?v=woWpGJ4ca6U")
                                    break
                                else:
                                    continue
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue

                        print()
                        input("> Pressione enter para fazer os exercícios ...")
                        print()

                        listaop = ["1","2","3","4"]
                        PotRadlist = ["""• Sabendo que o valor de 5^7 é 78 125, qual o resultado de 5^8?""", """• Em um sítio há 12 árvores. 
                        Cada árvore possui 12 galhos e em cada galho tem 12 maçãs. Quantas maçãs existem no sítio?""", 
                        "• O valor da expressão 20(x^3) + 2(x^2)(y^5), para x = - 4 e y = 2 é: ", "• ( 3^6 * 3^-2 ) / 3^4 é igual a: ", 
                        """• Um adulto humano saudável abriga cerca de 100 bilhões de bactérias, somente em seu trato digestivo. 
                        Esse número de bactérias pode ser escrito como""", """• Para comemorar o aniversário de uma cidade, 
                        a prefeitura organiza quatro dias consecutivos de atrações culturais. A experiência de anos anteriores mostra que, 
                        de um dia para o outro, o número de visitantes no evento é triplicado. 
                        É esperada a presença de 345 visitantes para o primeiro dia do evento.
                        Uma representação possível do número esperado de participantes para o último dia é""", 
                        "• Simplificando a expressão, encontramos:  ((2^65 + 2^67)/10)^(1/4)"]
                        PotRadlistrespota = ["1) 156 250","2) 390 625","3) 234 375","4) 312 500",
                        "1) 144","2) 1224","3) 1564","4) 1728","1) 256","2) -400","3) 400","4) -256",
                        "1) 0","2) 1","3)  3^-3","4) 3^-8", "1) 10^9","2) 10^10","3) 10^11","4) 10^13", "1) 3 * 345","2) 3^3 * 345","3) 34 * 345",
                        "4) 3 * 4 * 345", "1) 2","2) 2^10","3) 2^15","4) 2^16"]
                        gabarito = [2, 4, 4, 2, 3, 2, 4]
                        gabarito2 = [") 390 625", ") 1 728 maçãs", ") -256", ") 1", ") 10^11", ") 3^3 * 345", ") 2^16"]
                        respostas = []

                        n = 0
                        y = 0
                        while True:
                            while y != 7:
                                print(PotRadlist[y])
                                y+= 1
                                l = 0
                                while l != 4: 
                                    print(PotRadlistrespota[n])
                                    n+= 1
                                    l+= 1
                                while True:
                                    resposta = input("• Digite o número da alternativa escolhida: ")
                                    print()
                                    if resposta.isdigit():
                                        resposta = int(resposta)
                                        if 0 < resposta < 5:
                                            respostas.append(resposta)
                                            break
                                        else:
                                            continue
                                    else:
                                        continue
                            break    

                        print("Gabarito: ")
                        for k in range(0,7):
                            print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                            print()
                        print()

                        v = 0
                        print("Suas respostas: ")
                        for c in range(0,7):
                            variavelsoma = respostas[c] - 1
                            print(f"[Questão {c + 1}: {PotRadlistrespota[c + v + variavelsoma]}]", end=" ")
                            v += 3
                            print()
                        print()  

                        print("Sua Pontuação: ")
                        Pontuação = 0
                        for p in range(0,7):
                            if respostas[p] == gabarito[p]:
                                Pontuação += 1
                            else:
                                continue
                        print(f" > Nota: {Pontuação}/{len(gabarito)}")
                        print()

                        d2 = datetime.now()
                        revisãopotenciaerad = 1
                        collection8.update_one(
                            {'nome':'dia2'},{'$set':{"d2" : d2}})
                        collection8.update_one(
                        {'nome':'dia2'},{'$set':{"variavelrevisao" : revisãopotenciaerad}})

                    elif materias == 3:

                        collection2 = db.get_collection("expressaonumerica")
                        expressaonumerica = collection2.find({})

                        for col2 in expressaonumerica:
                            print(f" > {col2['Nome']} < ")
                            print(col2['Def'])
                            print(col2['Ordem'])
                            print(col2['Símbolos'])

                        while True:
                            decisão = input("• Gostaria de ver uma vídeo aula(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                decisãoautomatica = input ("• Gostaria de abrir a vídeo aula automaticamente(s/n)? ")
                                if decisãoautomatica == "s" or decisãoautomatica == "S" or decisãoautomatica == "Sim" or decisãoautomatica == "sim":
                                    url = 'https://www.youtube.com/watch?v=x1bQ854ovbA'
                                    webbrowser.open_new(url)
                                    break
                                elif decisãoautomatica == "n" or decisãoautomatica == "N" or decisãoautomatica == "Não" or decisãoautomatica == "não":
                                    print("• Link da vídeo aula: https://www.youtube.com/watch?v=x1bQ854ovbA")
                                    break
                                else:
                                    continue
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue

                        while True:
                            decisão = input("• Gostaria de ver exemplos(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                im = Image.open('exemplosdeimagens/exemploExpNum.png')
                                im.show()
                                break
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue

                        print()
                        input("> Pressione enter para fazer os exercícios ...")
                        print()

                        listaop = ["1","2","3","4"]
                        ExpNumlist = ["• A respeito da resolução de expressões numéricas, assinale a alternativa correta:", 
                        """• Qual das alternativas a seguir representa um quinto do resultado desta expressão numérica: [(64 – 16·4) + (48·10 – 180)]*5""", 
                        "• Margarida viu no quadro-negro algumas anotações da aula anterior. Qual o valor de X? ", 
                        """• Analisando as expressões: 
                        I. [(+2)(– 3/4) / (–2/3)]

                        II. (+2–3+1) / (–2+2)

                        III. (+4–9) / (–5+3)

                        IV. (2–3+1) / (–7)

                        podemos afirmar que zero é o valor de:""", """• Qual é o valor da expressão numérica abaixo? 
                        [- (-2)^3 – 2^3]""", 
                        "• Calcule o valor da expressão: [2 + 3 * 4] / 7 + 7.",
                        """• Determine o valor da expressão: 
                        -1 + 6 x (7 – 4 ÷ 2)"""]
                        ExpNumlistrespota = ["1) As operações devem ser feitas na ordem em que aparecem.",
                        "2) É necessário calcular primeiro todas as operações no interior dos parênteses na ordem em que elas aparecem.",
                        "3) Não existe ordem para realização dos cálculos em uma expressão numérica.",
                        "4) As adições e subtrações são os últimos cálculos na lista de prioridades das expressões numéricas.", 
                        "1) 270","2) 300","3) 350","4) 410",
                        "1) 9","2) 10","3) 12","4) 15",
                        "1) I, II e IV","2) I e III","3)  somente IV","4) somente II e IV", 
                        "1) 0","2) 1","3) -8","4) -16", 
                        "1) 9","2) 7","3) 12","4) 1", 

                        "1) 7,5","2) 29","3)  8,5","4) 24"]
                        gabarito = [4, 2, 1, 3, 1, 1, 2]
                        gabarito2 = [") As adições e subtrações são os últimos cálculos na lista de prioridades das expressões numéricas.", ") 300", ") 9", 
                        ") somente IV", ") 0", ") 9", ") 29"]
                        respostas = []

                        n = 0
                        y = 0
                        while True:
                            while y != 7:
                                print(ExpNumlist[y])
                                y+= 1
                                l = 0
                                while l != 4: 
                                    print(ExpNumlistrespota[n])
                                    n+= 1
                                    l+= 1
                                while True:
                                    resposta = input("• Digite o número da alternativa escolhida: ")
                                    print()
                                    if resposta.isdigit():
                                        resposta = int(resposta)
                                        if 0 < resposta < 5:
                                            respostas.append(resposta)
                                            break
                                        else:
                                            continue
                                    else:
                                        continue
                            break    

                        print("Gabarito: ")
                        for k in range(0,7):
                            print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                            print()
                        print()

                        v = 0
                        print("Suas respostas: ")
                        for c in range(0,7):
                            variavelsoma = respostas[c] - 1
                            print(f"[Questão {c + 1}: {ExpNumlistrespota[c + v + variavelsoma]}]", end=" ")
                            v+= 3
                            print()
                        print()  

                        print("Sua Pontuação: ")
                        Pontuação = 0
                        for p in range(0,7):
                            if respostas[p] == gabarito[p]:
                                Pontuação += 1
                            else:
                                continue
                        print(f" > Nota: {Pontuação}/{len(gabarito)}")
                        print()
                        d3 = datetime.now()
                        revisãoexpressaonum = 1
                        collection9.update_one(
                            {'nome':'dia3'},{'$set':{"d3" : d3}})
                        collection9.update_one(
                        {'nome':'dia3'},{'$set':{"variavelrevisao" : revisãoexpressaonum}})
                        

                    elif materias == 4:
                        
                        collection3 = db.get_collection("multiplosdivisores")
                        multiplosdivisores = collection3.find({})

                        for col3 in multiplosdivisores:
                            print(f" > {col3['Nome']} < ")
                            print(col3['Múltiplos e Divisores'])
                            print(col3['MMC e MDC'])

                        while True:
                            decisão = input("• Gostaria de ver uma vídeo aula(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                decisãoautomatica = input ("• Gostaria de abrir a vídeo aula automaticamente(s/n)? ")
                                if decisãoautomatica == "s" or decisãoautomatica == "S" or decisãoautomatica == "Sim" or decisãoautomatica == "sim":
                                    url = 'https://www.youtube.com/watch?v=LoiM5d7Kors'
                                    webbrowser.open_new(url)
                                    break
                                elif decisãoautomatica == "n" or decisãoautomatica == "N" or decisãoautomatica == "Não" or decisãoautomatica == "não":
                                    print("• Link da vídeo aula: https://www.youtube.com/watch?v=LoiM5d7Kors")
                                    break
                                else:
                                    continue
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue

                        print()
                        input("> Pressione enter para fazer os exercícios ...")
                        print()

                        listaop = ["1","2","3","4"]
                        MultDivlist = ["• O MDC entre 2³.3.5² e 2².3.7² é igual a: ", "• Quais dos números a seguir estão entre os divisores de 148?", 
                        """•  O conjunto dos números naturais é composto por todos os números inteiros positivos. Das alternativas a seguir, 
                        qual representa um conjunto de múltiplos de um número natural e, ao mesmo tempo, um subconjunto dos números naturais?""", 
                        """•  Um escritório comprou os seguintes itens: 140 marcadores de texto, 120 corretivos e 148 blocos de rascunho e dividiu 
                        esse material em pacotinhos, cada um deles contendo um só tipo de material, porém todos com o mesmo número de itens e 
                        na maior quantidade possível. Sabendo-se que todos os itens foram utilizados, então o número total de pacotinhos feitos foi""", 
                        """• Seja A = 120, B = 160, x = mmc (A,B) e y = mdc (A,B), então o valor de x + y é igual a:""", 
                        """• Utilizando a fatoração em números primos, determine: quais são os dois números consecutivos cujo mmc é 1260?""", 
                        "• O MMC e o MDC de 40 e 64 são respectivamente:"]
                        MultDivlistrespota = ["1) 6","2) 12","3) 60","4) 50", 
                        "1) 4, 7 e 8", "2) 4, 8 e 37","3) 2, 4, 37 e 148","4) 2, 8 e 37",
                        "1) {1, 3, 5, 7, 9, 11, …}","2) {2, 3, 5, 7, 11, 13, 17, …}","3) {…, -4, -2, 0, 2, 4, ...}","4) {2, 4, 8, 10, 12, 14, …}", 
                        "1) 74.", "2)  88", "3) 96", "4) 102.", 
                        "1) 520","2) 460","3)  540","4) 500", 
                        "1) 32 e 33","2) 33 e 34","3) 35 e 36","4) 37 e 38", 
                        "1) 320 e 8","2) 300 e 4","3) 220 e 16","4) 380 e 14"]
                        gabarito = [2, 3, 4, 4, 1, 3, 1]
                        gabarito2 = [") 12", ") 2, 4, 37 e 148", ") {2, 4, 8, 10, 12, 14, …}", 
                        ") 102", ") 520", ") 35 e 36", ") 320 e 8"]
                        respostas = []

                        n = 0
                        y = 0
                        while True:
                            while y != 7:
                                print(MultDivlist[y])
                                y+= 1
                                l = 0
                                while l != 4: 
                                    print(MultDivlistrespota[n])
                                    n+= 1
                                    l+= 1
                                while True:
                                    resposta = input("• Digite o número da alternativa escolhida: ")
                                    print()
                                    if resposta.isdigit():
                                        resposta = int(resposta)
                                        if 0 < resposta < 5:
                                            respostas.append(resposta)
                                            break
                                        else:
                                            continue
                                    else:
                                        continue
                            break    

                        print("Gabarito: ")
                        for k in range(0,7):
                            print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                            print()
                        print()

                        v = 0
                        print("Suas respostas: ")
                        for c in range(0,7):
                            variavelsoma = respostas[c] - 1
                            print(f"[Questão {c + 1}: {MultDivlistrespota[c + v + variavelsoma]}]", end=" ")
                            v += 3
                            print()
                        print()  

                        print("Sua Pontuação: ")
                        Pontuação = 0
                        for p in range(0,7):
                            if respostas[p] == gabarito[p]:
                                Pontuação += 1
                            else:
                                continue
                        print(f" > Nota: {Pontuação}/{len(gabarito)}")
                        print()
                        d4 = datetime.now()
                        revisãomultiplosdivisores = 1
                        collection10.update_one(
                            {'nome':'dia4'},{'$set':{"d4" : d4}})
                        collection10.update_one(
                        {'nome':'dia4'},{'$set':{"variavelrevisao" : revisãomultiplosdivisores}})
                        

                    elif materias == 5:

                        collection4 = db.get_collection("operacaobasicapolinomio")
                        operacaobasicapolinomio = collection4.find({})

                        for col4 in operacaobasicapolinomio:
                            print(f" > {col4['Nome']} < ")
                            print(col4['def'])
                            print(col4['Monômios'])

                            while True:
                                decisão = input("• Gostaria de ver exemplos(s/n)? ")
                                if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                    im = Image.open('exemplosdeimagens/exemplograupolinomio.png')
                                    im.show()
                                    break
                                elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                    break
                                else:
                                    continue
                            print(dado['Adição'])
                            print()
                            while True:
                                decisão = input("• Gostaria de ver exemplos(s/n)? ")
                                if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                    im = Image.open('exemplosdeimagens/exemploadicaopolinomio.png')
                                    im.show()
                                    break
                                elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                    break
                                else:
                                    continue
                            print(dado['Subtração'])
                            print()
                            while True:
                                decisão = input("• Gostaria de ver exemplos(s/n)? ")
                                if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                    im = Image.open('exemplosdeimagens/exemplosubtracaopolinomio.png')
                                    im.show()
                                    break
                                elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                    break
                                else:
                                    continue
                            print(dado['Multiplicação'])
                            print()
                            while True:
                                decisão = input("• Gostaria de ver exemplos(s/n)? ")
                                if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                    im = Image.open('exemplosdeimagens/exemplomultiplicacaopolinomio.png')
                                    im.show()
                                    break
                                elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                    break
                                else:
                                    continue
                            print(dado['Divisão'])
                            print()
                            while True:
                                decisão = input("• Gostaria de ver exemplos(s/n)? ")
                                if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                    im = Image.open('exemplosdeimagens/exemplodivisaopolinomio.png')
                                    im.show()
                                    break
                                elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                    break
                                else:
                                    continue


                        while True:
                            decisão = input("• Gostaria de ver uma vídeo aula(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                decisãoautomatica = input ("• Gostaria de abrir a vídeo aula automaticamente(s/n)? ")
                                if decisãoautomatica == "s" or decisãoautomatica == "S" or decisãoautomatica == "Sim" or decisãoautomatica == "sim":
                                    url = 'https://www.youtube.com/watch?v=RevbMgyMQmg&list=PLEfwqyY2ox84iIVoCHP8JjObsXQtVjh2k'
                                    webbrowser.open_new(url)
                                    break
                                elif decisãoautomatica == "n" or decisãoautomatica == "N" or decisãoautomatica == "Não" or decisãoautomatica == "não":
                                    print("• Link da vídeo aula: https://www.youtube.com/watch?v=RevbMgyMQmg&list=PLEfwqyY2ox84iIVoCHP8JjObsXQtVjh2k")
                                    break
                                else:
                                    continue
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue

                        listaop = ["1","2","3","4"]
                        OpPolilist = ["• Reduzindo-se os termos semelhantes da expressão b(a - b) + (b + a) (b - a) - a(b - a) + (b - a)2, obtém-se:", 
                        "• Dividindo o polinômio x^3 – 4x + 3 por x – 2, encontramos o resto:", 
                        """• O quociente e o resto da divisão do polinômio x² + x – 1 pelo binômio x + 3 são, respectivamente:""", 
                        """• Um laticínio possui dois reservatórios de leite. Cada reservatório é abastecido por uma torneira acoplada a um tanque 
                        resfriado. O volume, em litros, desses reservatórios depende da quantidade inicial de leite no reservatório e do tempo t, 
                        em horas, em que as duas torneiras ficam abertas. Os volumes dos reservatórios são dados pelas funções 
                        V1(t) = 250t^3 – 100t + 3000 e V2(t) = 150t^3 + 69t + 3000.
                        Depois de aberta cada torneira, o volume de leite de um reservatório é igual ao do outro no instante t = 0 e, 
                        também, no tempo t igual a""", 
                        """• Assinalar a nativa que apresenta o resultado do polinômio abaixo: 
                        2x(5x + 7y) + 9x(2y)""", 
                        """• O resto da divisão do polinômio x³ + 3x² – 5x + 1 por (x-2) é""", 
                        """• Dividindo o polinômio p(x) por d(x) = x² + 1, encontram-se o quociente q(x) = x + 3 e o resto r(x) = -7x - 11. 
                        Então a soma de todas as soluções da equação p(x) = 0 é igual a:"""]

                        OpPolilistrespota = [
                        "1) (a – b)^2", "2) (a + b)^2", "3) b^2 – a^2", "4) a^2 – b^2", 
                        "1) x + 3", "2) 3", "3) x – 3", "4) x^2 – 3",
                        "1) x – 3 e 2", "2)  x + 2 e 6", "3) x – 1 e –2", "4) x – 2 e 5", 
                        "1) 10,0 h.", "2) 1,69 h.", "3) 1,3 h.", "4) 16,9 h.", 
                        "1) 10x + 14xy + 18yx", "2) 6x² + 21xy"," 3) 10x² + 32xy", "4) 22x + 9y", 
                        "1) 10", "2) 11", "3) 13", "4) 12", 
                        "1) -3", "2) 4", "3) -1", "4) 16"]
                        gabarito = [1, 2, 4, 3, 3, 2, 1]
                        gabarito2 = [") (a – b)^2", ") 3", ") x – 2 e 5", 
                        ") 1,3 h.", ") 10x² + 32xy", ") 11", ") -3"]
                        respostas = []

                        n = 0
                        y = 0
                        while True:
                            while y != 7:
                                print(OpPolilist[y])
                                y+= 1
                                l = 0
                                while l != 4: 
                                    print(OpPolilistrespota[n])
                                    n+= 1
                                    l+= 1
                                while True:
                                    resposta = input("• Digite o número da alternativa escolhida: ")
                                    print()
                                    if resposta.isdigit():
                                        resposta = int(resposta)
                                        if 0 < resposta < 5:
                                            respostas.append(resposta)
                                            break
                                        else:
                                            continue
                                    else:
                                        continue
                            break    

                        print("Gabarito: ")
                        for k in range(0,7):
                            print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                            print()
                        print()

                        v = 0
                        print("Suas respostas: ")
                        for c in range(0,7):
                            variavelsoma = respostas[c] - 1
                            print(f"[Questão {c + 1}: {OpPolilistrespota[c + v + variavelsoma]}]", end=" ")
                            v += 3
                            print()
                        print()  

                        print("Sua Pontuação: ")
                        Pontuação = 0
                        for p in range(0,7):
                            if respostas[p] == gabarito[p]:
                                Pontuação += 1
                            else:
                                continue
                        print(f" > Nota: {Pontuação}/{len(gabarito)}")
                        print()
                        d5 = datetime.now()
                        revisãooppolinomios = 1

                        collection11.update_one(
                            {'nome':'dia5'},{'$set':{"d5" : d5}})
                        collection11.update_one(
                        {'nome':'dia5'},{'$set':{"variavelrevisao" : revisãooppolinomios}})
                        

                    elif materias == 6:

                        collection5 = db.get_collection("fracoesdecimaisedizimas")
                        fracoesdecimaisedizimas = collection5.find({})

                        for col5 in fracoesdecimaisedizimas:
                            print(f" > {col5['Nome']} < ")
                            print(col5['Frações'])
                            print(col5['Decimais'])
                            print(col5['Dízimas'])

                        while True:
                            decisão = input("• Gostaria de ver Dízimas simples(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                im = Image.open('exemplosdeimagens/exemplodizimasimples.png')
                                im.show()
                                break
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue

                        while True:
                            decisão = input("• Gostaria de ver Dízimas compostas(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                im = Image.open('exemplosdeimagens/exemplodizimascomposta.png')
                                im.show()
                                break
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue

                        while True:
                            decisão = input("• Gostaria de ver uma vídeo aula(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                decisãoautomatica = input ("• Gostaria de abrir a vídeo aula automaticamente(s/n)? ")
                                if decisãoautomatica == "s" or decisãoautomatica == "S" or decisãoautomatica == "Sim" or decisãoautomatica == "sim":
                                    url = 'https://www.youtube.com/watch?v=iaXXPRyFBB8'
                                    webbrowser.open_new(url)
                                    break
                                elif decisãoautomatica == "n" or decisãoautomatica == "N" or decisãoautomatica == "Não" or decisãoautomatica == "não":
                                    print("• Link da vídeo aula: https://www.youtube.com/watch?v=iaXXPRyFBB8")
                                    break
                                else:
                                    continue
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue
                        
                        listaop = ["1","2","3","4"]
                        FracDeciDilist = [
                        """• Em uma disputa entre carros de corrida um competidor estava a 2/7 de terminar a prova quando sofreu um acidente e precisou 
                        abandoná-la. Sabendo que a competição foi realizada com 56 voltas no autódromo, em que volta o competidor foi retirado da 
                        pista?""", 
                        """• Duas empreiteiras farão conjuntamente a pavimentação de uma estrada, cada uma trabalhando a partir de uma das extremidades. 
                        Se uma delas pavimentar 2/5 da estrada e a outra os 81 km restantes, a extensão dessa estrada é de:""", 
                        """•  Uma peça de tecido, após a lavagem, perdeu 1/10 de seu comprimento e ficou medindo 36 metros. Nessas condições, o 
                        comprimento, em metros, da peça antes da lavagem era igual a:""", 
                        """• Qual é o resultado da expressão numérica abaixo?
                                        41,32 + 56,4 – 81,932 + 5""", 
                        """• Qual é a área de um retângulo cuja largura mede 23,32 m e o comprimento mede 52,25 m?""", 
                        """• A soma 1,3333... + 0,16666... é igual a:""", 
                        """• Um estudante se cadastrou numa rede social na internet que exibe o índice de popularidade do usuário. Esse índice é a 
                        razão entre o número de admiradores do usuário e o número de pessoas que visitam seu perfil na rede. Ao acessar seu perfil 
                        hoje, o estudante descobriu que seu índice de popularidade é 0,3121212...
                        O índice revela que as quantidades relativas de admiradores do estudante e pessoas que visitam seu perfil são"""]

                        FracDeciDilistrespota = [
                        "1) 16ª volta", "2) 40ª volta", "3) 32ª volta", "4) 50ª volta", 
                        "1) 125 km", "2) 135 km", "3) 142 km", "4) 145 km",
                        "1) 39,6 metros", "2) 42,8 metros", "3) 41,3 metros", "4) 40 metros", 
                        "1) 102,72", "2) 20,8", "3) 20,788", "4) 20", 
                        "1)  1218,47 m^2", "2) 1045,0 m^2"," 3) 1219,01 m^2", "4) 1567,5 m^2", 
                        "1) 5/2", "2) 4/3", "3) 3/2", "4) 1/2", 
                        "1) 103 em cada 330.", "2)  1 039 em cada 3 330.", "3) 104 em cada 333.", "4) 104 em cada 3 333."]
                        gabarito = [2, 2, 4, 3, 1, 3, 1]
                        gabarito2 = [") 40ª volta", ") 135 km", ") 40 metros", 
                        ") 20,788", ")  1218,47 m^2", ") 3/2", ") 103 em cada 330."]
                        respostas = []

                        n = 0
                        y = 0
                        while True:
                            while y != 7:
                                print(FracDeciDilist[y])
                                y+= 1
                                l = 0
                                while l != 4: 
                                    print(FracDeciDilistrespota[n])
                                    n+= 1
                                    l+= 1
                                while True:
                                    resposta = input("• Digite o número da alternativa escolhida: ")
                                    print()
                                    if resposta.isdigit():
                                        resposta = int(resposta)
                                        if 0 < resposta < 5:
                                            respostas.append(resposta)
                                            break
                                        else:
                                            continue
                                    else:
                                        continue
                            break    

                        print("Gabarito: ")
                        for k in range(0,7):
                            print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                            print()
                        print()

                        v = 0
                        print("Suas respostas: ")
                        for c in range(0,7):
                            variavelsoma = respostas[c] - 1
                            print(f"[Questão {c + 1}: {FracDeciDilistrespota[c + v + variavelsoma]}]", end=" ")
                            v+= 3
                            print()
                        print()  

                        print("Sua Pontuação: ")
                        Pontuação = 0
                        for p in range(0,7):
                            if respostas[p] == gabarito[p]:
                                Pontuação += 1
                            else:
                                continue
                        print(f" > Nota: {Pontuação}/{len(gabarito)}")
                        print()

                        d6 = datetime.now()
                        revisãofracoes = 1
                        
                        collection12.update_one(
                            {'nome':'dia6'},{'$set':{"d6" : d6}})
                        collection12.update_one(
                        {'nome':'dia6'},{'$set':{"variavelrevisao" : revisãofracoes}})

                    elif materias == 7:

                        collection6 = db.get_collection("notacaocientifica")
                        notacaocientifica = collection6.find({})

                        for col6 in notacaocientifica:
                            print(f" > {col6['nome']} < ")
                            print(col6['def'])
                            
                        while True:
                            decisão = input("• Gostaria de ver exemplos(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                im = Image.open('exemplosdeimagens/exemplonotcien.png')
                                im.show()
                                break
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue

                        while True:
                            decisão = input("• Gostaria de ver uma vídeo aula(s/n)? ")
                            if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                                decisãoautomatica = input ("• Gostaria de abrir a vídeo aula automaticamente(s/n)? ")
                                if decisãoautomatica == "s" or decisãoautomatica == "S" or decisãoautomatica == "Sim" or decisãoautomatica == "sim":
                                    url = 'https://www.youtube.com/watch?v=PebTiUSshPQ'
                                    webbrowser.open_new(url)
                                    break
                                elif decisãoautomatica == "n" or decisãoautomatica == "N" or decisãoautomatica == "Não" or decisãoautomatica == "não":
                                    print("• Link da vídeo aula: https://www.youtube.com/watch?v=PebTiUSshPQ")
                                    break
                                else:
                                    continue
                            elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                                break
                            else:
                                continue

                        print()
                        input("> Pressione enter para fazer os exercícios ...")
                        print()

                        listaop = ["a","b","c","d"]
                        notcientificalist = ["• Considere o número 0,00000000000002, converta-o em notação científica.",
                        "• O número 349000 em notação científica corresponde a:","• Escreva o número 0,0004 em notação científica.",
                        "• Como escrevemos 5 x 10³ na forma decimal?"]
                        notcientificalistrespota = ["1)2x10^-14","2)20x10^-11","3)3x10^10","4)4x10^-12",
                        "1)3x10^-14","2)3,49x10^5","3)349x10^6","4)34,9x10^-10","1)4x10^-4","2)40x10^-5","3)0,4x10^10","4)4x10^-12",
                        "1)0,05","2)0,000005","3)0,005","4)0,5"]
                        gabarito = [1,2,1,3]
                        gabarito2 = [")2x10^-14",")3,49x10^5",")4x10^-4",")0,005"]
                        respostas = []

                        n = 0
                        y = 0
                        while True:
                            while y != 4:
                                print(notcientificalist[y])
                                y+= 1
                                l = 0
                                while l != 4: 
                                    print(notcientificalistrespota[n])
                                    n+= 1
                                    l+= 1
                                while True:
                                    resposta = input("• Digite o número da alternativa escolhida: ")
                                    print()
                                    if resposta.isdigit():
                                        resposta = int(resposta)
                                        if 0 < resposta < 5:
                                            respostas.append(resposta)
                                            break
                                        else:
                                            continue
                                    else:
                                        continue
                            break    

                        print("Gabarito: ")
                        for k in range(0,4):
                            print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                            print()
                        print()

                        v = 0
                        print("Suas respostas: ")
                        for c in range(0,4):
                            variavelsoma = respostas[c] - 1
                            print(f"[Questão {c + 1}: {notcientificalistrespota[c + v + variavelsoma]}]", end=" ")
                            v+= 3
                            print()
                        print()  

                        print("Sua Pontuação: ")
                        Pontuação = 0
                        for p in range(0,4):
                            if respostas[p] == gabarito[p]:
                                Pontuação += 1
                            else:
                                continue
                        print(f" > Nota: {Pontuação}/{len(gabarito)}")
                        print()
                        d7 = datetime.now()
                        revisãonotcient = 1
                        
                        collection13.update_one(
                            {'nome':'dia7'},{'$set':{"d7" : d7}})
                        collection13.update_one(
                        {'nome':'dia7'},{'$set':{"variavelrevisao" : revisãonotcient}})

                    elif materias == 8:
                        break
    
                else:
                    print("• Opção inválida, Digite uma opção existente")
                    continue

        elif Menu == 3:
            # Inciar contagem de revisão 24h
            datual = datetime.now()

            if revisãooperaçãobasica == 1:
                if datual - d1 == 1:
                    print()
                    input("> Pressione enter para fazer a revisão de Operações básicas...")
                    print()
                    listaop = ["1","2","3","4"]
                    OpBasiclist = [
                    """• Calcule: 765 + 456:""", 
                    """• Qual o resultado da operação: 56 x 9:""", 
                    """• Calcule: 895 - 123:""", 
                    """• Qual o resultado da soma: 234 + 876:""", 
                    ]

                    OpBasiclistrespota = [
                    "1) 1.700", "2) 1.221", "3) 1.321", "4) 1.121", 
                    "1) 504", "2) 560", "3) 469", "4) 392",
                    "1) 762", "2) 782", "3) 772", "4) 789", 
                    "1) 1.110", "2) 1.000", "3) 1.010", "4) 1.100", 
                    ]
                    gabarito = [2, 1, 3, 1]
                    gabarito2 = [") 1.221", ") 504", ") 772", ") 1.110"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(OpBasiclist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(OpBasiclistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {OpBasiclistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                    
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 24 Horas")
                

            elif revisãopotenciaerad == 1:
                if datual - d2 == 1:
                    print()
                    input("> Pressione enter para fazer a revisão de Potenciação e radiciação...")
                    print()

                    listaop = ["1","2","3","4"]
                    PotRadlist = [
                    """• Calcule: 3³ x 2²:""", 
                    """• Qual o resultado da operação: (2²)²:""", 
                    """• Calcule: (2 x 3)²:""", 
                    """• Calcule: (2²+4)²:""", 
                    ]

                    PotRadlistrespota = [
                    "1) 100", "2) 108", "3) 110", "4) 106", 
                    "1) 8", "2) 2", "3) 4", "4) 16",
                    "1) 6", "2) 12", "3) 36", "4) 24", 
                    "1) 64", "2) 32", "3) 16", "4) 24", 
                    ]
                    gabarito = [2, 4, 3, 1]
                    gabarito2 = [") 108", ") 16", ") 36", ") 64"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(PotRadlist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(PotRadlistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {PotRadlistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()

                else:
                    print("• Ainda não passou o tempo necessário para a revisão 24 Horas")
                

            elif revisãoexpressaonum == 1:
                if datual - d3 == 1:
                    print()
                    input("> Pressione enter para fazer a revisão de Expressões numéricas...")
                    print()
                    listaop = ["1","2","3","4"]
                    ExpNumlist = [
                    """• Analise a solução da expressão algébrica abaixo e assinale a alternativa correta:

                    {(10·10 + 4·11):12 – [(20 + 19·10):39 + 15]} + 50 =

                    {(100 + 44):12 – [(39·10):39 + 15]} + 50 =

                    {144:12 – [390:39 + 15]} + 50 =

                    {12 – [10 + 15]} + 50 =

                    {12 – 25} + 50 =

                    – 13 + 50 =

                    37""", 
                    """• Calcule: (34 x 7) - (23 x 2)""", 
                    """• Calcule: (37 x 3) + (22 x 3)""", 
                    """• Calcule: [(71 x 4) - (18 x 6)] x5""", 
                    ]

                    ExpNumlistrespota = [
                    "1) A resolução está correta, nenhum erro foi cometido.", "2) A resolução está correta, mas por coincidência, pois alguns erros foram cometidos.", "3) A resolução está incorreta, o verdadeiro resultado é 50.", "4) A resolução está incorreta, pois foi feita uma soma em vez de dar prioridade a uma multiplicação.", 
                    "1) 192", "2) 205 ", "3) 202", "4) 190",
                    "1) 192", "2) 177 ", "3) 209", "4) 170", 
                    "1) 195", "2) 176 ", "3) 880", "4) 876", 
                    ]
                    gabarito = [4, 1, 2, 3]
                    gabarito2 = [") A resolução está incorreta, pois foi feita uma soma em vez de dar prioridade a uma multiplicação.", 
                    ") 192", ") 177", ") 880"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(ExpNumlist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(ExpNumlistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {ExpNumlistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 24 Horas")
            

            elif revisãomultiplosdivisores == 1:
                if datual - d4 == 1:
                    print()
                    input("> Pressione enter para fazer a revisão de Múltiplos, divisores, MDC e MMC...")
                    print()
                    listaop = ["1","2","3","4"]
                    MultDivlist = [
                    """• Quais os divisores de 18?""", 
                    """• Quais os divisores comuns de 12 e 18?""", 
                    """• Qual o maior divisor comum entre 12 e 18?""", 
                    """• Em uma confecção, há rolos de malha com medidas de 120, 180 e 240 centímetros. Será preciso cortar o tecido em pedaços iguais, maiores possíveis e, não sobrar nada. Qual será o comprimento máximo de cada tira de malha?""", 
                    ]

                    MultDivlistrespota = [
                    "1) 1, 9, 18", "2) 2, 3, 4, 6 e 12.", "3) 2, 3, 6, 9, 18.", "4) 2, 3 e 6", 
                    "1) 1 e 2", "2) 9 e 12", "3) 1, 2, 3, 4, 9", "4) 2, 3 e 6",
                    "1) 4", "2) 9", "3) 12", "4) 6", 
                    "1) 60", "2) 40", "3) 20", "4) 80", 
                    ]
                    gabarito = [3, 4, 4, 1]
                    gabarito2 = [") 2, 3, 6, 9, 18.", ") 2, 3 e 6", ") 6", ") 60"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(MultDivlist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(MultDivlistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {MultDivlistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 24 Horas")
                

            elif revisãooppolinomios == 1:
                if datual - d5 == 1:                       
                    print()
                    input("> Pressione enter para fazer a revisão de Operações básicas com polinômios...")
                    print()
                    listaop = ["1","2","3","4"]
                    OpPolilist = [
                    """• Efetue a operação: (–2x² + 5x – 2) + (–3x³ + 2x – 1)""", 
                    """• Efutue a operação: (–2x² + 5x – 2) – (–3x³ + 2x – 1)""", 
                    """• Efetue a operação: (x – 1) * (x2 + 2x - 6)""", 
                    """• Efetue a operação: (2 - x) * (x + 1)""", 
                    ]

                    OpPolilistrespota = [
                    "1) – 3x³ – 2x² + 7x – 3", "2) –2x² + 5x – 2", "3) –3x³ + 2x – 1", "4) 3x³ – 2x² + 7x", 
                    "1) – 3x³ – 2x² + 7x – 3", "2) 3x³ – 2x² + 3x – 1", "3) 3x³ + 2x – 1", "4) 3x³ + 2x² + 7",
                    "1) x³ + x² – 8x + 6", "2) 3x³ + 2x² + 7", "3) -x³ - x² + 8x - 6", "4) -3x³ - 2x² - 7", 
                    "1)  x² - x + 2", "2)  - x² + x + 2", "3) -x² - x - 2", "4)  x² + x - 2", 
                    ]
                    gabarito = [1, 2, 1, 2]
                    gabarito2 = [")  – 3x³ – 2x² + 7x – 3", ") 3x³ – 2x² + 3x – 1", ") x³ + x² – 8x + 6", ") - x² + x + 2"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(OpPolilist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(OpPolilistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {OpPolilistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 24 Horas")
                

            elif revisãofracoes == 1:
                if datual - d6 == 1:
                    print()
                    input("> Pressione enter para fazer a revisão de Frações, decimais e dízimas...")
                    print()
                    listaop = ["1","2","3","4"]
                    FracDeciDilist = [
                    """• Diga o valor da multiplicação: 27/4 x 4/9:""", 
                    """• Calcule: 1.234 + (875/5):""", 
                    """• Calcule: 7/10 +7/5""", 
                    """• Dos números a seguir, assinale aquele que corresponde a uma dízima periódica composta.""", 
                    ]

                    FracDeciDilistrespota = [
                    "1) 3", "2) 5/2", "3) 2", "4) 27", 
                    "1) 421,8", "2) 2.109", "3) 1.409", "4) 1.737",
                    "1) 7", "2) 1,4", "3) 0,7", "4) 2,1", 
                    "1) 3,14159284…", "2) 2,21111", "3) 0,3333…", "4) 1,21111…", 
                    ]
                    gabarito = [1, 3, 4, 4]
                    gabarito2 = [") 3", ") 1.409", ") 2,1", ") 1,21111…"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(FracDeciDilist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(FracDeciDilistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {FracDeciDilistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 24 Horas")
                

            elif revisãonotcient == 1:
                if datual - d7 == 1:
                    print()
                    input("> Pressione enter para fazer a revisão de Notação científica...")
                    print()
                    listaop = ["1","2","3","4"]
                    NotCientlist = [
                    """• A distância entre o planeta Terra e o Sol é de 149.600.000 km. Qual a distância entre a Terra e Sol em Notação científica?""", 
                    """• A idade aproximada do planeta Terra é de 4.543.000.000 anos. Qual a idade aproximada da Terra em Notação científica?""", 
                    """• O diâmetro de um átomo é da ordem de 1 nanômetro, ou seja, 0,0000000001. Qual o diâmetro do raio em Notação científica?""", 
                    """• Resolva utilizando notação científica: 0,00003 * 0,0027:""", 
                    ]

                    NotCientlistrespota = [
                    "1) 1,496 * 10^8", "2) 14,96 * 10^7", "3) 1,496 * 10^7", "4) 1,496 * 10^9", 
                    "1) 4,543 * 10^9", "2) 45,43 * 10^8", "3) 4,543 * 10^10", "4) 4,543 * 10^7",
                    "1) 1 * 10^-9", "2) 1 * 10^-10", "3) 1 * 10^-11", "4) 1 * 10^10", 
                    "1) 0,0000081", "2) 0,00000081", "3) 0,0000000081", "4) 0,000000081", 
                    ]
                    gabarito = [1, 1, 2, 4]
                    gabarito2 = [") 1,496 * 10^8", ") 4,543 * 10^9", ") 1 * 10^-10", ") 0,000000081"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(NotCientlist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(NotCientlistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {NotCientlistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 24 Horas")

            else:
                print("• Faça alguma aula para liberar a revisão")
                
        elif Menu == 4:
            # Contagem revisão 7 Dias
            datual = datetime.now()

            if revisãooperaçãobasica == 1:
                if datual - d1 == 7:
                    print()
                    input("> Pressione enter para fazer a revisão de Operações básicas...")
                    print()
                    OperBásica = ["• 5 + 7", "• −5 + 7", "• −2 + 4 − 5 + 6 − 8 + 13", 
                    "• 18 ÷ 9", "• (9) * (−7)", "• (−3) * (−5)", "• −20 ÷ (5)"]
                    gabarito2 = [12, 2, 8, 2, -63 , 15, -4]
                    respostas = []
                    Pontuação = 0

                    n = 0
                    y = 0
                    while True:
                        while y != 7:

                            while True:
                                try:
                                    print(OperBásica[y])
                                    resposta = int(input("Digite a resposta para a operação: "))
                                    respostas.append(resposta)
                                    dado = respostas[y]
                                    dado1 = gabarito2[y]
                                    if dado == dado1:
                                        Pontuação += 1
                                        y += 1
                                    else:
                                        y += 1
                                    break 
                                except ValueError:
                                    print("apenas números são aceitos")
                                    continue
                        break
                    print()
                    print("Gabarito: ")
                    for k in range(0,7):
                        print(f"[Questão {k + 1}: {gabarito2[k]}]", end=" ")
                        print()
                    print()


                    print("Suas respostas: ")
                    for c in range(0,7):
                        variavelsoma = respostas[c]
                        print(f"[Questão {c + 1}: {variavelsoma}]", end=" ")
                        print()
                    print()

                    print(f"Sua pontuação é {Pontuação}/{len(gabarito2)}")
                    print()

                else:
                    print("• Ainda não passou o tempo necessário para a revisão 7 dias")
                

            elif revisãopotenciaerad == 1:
                if datual - d2 == 7:
                    print()
                    input("> Pressione enter para fazer a revisão de Potenciação e radiciação...")
                    print()
                    listaop = ["1","2","3","4"]
                    PotRadlist = ["""• Sabendo que o valor de 5^7 é 78 125, qual o resultado de 5^8?""", """• Em um sítio há 12 árvores. 
                    Cada árvore possui 12 galhos e em cada galho tem 12 maçãs. Quantas maçãs existem no sítio?""", 
                    "• O valor da expressão 20(x^3) + 2(x^2)(y^5), para x = - 4 e y = 2 é: ", "• ( 3^6 * 3^-2 ) / 3^4 é igual a: ", 
                    """• Um adulto humano saudável abriga cerca de 100 bilhões de bactérias, somente em seu trato digestivo. 
                    Esse número de bactérias pode ser escrito como""", """• Para comemorar o aniversário de uma cidade, 
                    a prefeitura organiza quatro dias consecutivos de atrações culturais. A experiência de anos anteriores mostra que, 
                    de um dia para o outro, o número de visitantes no evento é triplicado. 
                    É esperada a presença de 345 visitantes para o primeiro dia do evento.
                    Uma representação possível do número esperado de participantes para o último dia é""", 
                    "• Simplificando a expressão, encontramos:  ((2^65 + 2^67)/10)^(1/4)"]
                    PotRadlistrespota = ["1) 156 250","2) 390 625","3) 234 375","4) 312 500",
                    "1) 144","2) 1224","3) 1564","4) 1728","1) 256","2) -400","3) 400","4) -256",
                    "1) 0","2) 1","3)  3^-3","4) 3^-8", "1) 10^9","2) 10^10","3) 10^11","4) 10^13", "1) 3 * 345","2) 3^3 * 345","3) 34 * 345",
                    "4) 3 * 4 * 345", "1) 2","2) 2^10","3) 2^15","4) 2^16"]
                    gabarito = [2, 4, 4, 2, 3, 2, 4]
                    gabarito2 = [") 390 625", ") 1 728 maçãs", ") -256", ") 1", ") 10^11", ") 3^3 * 345", ") 2^16"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 7:
                            print(PotRadlist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(PotRadlistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,7):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,7):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {PotRadlistrespota[c + v + variavelsoma]}]", end=" ")
                        v += 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,7):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 7 dias")
                

            elif revisãoexpressaonum == 1:
                if datual - d3 == 7:
                    print()
                    input("> Pressione enter para fazer a revisão de Expressões numéricas...")
                    print()
                    listaop = ["1","2","3","4"]
                    ExpNumlist = ["• A respeito da resolução de expressões numéricas, assinale a alternativa correta:", 
                    """• Qual das alternativas a seguir representa um quinto do resultado desta expressão numérica: [(64 – 16·4) + (48·10 – 180)]*5""", 
                    "• Margarida viu no quadro-negro algumas anotações da aula anterior. Qual o valor de X? ", 
                    """• Analisando as expressões: 
                    I. [(+2)(– 3/4) / (–2/3)]

                    II. (+2–3+1) / (–2+2)

                    III. (+4–9) / (–5+3)

                    IV. (2–3+1) / (–7)

                    podemos afirmar que zero é o valor de:""", """• Qual é o valor da expressão numérica abaixo? 
                    [- (-2)^3 – 2^3]""", 
                    "• Calcule o valor da expressão: [2 + 3 * 4] / 7 + 7.",
                    """• Determine o valor da expressão: 
                    -1 + 6 x (7 – 4 ÷ 2)"""]
                    ExpNumlistrespota = ["1) As operações devem ser feitas na ordem em que aparecem.",
                    "2) É necessário calcular primeiro todas as operações no interior dos parênteses na ordem em que elas aparecem.",
                    "3) Não existe ordem para realização dos cálculos em uma expressão numérica.",
                    "4) As adições e subtrações são os últimos cálculos na lista de prioridades das expressões numéricas.", 
                    "1) 270","2) 300","3) 350","4) 410",
                    "1) 9","2) 10","3) 12","4) 15",
                    "1) I, II e IV","2) I e III","3)  somente IV","4) somente II e IV", 
                    "1) 0","2) 1","3) -8","4) -16", 
                    "1) 9","2) 7","3) 12","4) 1", 

                    "1) 7,5","2) 29","3)  8,5","4) 24"]
                    gabarito = [4, 2, 1, 3, 1, 1, 2]
                    gabarito2 = [") As adições e subtrações são os últimos cálculos na lista de prioridades das expressões numéricas.", ") 300", ") 9", 
                    ") somente IV", ") 0", ") 9", ") 29"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 7:
                            print(ExpNumlist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(ExpNumlistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,7):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,7):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {ExpNumlistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,7):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 7 dias")
                

            elif revisãomultiplosdivisores == 1:
                if datual - d4 == 7:
                    print()
                    input("> Pressione enter para fazer a revisão de Múltiplos, divisores, MDC e MMC...")
                    print()
                    listaop = ["1","2","3","4"]
                    MultDivlist = ["• O MDC entre 2³.3.5² e 2².3.7² é igual a: ", "• Quais dos números a seguir estão entre os divisores de 148?", 
                    """•  O conjunto dos números naturais é composto por todos os números inteiros positivos. Das alternativas a seguir, 
                    qual representa um conjunto de múltiplos de um número natural e, ao mesmo tempo, um subconjunto dos números naturais?""", 
                    """•  Um escritório comprou os seguintes itens: 140 marcadores de texto, 120 corretivos e 148 blocos de rascunho e dividiu 
                    esse material em pacotinhos, cada um deles contendo um só tipo de material, porém todos com o mesmo número de itens e 
                    na maior quantidade possível. Sabendo-se que todos os itens foram utilizados, então o número total de pacotinhos feitos foi""", 
                    """• Seja A = 120, B = 160, x = mmc (A,B) e y = mdc (A,B), então o valor de x + y é igual a:""", 
                    """• Utilizando a fatoração em números primos, determine: quais são os dois números consecutivos cujo mmc é 1260?""", 
                    "• O MMC e o MDC de 40 e 64 são respectivamente:"]
                    MultDivlistrespota = ["1) 6","2) 12","3) 60","4) 50", 
                    "1) 4, 7 e 8", "2) 4, 8 e 37","3) 2, 4, 37 e 148","4) 2, 8 e 37",
                    "1) {1, 3, 5, 7, 9, 11, …}","2) {2, 3, 5, 7, 11, 13, 17, …}","3) {…, -4, -2, 0, 2, 4, ...}","4) {2, 4, 8, 10, 12, 14, …}", 
                    "1) 74.", "2)  88", "3) 96", "4) 102.", 
                    "1) 520","2) 460","3)  540","4) 500", 
                    "1) 32 e 33","2) 33 e 34","3) 35 e 36","4) 37 e 38", 
                    "1) 320 e 8","2) 300 e 4","3) 220 e 16","4) 380 e 14"]
                    gabarito = [2, 3, 4, 4, 1, 3, 1]
                    gabarito2 = [") 12", ") 2, 4, 37 e 148", ") {2, 4, 8, 10, 12, 14, …}", 
                    ") 102", ") 520", ") 35 e 36", ") 320 e 8"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 7:
                            print(MultDivlist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(MultDivlistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,7):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,7):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {MultDivlistrespota[c + v + variavelsoma]}]", end=" ")
                        v += 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,7):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 7 dias")
                

            elif revisãooppolinomios == 1:
                if datual - d5 == 7:
                    print()
                    input("> Pressione enter para fazer a revisão de Operações básicas com polinõmios...")
                    print()
                    listaop = ["1","2","3","4"]
                    OpPolilist = ["• Reduzindo-se os termos semelhantes da expressão b(a - b) + (b + a) (b - a) - a(b - a) + (b - a)2, obtém-se:", 
                    "• Dividindo o polinômio x^3 – 4x + 3 por x – 2, encontramos o resto:", 
                    """• O quociente e o resto da divisão do polinômio x² + x – 1 pelo binômio x + 3 são, respectivamente:""", 
                    """• Um laticínio possui dois reservatórios de leite. Cada reservatório é abastecido por uma torneira acoplada a um tanque 
                    resfriado. O volume, em litros, desses reservatórios depende da quantidade inicial de leite no reservatório e do tempo t, 
                    em horas, em que as duas torneiras ficam abertas. Os volumes dos reservatórios são dados pelas funções 
                    V1(t) = 250t^3 – 100t + 3000 e V2(t) = 150t^3 + 69t + 3000.
                    Depois de aberta cada torneira, o volume de leite de um reservatório é igual ao do outro no instante t = 0 e, 
                    também, no tempo t igual a""", 
                    """• Assinalar a nativa que apresenta o resultado do polinômio abaixo: 
                    2x(5x + 7y) + 9x(2y)""", 
                    """• O resto da divisão do polinômio x³ + 3x² – 5x + 1 por (x-2) é""", 
                    """• Dividindo o polinômio p(x) por d(x) = x² + 1, encontram-se o quociente q(x) = x + 3 e o resto r(x) = -7x - 11. 
                    Então a soma de todas as soluções da equação p(x) = 0 é igual a:"""]

                    OpPolilistrespota = [
                    "1) (a – b)^2", "2) (a + b)^2", "3) b^2 – a^2", "4) a^2 – b^2", 
                    "1) x + 3", "2) 3", "3) x – 3", "4) x^2 – 3",
                    "1) x – 3 e 2", "2)  x + 2 e 6", "3) x – 1 e –2", "4) x – 2 e 5", 
                    "1) 10,0 h.", "2) 1,69 h.", "3) 1,3 h.", "4) 16,9 h.", 
                    "1) 10x + 14xy + 18yx", "2) 6x² + 21xy"," 3) 10x² + 32xy", "4) 22x + 9y", 
                    "1) 10", "2) 11", "3) 13", "4) 12", 
                    "1) -3", "2) 4", "3) -1", "4) 16"]
                    gabarito = [1, 2, 4, 3, 3, 2, 1]
                    gabarito2 = [") (a – b)^2", ") 3", ") x – 2 e 5", 
                    ") 1,3 h.", ") 10x² + 32xy", ") 11", ") -3"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 7:
                            print(OpPolilist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(OpPolilistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,7):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,7):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {OpPolilistrespota[c + v + variavelsoma]}]", end=" ")
                        v += 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,7):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 7 dias")
            

            elif revisãofracoes == 1:
                if datual - d6 == 7:
                    print()
                    input("> Pressione enter para fazer a revisão de Frações, decimais e dízimas...")
                    print()
                    listaop = ["1","2","3","4"]
                    FracDeciDilist = [
                    """• Em uma disputa entre carros de corrida um competidor estava a 2/7 de terminar a prova quando sofreu um acidente e precisou 
                    abandoná-la. Sabendo que a competição foi realizada com 56 voltas no autódromo, em que volta o competidor foi retirado da 
                    pista?""", 
                    """• Duas empreiteiras farão conjuntamente a pavimentação de uma estrada, cada uma trabalhando a partir de uma das extremidades. 
                    Se uma delas pavimentar 2/5 da estrada e a outra os 81 km restantes, a extensão dessa estrada é de:""", 
                    """•  Uma peça de tecido, após a lavagem, perdeu 1/10 de seu comprimento e ficou medindo 36 metros. Nessas condições, o 
                    comprimento, em metros, da peça antes da lavagem era igual a:""", 
                    """• Qual é o resultado da expressão numérica abaixo?
                                    41,32 + 56,4 – 81,932 + 5""", 
                    """• Qual é a área de um retângulo cuja largura mede 23,32 m e o comprimento mede 52,25 m?""", 
                    """• A soma 1,3333... + 0,16666... é igual a:""", 
                    """• Um estudante se cadastrou numa rede social na internet que exibe o índice de popularidade do usuário. Esse índice é a 
                    razão entre o número de admiradores do usuário e o número de pessoas que visitam seu perfil na rede. Ao acessar seu perfil 
                    hoje, o estudante descobriu que seu índice de popularidade é 0,3121212...
                    O índice revela que as quantidades relativas de admiradores do estudante e pessoas que visitam seu perfil são"""]

                    FracDeciDilistrespota = [
                    "1) 16ª volta", "2) 40ª volta", "3) 32ª volta", "4) 50ª volta", 
                    "1) 125 km", "2) 135 km", "3) 142 km", "4) 145 km",
                    "1) 39,6 metros", "2) 42,8 metros", "3) 41,3 metros", "4) 40 metros", 
                    "1) 102,72", "2) 20,8", "3) 20,788", "4) 20", 
                    "1)  1218,47 m^2", "2) 1045,0 m^2"," 3) 1219,01 m^2", "4) 1567,5 m^2", 
                    "1) 5/2", "2) 4/3", "3) 3/2", "4) 1/2", 
                    "1) 103 em cada 330.", "2)  1 039 em cada 3 330.", "3) 104 em cada 333.", "4) 104 em cada 3 333."]
                    gabarito = [2, 2, 4, 3, 1, 3, 1]
                    gabarito2 = [") 40ª volta", ") 135 km", ") 40 metros", 
                    ") 20,788", ")  1218,47 m^2", ") 3/2", ") 103 em cada 330."]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 7:
                            print(FracDeciDilist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(FracDeciDilistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,7):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,7):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {FracDeciDilistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,7):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 7 dias")
                

            elif revisãonotcient == 1:
                if datual - d7 == 7:
                    print()
                    input("> Pressione enter para fazer a revisão de Notação científica...")
                    print()
                    listaop = ["a","b","c","d"]
                    notcientificalist = ["• Considere o número 0,00000000000002, converta-o em notação científica.",
                    "• O número 349000 em notação científica corresponde a:","• Escreva o número 0,0004 em notação científica.",
                    "• Como escrevemos 5 x 10³ na forma decimal?"]
                    notcientificalistrespota = ["1)2x10^-14","2)20x10^-11","3)3x10^10","4)4x10^-12",
                    "1)3x10^-14","2)3,49x10^5","3)349x10^6","4)34,9x10^-10","1)4x10^-4","2)40x10^-5","3)0,4x10^10","4)4x10^-12",
                    "1)0,05","2)0,000005","3)0,005","4)0,5"]
                    gabarito = [1,2,1,3]
                    gabarito2 = [")2x10^-14",")3,49x10^5",")4x10^-4",")0,005"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(notcientificalist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(notcientificalistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {notcientificalistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 7 dias")

            else:
                print("• Faça alguma aula para liberar a revisão")

        elif Menu == 5:
            #Contagem revisão 30 dias
            datual = datetime.now()

            if revisãooperaçãobasica == 1:
                if datual - d1 == 30:                    
                    print()
                    input("> Pressione enter para fazer a revisão de Operações básicas...")
                    print()
                    listaop = ["1","2","3","4"]
                    OpBasiclist = [
                    """• Calcule: 765 + 456:""", 
                    """• Qual o resultado da operação: 56 x 9:""", 
                    """• Calcule: 895 - 123:""", 
                    """• Qual o resultado da soma: 234 + 876:""", 
                    ]

                    OpBasiclistrespota = [
                    "1) 1.700", "2) 1.221", "3) 1.321", "4) 1.121", 
                    "1) 504", "2) 560", "3) 469", "4) 392",
                    "1) 762", "2) 782", "3) 772", "4) 789", 
                    "1) 1.110", "2) 1.000", "3) 1.010", "4) 1.100", 
                    ]
                    gabarito = [2, 1, 3, 1]
                    gabarito2 = [") 1.221", ") 504", ") 772", ") 1.110"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(OpBasiclist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(OpBasiclistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {OpBasiclistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 30 dias")
                

            elif revisãopotenciaerad == 1:
                if datual - d2 == 30:                        
                    print()
                    input("> Pressione enter para fazer a revisão de Potenciação e radiciação...")
                    print()
                    listaop = ["1","2","3","4"]
                    PotRadlist = [
                    """• Calcule: 3³ x 2²:""", 
                    """• Qual o resultado da operação: (2²)²:""", 
                    """• Calcule: (2 x 3)²:""", 
                    """• Calcule: (2²+4)²:""", 
                    ]

                    PotRadlistrespota = [
                    "1) 100", "2) 108", "3) 110", "4) 106", 
                    "1) 8", "2) 2", "3) 4", "4) 16",
                    "1) 6", "2) 12", "3) 36", "4) 24", 
                    "1) 64", "2) 32", "3) 16", "4) 24", 
                    ]
                    gabarito = [2, 4, 3, 1]
                    gabarito2 = [") 108", ") 16", ") 36", ") 64"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(PotRadlist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(PotRadlistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {PotRadlistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 30 dias")
                

            elif revisãoexpressaonum == 1:
                if datual - d3 == 30: 
                    print()
                    input("> Pressione enter para fazer a revisão de Expressões númericas...")
                    print()
                    listaop = ["1","2","3","4"]
                    ExpNumlist = [
                    """• Analise a solução da expressão algébrica abaixo e assinale a alternativa correta:

                    {(10·10 + 4·11):12 – [(20 + 19·10):39 + 15]} + 50 =

                    {(100 + 44):12 – [(39·10):39 + 15]} + 50 =

                    {144:12 – [390:39 + 15]} + 50 =

                    {12 – [10 + 15]} + 50 =

                    {12 – 25} + 50 =

                    – 13 + 50 =

                    37""", 
                    """• Calcule: (34 x 7) - (23 x 2)""", 
                    """• Calcule: (37 x 3) + (22 x 3)""", 
                    """• Calcule: [(71 x 4) - (18 x 6)] x5""", 
                    ]

                    ExpNumlistrespota = [
                    "1) A resolução está correta, nenhum erro foi cometido.", "2) A resolução está correta, mas por coincidência, pois alguns erros foram cometidos.", "3) A resolução está incorreta, o verdadeiro resultado é 50.", "4) A resolução está incorreta, pois foi feita uma soma em vez de dar prioridade a uma multiplicação.", 
                    "1) 192", "2) 205 ", "3) 202", "4) 190",
                    "1) 192", "2) 177 ", "3) 209", "4) 170", 
                    "1) 195", "2) 176 ", "3) 880", "4) 876", 
                    ]
                    gabarito = [4, 1, 2, 3]
                    gabarito2 = [") A resolução está incorreta, pois foi feita uma soma em vez de dar prioridade a uma multiplicação.", 
                    ") 192", ") 177", ") 880"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(ExpNumlist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(ExpNumlistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {ExpNumlistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 30 dias")
                

            elif revisãomultiplosdivisores == 1:
                if datual - d4 == 30:
                    print()
                    input("> Pressione enter para fazer a revisão de Multiplos, divisores, MDC e MMC...")
                    print()
                    listaop = ["1","2","3","4"]
                    MultDivlist = [
                    """• Quais os divisores de 18?""", 
                    """• Quais os divisores comuns de 12 e 18?""", 
                    """• Qual o maior divisor comum entre 12 e 18?""", 
                    """• Em uma confecção, há rolos de malha com medidas de 120, 180 e 240 centímetros. Será preciso cortar o tecido em pedaços iguais, maiores possíveis e, não sobrar nada. Qual será o comprimento máximo de cada tira de malha?""", 
                    ]

                    MultDivlistrespota = [
                    "1) 1, 9, 18", "2) 2, 3, 4, 6 e 12.", "3) 2, 3, 6, 9, 18.", "4) 2, 3 e 6", 
                    "1) 1 e 2", "2) 9 e 12", "3) 1, 2, 3, 4, 9", "4) 2, 3 e 6",
                    "1) 4", "2) 9", "3) 12", "4) 6", 
                    "1) 60", "2) 40", "3) 20", "4) 80", 
                    ]
                    gabarito = [3, 4, 4, 1]
                    gabarito2 = [") 2, 3, 6, 9, 18.", ") 2, 3 e 6", ") 6", ") 60"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(MultDivlist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(MultDivlistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {MultDivlistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 30 dias")
                

            elif revisãooppolinomios == 1:
                if datual - d5 == 30:  
                    print()
                    input("> Pressione enter para fazer a revisão de Operações básicas com polinômios...")
                    print()
                    listaop = ["1","2","3","4"]
                    OpPolilist = [
                    """• Efetue a operação: (–2x² + 5x – 2) + (–3x³ + 2x – 1)""", 
                    """• Efutue a operação: (–2x² + 5x – 2) – (–3x³ + 2x – 1)""", 
                    """• Efetue a operação: (x – 1) * (x2 + 2x - 6)""", 
                    """• Efetue a operação: (2 - x) * (x + 1)""", 
                    ]

                    OpPolilistrespota = [
                    "1) – 3x³ – 2x² + 7x – 3", "2) –2x² + 5x – 2", "3) –3x³ + 2x – 1", "4) 3x³ – 2x² + 7x", 
                    "1) – 3x³ – 2x² + 7x – 3", "2) 3x³ – 2x² + 3x – 1", "3) 3x³ + 2x – 1", "4) 3x³ + 2x² + 7",
                    "1) x³ + x² – 8x + 6", "2) 3x³ + 2x² + 7", "3) -x³ - x² + 8x - 6", "4) -3x³ - 2x² - 7", 
                    "1)  x² - x + 2", "2)  - x² + x + 2", "3) -x² - x - 2", "4)  x² + x - 2", 
                    ]
                    gabarito = [1, 2, 1, 2]
                    gabarito2 = [")  – 3x³ – 2x² + 7x – 3", ") 3x³ – 2x² + 3x – 1", ") x³ + x² – 8x + 6", ") - x² + x + 2"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(OpPolilist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(OpPolilistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {OpPolilistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 30 dias")
                

            elif revisãofracoes == 1:
                if datual - d6 == 30:
                    print()
                    input("> Pressione enter para fazer a revisão de Frações, decimais e dízimas...")
                    print()
                    listaop = ["1","2","3","4"]
                    FracDeciDilist = [
                    """• Diga o valor da multiplicação: 27/4 x 4/9:""", 
                    """• Calcule: 1.234 + (875/5):""", 
                    """• Calcule: 7/10 +7/5""", 
                    """• Dos números a seguir, assinale aquele que corresponde a uma dízima periódica composta.""", 
                    ]

                    FracDeciDilistrespota = [
                    "1) 3", "2) 5/2", "3) 2", "4) 27", 
                    "1) 421,8", "2) 2.109", "3) 1.409", "4) 1.737",
                    "1) 7", "2) 1,4", "3) 0,7", "4) 2,1", 
                    "1) 3,14159284…", "2) 2,21111", "3) 0,3333…", "4) 1,21111…", 
                    ]
                    gabarito = [1, 3, 4, 4]
                    gabarito2 = [") 3", ") 1.409", ") 2,1", ") 1,21111…"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(FracDeciDilist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(FracDeciDilistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {FracDeciDilistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()

                else:
                    print("• Ainda não passou o tempo necessário para a revisão 30 dias")
                

            elif revisãonotcient == 1:
                if datual - d7 == 30:
                    print()
                    input("> Pressione enter para fazer a revisão de Notação científica...")
                    print()
                    listaop = ["1","2","3","4"]
                    NotCientlist = [
                    """• A distância entre o planeta Terra e o Sol é de 149.600.000 km. Qual a distância entre a Terra e Sol em Notação científica?""", 
                    """• A idade aproximada do planeta Terra é de 4.543.000.000 anos. Qual a idade aproximada da Terra em Notação científica?""", 
                    """• O diâmetro de um átomo é da ordem de 1 nanômetro, ou seja, 0,0000000001. Qual o diâmetro do raio em Notação científica?""", 
                    """• Resolva utilizando notação científica: 0,00003 * 0,0027:""", 
                    ]

                    NotCientlistrespota = [
                    "1) 1,496 * 10^8", "2) 14,96 * 10^7", "3) 1,496 * 10^7", "4) 1,496 * 10^9", 
                    "1) 4,543 * 10^9", "2) 45,43 * 10^8", "3) 4,543 * 10^10", "4) 4,543 * 10^7",
                    "1) 1 * 10^-9", "2) 1 * 10^-10", "3) 1 * 10^-11", "4) 1 * 10^10", 
                    "1) 0,0000081", "2) 0,00000081", "3) 0,0000000081", "4) 0,000000081", 
                    ]
                    gabarito = [1, 1, 2, 4]
                    gabarito2 = [") 1,496 * 10^8", ") 4,543 * 10^9", ") 1 * 10^-10", ") 0,000000081"]
                    respostas = []

                    n = 0
                    y = 0
                    while True:
                        while y != 4:
                            print(NotCientlist[y])
                            y+= 1
                            l = 0
                            while l != 4: 
                                print(NotCientlistrespota[n])
                                n+= 1
                                l+= 1
                            while True:
                                resposta = input("• Digite o número da alternativa escolhida: ")
                                print()
                                if resposta.isdigit():
                                    resposta = int(resposta)
                                    if 0 < resposta < 5:
                                        respostas.append(resposta)
                                        break
                                    else:
                                        continue
                                else:
                                    continue
                        break    

                    print("Gabarito: ")
                    for k in range(0,4):
                        print(f"[Questão {k + 1}: {gabarito[k]}{gabarito2[k]}]", end=" ")
                        print()
                    print()

                    v = 0
                    print("Suas respostas: ")
                    for c in range(0,4):
                        variavelsoma = respostas[c] - 1
                        print(f"[Questão {c + 1}: {NotCientlistrespota[c + v + variavelsoma]}]", end=" ")
                        v+= 3
                        print()
                    print()  

                    print("Sua Pontuação: ")
                    Pontuação = 0
                    for p in range(0,4):
                        if respostas[p] == gabarito[p]:
                            Pontuação += 1
                        else:
                            continue
                    print(f" > Nota: {Pontuação}/{len(gabarito)}")
                    print()
                else:
                    print("• Ainda não passou o tempo necessário para a revisão 30 dias")
                
            else:
                print("• Faça alguma aula para liberar a revisão")

        elif Menu == 6:
            # Opção para mostrar fontes de pesquisa
            print("> Fontes de pesquisa utilizadas nas matérias <")
            print("""
 • https://exercicios.brasilescola.uol.com.br/exercicios-matematica/exercicios-sobre-operacoes-com-numeros-decimais.htm#resp-2
 • https://www.todamateria.com.br/fracoes/
 • https://www.todamateria.com.br/exercicios-de-fracoes/
 • https://www.infoescola.com/matematica/adicao-subtracao-e-multiplicacao-de-polinomios/exercicios/
 • https://exercicios.brasilescola.uol.com.br/exercicios-matematica/exercicios-sobre-adicao-subtracao-polinomios.htm
 • https://blogdoenem.com.br/polinomios-definicao-e-operacoes/
 • https://www.todamateria.com.br/polinomios/
 • https://www.todamateria.com.br/mmc-e-mdc-exercicios/
 • https://www.todamateria.com.br/mmc-e-mdc/
 • https://www.todamateria.com.br/multiplos-e-divisores/
 • https://sabermatematica.com.br/exercicios-resolvidos-sobre-expressoes-numericas.html
 • https://exercicios.brasilescola.uol.com.br/exercicios-matematica/exercicios-sobre-expressoes-numericas.htm#resp-1
 • https://www.todamateria.com.br/expressoes-numericas/
 • https://www.todamateria.com.br/potenciacao-e-radiciacao/
 • https://www.educamaisbrasil.com.br/enem/matematica/operacoes-matematicas
 • https://exercicios.brasilescola.uol.com.br/exercicios-matematica/exercicios-sobre-calculo-mmc-mdc.htm
 • https://www.todamateria.com.br/mmc-e-mdc-exercicios/""")

        elif Menu == 7:
            # Opção para sair do programa
            break

        elif Menu == 8:
            # Opção de reset
            while True:
                print(" > ATENÇÃO ESSA OPÇÃO FAZ COM QUE O PROGRAMA REINICIE A CONTAGEM DOS DIAS ESTUDADOS < ")
                decisão = input("• Gostaria de RESETAR O PROGRAMA(s/n)? ")
                if decisão == "s" or decisão == "S" or decisão == "Sim" or decisão == "sim":
                    collection7.update_one(
                            {'nome':'dia1'},{'$set':{"d1" : None}})
                    collection7.update_one(
                        {'nome':'dia1'},{'$set':{"variavelrevisao" : None}})
                    collection8.update_one(
                            {'nome':'dia2'},{'$set':{"d2" : None}})
                    collection8.update_one(
                        {'nome':'dia2'},{'$set':{"variavelrevisao" : None}})
                    collection9.update_one(
                            {'nome':'dia3'},{'$set':{"d3" : None}})
                    collection9.update_one(
                        {'nome':'dia3'},{'$set':{"variavelrevisao" : None}})
                    collection10.update_one(
                            {'nome':'dia4'},{'$set':{"d4" : None}})
                    collection10.update_one(
                        {'nome':'dia4'},{'$set':{"variavelrevisao" : None}})
                    collection11.update_one(
                            {'nome':'dia5'},{'$set':{"d5" : None}})
                    collection11.update_one(
                        {'nome':'dia5'},{'$set':{"variavelrevisao" : None}})
                    collection12.update_one(
                            {'nome':'dia6'},{'$set':{"d6" : None}})
                    collection12.update_one(
                        {'nome':'dia6'},{'$set':{"variavelrevisao" : None}})
                    collection13.update_one(
                            {'nome':'dia7'},{'$set':{"d7" : None}})
                    collection13.update_one(
                        {'nome':'dia7'},{'$set':{"variavelrevisao" : None}})
                    print("• PROGRAMANDO REINICIANDO... RETORNANDO AO MENU...")
                    time.sleep(10)
                    break

                elif decisão == "n" or decisão == "N" or decisão == "Não" or decisão == "não":
                    break
                else:
                    continue
        else:
            print("• Opção inválida, Digite uma opção existente")
            continue

    else:
        print("• Opção inválida, Digite uma opção existente")
        continue