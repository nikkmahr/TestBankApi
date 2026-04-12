from sqlalchemy.orm import Session
from src.main.api.db.models.credit_table import CreditTable


class CreditCrudDB:
    @staticmethod
    def get_credit_by_id(db: Session, credit_id: int) -> CreditTable | None:
        return db.query(CreditTable).filter_by(id=credit_id).first()