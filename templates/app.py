import __init__
from views.view import SubscriptionService
from models.database import engine
from models.model import Subscription
from datetime import datetime
from decimal import Decimal

class UI:
    def __init__(self):
        self.subscription_service = SubscriptionService(engine)
    
    def start(self):
        while True:
            print('''
            [1] -> Adicionar assinatura
            [2] -> Remover assinatura
            [3] -> Valor total
            [4] -> Gastos últimos 12 meses
            [5] -> Pagar assinatura
            [6] -> Listar assinaturas
            [7] -> Sair
''')
            choice = int(input('escolha uma opção: '))

            match choice:
                case 1:
                    self.add_subscription()
                case 2:
                    self.delete_subscription()
                case 3:
                    self.total_value()
                case 4:
                    self.subscription_service.gen_chart()
                case 5:
                    self.pay_subscription()
                case 6:
                    self.list_all_subscription()
                case _:
                    break
    
    def add_subscription(self):
        empresa = input('Empresa: ')
        site = input('Site: ')
        data = datetime.strptime(input('Data de assisnatura: '), '%d/%m/%Y')
        valor = Decimal(input('Valor: '))
        subscription = Subscription(empresa= empresa, site= site, data_assinatura= data, valor= valor)
        self.subscription_service.create(subscription)

    def delete_subscription(self):
        subscription = self.subscription_service.list_all()
        print('Escolha qual assinatura deseja excluir')

        for i in subscription:
            print(f'[{i.id}] -> {i.empresa}')
        
        choice = int(input('Escolha a assinatura: '))
        self.subscription_service.delete(choice)
        self.subscription_service.delete_payments(choice)
        print('Assinatura exxcluida com sucesso')
    
    def total_value(self):
        print(f'Seu valor total mensal em assinatura é: {self.subscription_service.total_value()}')
    
    def pay_subscription(self):
        subs = self.subscription_service.list_all()
        for index, val in enumerate(subs):
            print(f'[{index}] -> {val.empresa}')
        choice = int(input('Escolha a assinatura: '))
        self.subscription_service.pay(subs[choice])
        print('pago com sucesso')

    def list_all_subscription(self):
        subs = self.subscription_service.list_all()
        results = []
        for i in subs:
            results.append(i.empresa)
        print(results)

UI().start()