import datetime
from backend import db
from sqlalchemy import Column, Integer, String, DateTime


class Budget(db.Model):
    __tablename__ = 'budget'

    id = Column(Integer, primary_key=True)
    date_posted = Column(DateTime, nullable=False)
    budget_amount = Column(Integer)
    withdraw_category = Column(String(20))
    withdraw_description = Column(String(20))
    withdraw_amount = Column(Integer)

    def __init__(self, budget_amount=None, withdraw_category=None, withdraw_description=None, withdraw_amount=None):
        self.date_posted = datetime.datetime.now()
        self.budget_amount = budget_amount
        self.withdraw_category = withdraw_category
        self.withdraw_description = withdraw_description
        self.withdraw_amount = withdraw_amount

    def __repr__(self):
        return f"Budget('{self.date_posted}', '{self.withdraw_description}, '{self.withdraw_amount}')"
