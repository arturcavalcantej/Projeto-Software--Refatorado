# PROJETO DE SOFTWARE - FOLHA DE PAGAMENTO!!
# Aluno: Artur Cavalcante de Jesus

import datetime as dt
from Horista import Horista
from Assalariado import Assalariado
from Comissionado import Comissionado
from Vendas import Vendas
from Sindicato import Sindicato
from Deposito import Deposito
from Correios import Correios
from Cheque import Cheque
from EmpregadoTemplate import cadhorista, cadassalariado, cadcomissionado

deletedIds = []
numID = 0
sindID = 0
today = dt.datetime(2021, 8, 10)


def getId():
    if (len(deletedIds) > 0):
        return deletedIds.pop(0)
    else:
        global numID
        numID += 1
        return numID



def menu():
    print("Escolha uma opção:")
    print("1 - Adicionar Empregado")
    print("2 - Remover Empregado")
    print("3 - Número de empregados")
    print("4 - Ver dados individuais")
    print("5 - Adicionar ao sindicato")
    print("6 - Lançar cartão de ponto")
    print("7 - Lançar resultado de vendas")
    print("8 - Visualizar resultado de venda")
    print("9 - Taxa de serviço")
    print("10 - Editar Empregado")
    print("0 - Voltar")
    x = int(input())
    return x


def employeeChoose():
    print("Escolha uma opção:")
    print("1 - Horista")
    print("2 - Assalariado")
    print("3 - Comissionado")
    print("0 - Cancelar")
    w = int(input())
    return w




def getUnionId():
    global sindID
    sindID += 2
    return sindID




def adicionar(option):
    global emp
    if option == 1:
        emp = cadhorista().add()
    elif option == 2:
        emp = cadassalariado().add()
    elif option == 3:
        emp = cadcomissionado().add()

    return emp


def removeFromSchedule(key, schedule):
    if key in schedule['weekly']:
        schedule['weekly'].remove(key)
    if key in schedule['bi-weekly']:
        schedule['bi-weekly'].remove(key)
    if key in schedule['monthly']:
        schedule['monthly'].remove(key)


def remover(dictionary, schedule):
    key = int(input("Digite o ID do Empregado: "))
    if (key not in dictionary):
        print("ID inválida, nenhum Empregado deletado.")

    else:
        name = dictionary[key]['worker'].name
        deletedIds.append(key)
        removeFromSchedule(key, schedule)
        del dictionary[key]
        print("Operação bem sucedida, Empregado {} deletado.".format(name))


def choosePaymentMethod():
    print("Escolha uma opção:")
    print("1 - Deposito em conta")
    print("2 - Cheque em mãos")
    print("3 - Cheque pelos correios")
    w = int(input())
    return w


def exibir(dictionary):
    if len(dictionary) == 1:
        print("A folha de pagamento contém 1 Empregado.\n")
    else:
        print("A folha de pagamento contém %d Empregados.\n" % len(dictionary))


def buscar(dictionary, uniondict, schedule):
    key = int(input("Digite o ID do Empregado: "))
    if (key not in dictionary):
        print("ID inválida.")
    else:

        print(dictionary[key]['worker'])
        if (dictionary[key]['worker'].kind == 'Comissionado'):
            print("Vendas: {}".format(len(dictionary[key]['sales'])))

        if key in schedule['weekly']:
            print("Empregado pago semanalmente")
        elif key in schedule['bi-weekly']:
            print("Empregado pago bi-semanalmente")
        elif key in schedule['monthly']:
            print("Empregado pago mensalmente")
        print("Forma de pagamento: {}".format(dictionary[key]['worker'].paymentMethod))
        dictionary[key]['worker'].GetNetIncome()
        dictionary[key]['worker'].PrintLastPayment()

        print("Informações sindicais:")
        if ('unionKey' in dictionary[key]):
            print("Empregado sindicalizado.")
            print(uniondict[dictionary[key]['unionKey']])
        else:
            print("Empregado não sindicalizado.")


def unionStatus(dictUnion):
    key = int(input("Digite a ID do Empregado: "))
    if (key not in dictUnion):
        print("ID inválida.")
    else:

        print(dictUnion[key])

