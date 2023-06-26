#Sua empresa te passou uma lista com requisições de treinamentos (muitos repetidos), você tem que definir o cenário que melhor atenda os pedidos, o budget é de 150 moedas e você tem um dicionário que contém o nome do treinamento e o valor dele treinamentos = [{'treinamento':'Scrum','moedas':30}, {'treinamento':'Data Science','moedas':40}, {'treinamento':'Gestão de Projetos','moedas':50}, {'treinamento':'Marketing','moedas':30}, {'treinamento':'Cloud','moedas':20}, {'treinamento':'Blockchain','moedas':10}, {'treinamento':'Python','moedas':30}] pedidos = ['Scrum','Data Science','Gestão de Projetos','Marketing','Cloud','Python','Python','Python', 'Scrum','Data Science','Gestão de Projetos','Marketing','Data Science','Gestão de Projetos', 'Python','Marketing','Data Science','Gestão de Projetos','Data Science','Gestão de Projetos','Data Science']#

treinamentos = [{'treinamento':'Scrum','moedas':30}, 
                {'treinamento':'Data Science','moedas':40}, 
                {'treinamento':'Gestão de Projetos','moedas':50}, 
                {'treinamento':'Marketing','moedas':30}, 
                {'treinamento':'Cloud','moedas':20}, 
                {'treinamento':'Blockchain','moedas':10}, 
                {'treinamento':'Python','moedas':30}]

pedidos = ['Scrum','Data Science','Gestão de Projetos','Marketing','Cloud','Python','Python','Python', 'Scrum','Data Science','Gestão de Projetos','Marketing','Data Science','Gestão de Projetos', 'Python','Marketing','Data Science','Gestão de Projetos','Data Science','Gestão de Projetos','Data Science']

def get_value (x,b):
    for a in x:
        if a ['treinamento'] in b:
            print('valor: ', a ,'Média')
            return a ['moedas']

ped = sorted(set(pedidos))
for a in ped:
    print('Solicitações: ',pedidos.count(a),'\n treinamentos:', a)
    val = get_value(treinamentos,a)
    for b in treinamentos:
        b['total_pedidos']=pedidos.count(a)

budget= 150
count = 6
total=[]
while budget >0:
    for a in treinamentos:
        qtd = a.get('total_pedidos',0)
        if qtd==count:
            print('treinamento', a['treinamento'], 'çomprado')
            total_.append(qtd)
            budget= budget-a['moedas']
            count = count -1
        else:
            continue
print('total de pedidos atendidos',sum(total),'representando',sum(total)/len(pedidos),'% de atendimento')        