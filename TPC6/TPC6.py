# dadosDiabetesRaw = [gender,float(age), float(glucoseLevel), int(diabetes)]
# dadosDiabetesTratado = [gender,float(age), float(glucoseLevel) ]

dadosDiabetesRaw = []
dadosDiabetesTratado = []

def lerDataset():
    dataset = open("diabetes_prediction_dataset.csv")
    dataset.readline()
    for linha in dataset:
        linha.strip("\n")
        gender , age , _ , _ , _ , _ , _ , glucoseLevel, temDiabetes = linha.split(",")
        dadosDiabetesRaw.append((gender,float(age),float(glucoseLevel),int(temDiabetes)))
    return dadosDiabetesRaw

def removeNaoDoentes():
    for doente in dadosDiabetesRaw:
        if doente[3] == 1:
            doente2 = list(doente)
            doente2.pop(3)
            doente2 = tuple(doente2)
            dadosDiabetesTratado.append(doente2)
    return dadosDiabetesTratado

def ordenarValores(dist):
    return dist[0]

def distribuicaoSexo():
    distSexo = {}
    for doente in dadosDiabetesTratado:
        if doente[0] in distSexo:
            distSexo[doente[0]] = distSexo[doente[0]] + 1
        else:
            distSexo[doente[0]] = 1
    return distSexo

def distribuicaoEtaria():
    distEtaria = {}
    for doente in dadosDiabetesTratado:
        idadeMin = 25
        idadeMax = 29
        cond = True
        if doente[1] >= 0 and doente[1] <= 10:
            if "0,10" in distEtaria:
                distEtaria["0,10"] = distEtaria["0,10"] + 1
            else:
                distEtaria["0,10"] = 1
        elif doente[1] >= 11 and doente[1] <= 24:
            if "11,24" in distEtaria:
                distEtaria["11,24"] = distEtaria["11,24"] + 1
            else:
                distEtaria["11,24"] = 1
        else: 
            cond = False
            while cond == False:
                placeholder = "%d,%d"%(idadeMin,idadeMax)
                if doente[1] >= idadeMin and doente[1] <= idadeMax:
                    cond = True
                    if placeholder in distEtaria:
                        distEtaria[placeholder] = distEtaria[placeholder] + 1
                    else:
                        distEtaria[placeholder] = 1
                else:
                    idadeMin = idadeMin + 5
                    idadeMax = idadeMax + 5
    return distEtaria

def distribuicaoGlucose():
    distGlucose = {}
    for doente in dadosDiabetesTratado:
        valorMin = 0
        valorMax = 10
        while doente[2] > valorMin:
            valorMin = valorMin + 10
            valorMax = valorMax + 10
        placeholder = "%d,%d"%(valorMin,valorMax)
        if placeholder in distGlucose:
            distGlucose[placeholder] = distGlucose[placeholder] + 1
        else: distGlucose[placeholder] = 1
    return distGlucose

def sorter(dist):
    valores = list(dist.items())
    valores.sort(key = ordenarValores)
    distOrdenada = dict(valores)
    return distOrdenada

def escreveDist(d):
    print("--------------------------------")
    for chave in d:
        print(chave, "         ", d[chave])
    return

def percentagens(d):
    total = 0
    distPercentagem = {}
    for chave in d:
        total = total + d[chave]
    for chave in d:
        distPercentagem.update({chave:round((d[chave]/total)*100,2)})
    return distPercentagem

def main():
    print("""1) Ler dataset
2) Distribuição por sexo
3) Distribuição por escalão etário
4) Distribuição por níveis de glucose
0) Sair
          """)
    escolhaMain = input()

    if escolhaMain == "1":
        lerDataset()
        removeNaoDoentes()
        main()
    if escolhaMain == "2":
        print("Sexo          || Número de Doentes")
        print(escreveDist(distribuicaoSexo()))
        print("Sexo          || Doentes (%)")
        print(escreveDist(percentagens(distribuicaoSexo())))
        main()
    if escolhaMain == "3":
        print("Escalão Etário|| Número de Doentes")
        print(escreveDist(sorter(distribuicaoEtaria())))
        print("Escalão Etário|| Doentes (%)")
        print(escreveDist(percentagens(sorter(distribuicaoEtaria()))))
        main()
    if escolhaMain == "4":
        print("Níveis Glucose|| Número de Doentes")
        print(escreveDist(sorter(distribuicaoGlucose())))
        print("Níveis Glucose|| Doentes (%)")
        print(escreveDist(percentagens(sorter(distribuicaoGlucose()))))
        main()
    if escolhaMain == "0":
        exit()
main()