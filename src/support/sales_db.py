from datetime import date
from typing import List

from sqlmodel import Session, SQLModel, create_engine, select, Field


class Sales(SQLModel):
    class Config:
        table = True

    id: str = Field(primary_key=True)
    customer_name: str
    date: date
    price: float


def init_db_with_fake_data(db_file_name: str, db_data: List[Sales]) -> None:
    connection_url: str = f"postgresql://{db_file_name}"
    engine = create_engine(connection_url, echo=True)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        sales = session.exec(select(Sales)).all()
        if len(sales) == 0:
            for sale in db_data:
                session.add(sale)

            session.commit()