def sendTimeCard(dictionary):
    key = int(input("ID do Empregado: "))
    if (key not in dictionary):
        print("ID inválida.")


    elif (dictionary[key]['worker'].kind != "Horista"):
        print(" Empregado não horista.")

    else:
        print("Nome:", format(dictionary[key]['worker'].name))
        hours = float(input("Digite as horas trabalhadas: "))
        dictionary[key]['worker'].TimeCard(hours)
        print("Cartão submetido com sucesso.")


def sendSalesReport(dictionary):
    key = int(input("Digite a ID do Empregado: "))
    if (key not in dictionary):
        print("ID inválida.")


    elif (dictionary[key]['worker'].kind != "Comissionado"):
        print("Empregado não comissionado.")

    else:
        print("Funcionário:", format(dictionary[key]['worker'].name))
        dateTime = input("Digite a data: ")
        value = float(input("Digite o valor: "))
        saleReport = Vendas(dateTime, value)
        dictionary[key]['sales'].append(saleReport)
        print("Resultado de vendas submetido")


def showSaleReport(dictionary):
    key = int(input("Digite a ID do Empregado: "))
    if (key not in dictionary):
        print("ID inválida.")

    elif (dictionary[key]['worker'].kind != "Comissionado"):
        print("Empregadonão comissionado.")

    else:
        print("Funcionário:", format(dictionary[key]['worker'].name))
        print("Resultados de vendas: %d" % len(dictionary[key]['sales']))
        if (len(dictionary[key]['sales']) > 0):
            print("Ultimo resultado de venda: ")
            print(dictionary[key]['sales'][-1])


def addsindicato(dictionary, unionDic):
    key = int(input("ID do Empregado: "))
    if (key not in dictionary):
        print("ID inválida.")

    else:
        if ('unionKey' in dictionary[key]):
            print("Empregado já sindicalizado.")
        else:
            unionId = getUnionId()
            dictionary[key]['unionKey'] = unionId
            unionDic[unionId] = Sindicato(unionId)
            print("Empregado sindicalizado. ID  sindical número {}".format(sindID))


def sendUnionFee(dictionary, unionDic):

    key = int(input("ID do Empregado: "))
    if (key not in dictionary):
        print("ID inválida.")

    else:
        if ('unionKey' not in dictionary[key]):
            print("Empregado não sindicalizado.")
        else:
            print("Id sindical: %d" % dictionary[key]['unionKey'])
            value = float(input("Digite o valor da taxa:"))
            unionDic[dictionary[key]['unionKey']].incrementFee(value)
            print("Taxa adicionada.")


def edicao():
    print("1 - Editar dados pessoais do Empregado")
    print("2 - Editar tipo de Empregado")
    print("3 - Editar situação sindical do Empregado")
    print("4 - Editar agenda de pagamentos")
    print("5 - Editar forma de pagamento")
    print("0 - Cancelar")
    w = int(input())
    return w


def alterapessoal(dictionary, key):
    dictionary[key]['worker'].EditData(dictionary, key)
    print("Empregado editado com sucesso.")


def changeToHourly(dictionary, key):
    name = dictionary[key]['worker'].name
    address = dictionary[key]['worker'].address
    salary = dictionary[key]['worker'].salary
    editedEmployee = Horista(name, address, salary)
    dictionary[key]['worker'] = editedEmployee
    print("Tipo de Empregado editado")
    print(dictionary[key]['worker'])


def changeToSalaried(dictionary, key):
    name = dictionary[key]['worker'].name
    address = dictionary[key]['worker'].address
    salary = dictionary[key]['worker']._salary
    editedEmployee = Assalariado(name, address, salary)
    dictionary[key]['worker'] = editedEmployee
    print("Tipo de Empregado editado")
    print(dictionary[key]['worker'])


def changeToComissioned(dictionary, key):
    name = dictionary[key]['worker'].name
    address = dictionary[key]['worker'].address
    salary = dictionary[key]['worker']._salary
    bonus = float(input("Bônus do Empregado: "))
    editedEmployee = Comissionado(name, address, salary, bonus)
    dictionary[key]['worker'] = editedEmployee
    print("Tipo de Empregado editado")
    print(dictionary[key]['worker'])


