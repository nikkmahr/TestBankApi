from sqlalchemy.orm import Session
from src.main.api.db.models.transactions_table import TransactionsTable


class TransactionCrudDB:
    @staticmethod
    def get_transaction_by_id(db: Session, transaction_id: int) -> TransactionsTable | None:
        return db.query(TransactionsTable).filter_by(id=transaction_id).first()

    @staticmethod
    def get_transactions_by_from_account_id(db: Session, from_account_id: int) -> TransactionsTable | None:
        return db.query(TransactionsTable).filter_by(from_account_id=from_account_id).first()
