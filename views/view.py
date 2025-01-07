import __init__
from models.database import engine
from models.model import Subscription,Payments
from sqlmodel import Session,select
from datetime import date,datetime

#Lógicas da aplicação
class SubscriptionService:
    def __init__(self,engine):
        self.engine = engine 

    def create(self, subscription: Subscription):
        with Session(self.engine) as session:
                session.add(subscription)
                session.commit()
                return subscription
        
    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results= session.exec(statement).all()
        return results

    def delete(self, subscription_id):
        with Session(self.engine) as session:
            statement = select(Subscription).where(Subscription.id == subscription_id)
            result = session.exec(statement).one_or_none()

            if result is None:
                print(f"Nenhuma assinatura encontrada com o ID {subscription_id}.")
                return

            session.delete(result)
            session.commit()
            print(f"Assinatura com ID {subscription_id} foi excluída com sucesso.")

    def _has_pay(self, results):
        for result in results:
            if result.date.month == date.today().month:
                return True
        return False
                
    def pay(self, subscription: Subscription):
        with Session(self.engine) as session:
            statement = select(Payments).join(Subscription).where(Subscription.empresa == subscription.empresa)
            results = session.exec(statement).all()

            if self. _has_pay(results):
                question = input ('essa conta já foi paga esse mês, pagar novamente ? Y OU N: ')                     

                if not question.upper() == 'Y':
                    return
                
                pay = Payments(subscription_id=subscription.id)
                session.add(pay)
                session.commit()

    def total_value(self):
        with Session(self.engine) as session:
            statement = select(Subscription)      
            results = session.exec(statement).all()

        total = 0

        for result in results:
            total += result.valor

        return float(total)

    def _get_last_12_months_native(self):
        today = datetime.now()
        year = today.year
        month = today.month
        last_12_months = []
        for _ in range(12):
            last_12_months.append((month, year))
            month -= 1
            if month == 0:
                month = 12
                year -= 1
        return last_12_months[::-1]

    def _get_values_for_months(self, last_12_months):
        with Session(self.engine) as session:
            # Busca pagamentos associados às assinaturas
            statement = select(Payments).join(Subscription)
            results = session.exec(statement).all()

            print("Pagamentos encontrados:")
            for result in results:
                print(f"Pagamento: ID={result.id}, Date={result.date}, Empresa={result.subscription.empresa}, Valor={result.subscription.valor}")

            value_for_months = []
            for month, year in last_12_months:
                value = 0
                for result in results:
                    # Verifica se o pagamento está dentro do mês/ano correspondente
                    if result.date.month == month and result.date.year == year:
                        value += float(result.subscription.valor)
                value_for_months.append(value)

            # Exibe valores por mês para depuração
            print("\nValores por mês (debug):")
            for (month, year), value in zip(last_12_months, value_for_months):
                print(f"Mês: ({month}, {year}), Valor: R${value:.2f}")

            return value_for_months
                    
    def gen_chart(self):
        last_12_months = self._get_last_12_months_native()
        values_for_months = self._get_values_for_months(last_12_months)
        

        # Configura o gráfico
        import matplotlib.pyplot as plt
        months = [f"{m:02d}/{y}" for m, y in last_12_months]
        plt.plot(months, values_for_months, marker='o')
        plt.xlabel("Meses")
        plt.ylabel("Valores (R$)")
        plt.title("Gastos nos últimos 12 meses")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