def changeEmployeeType(dictionary, key):
    if (dictionary[key]['worker'].kind == 'Horista'):
        print("Escolha o novo tipo para o Empregado: ")
        print("1 - Comissionado")
        print("2 - Assalariado")
        w = int(input())
        if (w == 1):
            changeToComissioned(dictionary, key)
        elif (w == 2):
            changeToSalaried(dictionary, key)
        else:
            print("Cancelando")

    elif (dictionary[key]['worker'].kind == 'Assalariado'):
        print("Escolha o novo tipo para o Empregado: ")
        print("1 - Comissionado")
        print("2 - Horista")
        w = int(input())
        if (w == 1):
            changeToComissioned(dictionary, key)
        elif (w == 2):
            changeToHourly(dictionary, key)
        else:
            print("Cancelando")

    elif (dictionary[key]['worker'].kind == 'Comissionado'):
        print("Escolha o novo tipo para o Empregado: ")
        print("1 - Horista")
        print("2 - Assalariado")
        w = int(input())
        if (w == 1):
            changeToHourly(dictionary, key)
        elif (w == 2):
            changeToSalaried(dictionary, key)
        else:
            print("Cancelando")


def changePaymentMethod(dictionary, key):
    if (dictionary[key]['worker'].paymentMethod == 'Deposito em conta'):
        print("Escolha o novo metodo de pagamento: ")
        print("1 - Cheque em mãos")
        print("2 - Cheque pelos correios")
        w = int(input())
        if (w == 1):
            dictionary[key]['worker'].setPaymentMethod('Cheque em mãos')
        elif (w == 2):
            dictionary[key]['worker'].setPaymentMethod('Cheque pelos correios')
        else:
            print("Cancelado")

    elif (dictionary[key]['worker'].paymentMethod == 'Cheque em maos'):
        print("Escolha o novo metodo de pagamento: ")
        print("1 - Deposito em conta")
        print("2 - Cheque pelos correios")
        w = int(input())
        if (w == 1):
            dictionary[key]['worker'].setPaymentMethod('Deposito em conta')
        elif (w == 2):
            dictionary[key]['worker'].setPaymentMethod('Cheque pelos correios')
        else:
            print("Cancelando...")

    elif (dictionary[key]['worker'].paymentMethod == 'Cheque pelos correios'):
        print("Escolha o novo metodo de pagamento: ")
        print("1 - Cheque em maos")
        print("2 - Deposito em conta")
        w = int(input())
        if (w == 1):
            dictionary[key]['worker'].setPaymentMethod('Cheque em maos')
        elif (w == 2):
            dictionary[key]['worker'].setPaymentMethod('Deposito em conta')
        else:
            print("Cancelando")


def changeUnionStatus(dictionary, key, unionDic):
    if ('unionKey' in dictionary[key]):
        unionID = dictionary[key]['unionKey']
        del unionDic[unionID]
        del dictionary[key]['unionKey']

        print("Removido")

    else:
        unionId = getUnionId()
        dictionary[key]['unionKey'] = unionId
        unionDic[unionId] = Sindicato(unionId)
        print("Funcionario filiado ao sindicado. ID sindical numero {}".format(unionId))


def schedulePaymentOptions():
    print("Escolha uma opção:")
    print("1 - Pagamento semanal")
    print("2 - Pagamento bi-semanal")
    print("3 - Pagamento mensal")
    print("0 - Cancelar")
    w = int(input())
    return w


def changePaymentSchedule(option, key, schedule):
    if key in schedule['weekly']:
        schedule['weekly'].remove(key)
    if key in schedule['bi-weekly']:
        schedule['bi-weekly'].remove(key)
    if key in schedule['monthly']:
        schedule['monthly'].remove(key)
    if (option == 1):
        schedule['weekly'].add(key)
    elif (option == 2):
        schedule['bi-weekly'].add(key)
    elif (option == 3):
        schedule['monthly'].add(key)


