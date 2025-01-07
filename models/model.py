# Importações necessárias
from sqlmodel import Field, SQLModel, Relationship  # Classes e funções do SQLModel
from typing import Optional, List  # Para campos opcionais e listas
from datetime import date  # Tipo de dado para datas
from decimal import Decimal  # Precisão para valores monetários

# Modelo de assinatura (Subscription)
class Subscription(SQLModel, table=True):  # Define a tabela "subscription"
    id: int = Field(primary_key=True)  # Chave primária
    empresa: str  # Nome da empresa
    site: Optional[str] = None  # URL opcional
    data_assinatura: date  # Data da assinatura
    valor: Decimal  # Valor mensal
    payments: List["Payments"] = Relationship(back_populates="subscription")  # Relacionamento com Payments

# Modelo de pagamentos (Payments)
class Payments(SQLModel, table=True):  # Define a tabela "payments"
    id: int = Field(default=None, primary_key=True)  # Chave primária
    subscription_id: int = Field(foreign_key="subscription.id")  # Chave estrangeira para "subscription"
    subscription: Subscription = Relationship(back_populates="payments")  # Relacionamento com Subscription
    date: date  # Data do pagamento