def editar(dictionary, unionDic, schedule):
    key = int(input("ID do Empregado: "))
    if (key not in dictionary):
        print("ID inválida.")

    else:
        opcao = edicao()
        if (opcao == 1):
            alterapessoal(dictionary, key)
        elif (opcao == 2):
            changeEmployeeType(dictionary, key)
        elif (opcao == 3):
            changeUnionStatus(dictionary, key, unionDic)
        elif (opcao == 4):
            payoption = schedulePaymentOptions()
            if (payoption > 3):
                print("Cancelado")
            else:
                changePaymentSchedule(payoption, key, schedule)
                print("Agenda alterada")
        elif (opcao == 5):
            changePaymentMethod(dictionary, key)


def rodarfolha(employeeDict, unionDict, payrollSchedule):
    while True:
        opcao = menu()

        if opcao == 1:
            individualDict = {}
            value = getId()
            employeeOption = employeeChoose()
            if (employeeOption != 0):
                newEmployee = adicionar(employeeOption)
                if (employeeOption == 1):
                    try:
                        payrollSchedule['weekly'].add(value)
                    except KeyError:
                        payrollSchedule['weekly'] = {value}
                elif (employeeOption == 2):
                    try:
                        payrollSchedule['monthly'].add(value)
                    except KeyError:
                        payrollSchedule['monthly'] = {value}
                elif (employeeOption == 3):
                    try:
                        payrollSchedule['bi-weekly'].add(value)
                    except KeyError:
                        payrollSchedule['bi-weekly'] = {value}
                    individualDict['sales'] = []
                paymentOption = choosePaymentMethod()
                if paymentOption == 1:
                    newEmployee.setPaymentMethod('Deposito em conta')
                elif paymentOption == 2:
                    newEmployee.setPaymentMethod('Cheque em maos')
                elif paymentOption == 3:
                    newEmployee.setPaymentMethod('Cheque pelos correios')

                individualDict['worker'] = newEmployee

                unionOption = input("Entrar ao sindicato? (S/N)")
                if (unionOption == 's' or unionOption == 'S'):
                    unionId = getUnionId()
                    individualDict['unionKey'] = unionId
                    unionDict[unionId] = Sindicato(unionId)
                    print("Empregado sindicalizado. ID sindical numero {}".format(unionId))
                else:
                    print("Empregado não filiado ao sindicato.")
                employeeDict[value] = individualDict
                print("ID do Empregado: %d" % value)

            else:
                print("Retornando")

        elif opcao == 2:
            remover(employeeDict, payrollSchedule)
        elif opcao == 3:
            exibir(employeeDict)
        elif opcao == 4:
            buscar(employeeDict, unionDict, payrollSchedule)
        elif opcao == 5:
            addsindicato(employeeDict, unionDict)
        elif opcao == 6:
            if (len(employeeDict) > 0):
                sendTimeCard(employeeDict)
            else:
                print("A folha de pagamento está vazia")

        elif opcao == 7:
            if (len(employeeDict) > 0):
                sendSalesReport(employeeDict)
            else:
                print("A folha de pagamento está vazia")


        elif opcao == 8:
            showSaleReport(employeeDict)
        elif opcao == 9:
            sendUnionFee(employeeDict, unionDict)
        elif opcao == 10:
            editar(employeeDict, unionDict, payrollSchedule)
        else:
            print("Saindo...")

            break


def checkIfFriday(day):
    if (day.weekday() == 4):
        return True
    else:
        return False


def checkLastWorkDay(day):
    thimonth = day.month
    nextmonth = thimonth + 1
    tomorrow = day + dt.timedelta(days=1)
    nextMonday = day + dt.timedelta(days=3)
    if (day.weekday() >= 0 and day.weekday() <= 4 and tomorrow.month == nextmonth):
        return True
    elif (day.weekday() >= 0 and day.weekday() <= 4 and nextMonday.month == nextmonth):
        return True
    else:
        return False


def calcPaymentValue(dictionary, unionDict, key):
    global result
    if (dictionary[key]['worker'].kind == 'Horista'):
        result = dictionary[key]['worker'].GetIncome()

    elif (dictionary[key]['worker'].kind == 'Assalariado'):
        result = dictionary[key]['worker'].GetIncome()

    elif (dictionary[key]['worker'].kind == 'Comissionado'):
        salary = dictionary[key]['worker'].GetSalary()
        bonusPercentage = (dictionary[key]['worker'].GetBonus()) / 100
        salesResult = 0
        for sale in dictionary[key]['sales']:
            salesResult += sale.value
        dictionary[key]['sales'].clear()
        result = bonusPercentage * salesResult + salary

    if ('unionKey' in dictionary[key]):
        fee = unionDict[dictionary[key]['unionKey']].getFee()
        return result - fee
    else:
        return result



def weeklyPagar(dictionary, unionDic, schedule, day):
        for key in schedule['weekly']:
                payment = calcPaymentValue(dictionary, unionDic, key)
                if (dictionary[key]['worker'].paymentMethod == 'Deposito em conta'):
                    deposit = Deposito(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(deposit)
                    print("Pagamento semanal efetuado")
                elif (dictionary[key]['worker'].paymentMethod == 'Cheque em maos'):
                    check = Cheque(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(check)
                    print("Pagamento semanal efetuado")
                elif (dictionary[key]['worker'].paymentMethod == 'Cheque pelos correios'):
                    check = Correios(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(check)
                    print("Pagamento semanal efetuado")

def biweeklyPagar(dictionary, unionDic, schedule, day):
        for key in schedule['bi-weekly']:
                payment = calcPaymentValue(dictionary, unionDic, key)
                if (dictionary[key]['worker'].paymentMethod == 'Deposito em conta'):
                    deposit = Deposito(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(deposit)
                    print("Pagamento bi-semanal efetuado")
                elif (dictionary[key]['worker'].paymentMethod == 'Cheque em maos'):
                    check = Cheque(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(check)
                    print("Pagamento bi-semanal efetuado")
                elif (dictionary[key]['worker'].paymentMethod == 'Cheque pelos correios'):
                    check = Correios(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(check)
                    print("Pagamento bi-semanal efetuado")

def monthlyPagar(dictionary, unionDic, schedule, day):
        for key in schedule['monthly']:
                payment = calcPaymentValue(dictionary, unionDic, key)

                if (dictionary[key]['worker'].paymentMethod == 'Deposito em conta'):
                    deposit = Deposito(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(deposit)
                    print("Pagamento mensal efetuado")
                elif (dictionary[key]['worker'].paymentMethod == 'Cheque em maos'):
                    check = Cheque(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(check)
                    print("Pagamento mensal efetuado")
                elif (dictionary[key]['worker'].paymentMethod == 'Cheque pelos correios'):
                    check = Correios(dictionary[key]['worker'].name, payment, day)
                    dictionary[key]['worker'].PutInWallet(check)
                    print("Pagamento mensal efetuado")

def pagar(dictionary, unionDic, schedule, day):
    if len(dictionary) == 0:
            print("Não há funcionários para serem pagos")
    elif (day.weekday() > 4):
            print("É fim de semana, nenhum pagamento feito.")
    else:
        if (checkIfFriday(day) or checkLastWorkDay(day)):
                weeklyPagar(dictionary, unionDic, schedule, day)
                biweeklyPagar(dictionary, unionDic, schedule, day)
                monthlyPagar(dictionary, unionDic, schedule, day)
        else:
                print("Nenhum pagamento agendado hoje.")


def runPayRoll(employeeDict, unionDict, schedule):
    global today
    pagar(employeeDict, unionDict, schedule, today)
    today += dt.timedelta(days=1)


def menuprincipal():
    print("1 - Menu principal")
    print("2 - Rodar folha de pagamento")
    print("3 - Sair")
    w = int(input())

    return w


def main():
    employeeDict = {}
    unionDict = {}
    payrollSchedule = {}
    payrollSchedule['weekly'] = set()
    payrollSchedule['bi-weekly'] = set()
    payrollSchedule['monthly'] = set()
    while True:

        print("Olá, data: {:%A, %d %b %Y}.".format(today))
        x = menuprincipal()
        if (x == 1):
            rodarfolha(employeeDict, unionDict, payrollSchedule)
        elif (x == 2):
            runPayRoll(employeeDict, unionDict, payrollSchedule)
        elif (x == 3):
            print("Saindo")
            break
        else:

            continue


main()
