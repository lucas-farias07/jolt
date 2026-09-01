from sqlalchemy import MetaData, Table, Column, Integer, String, Date

metadata = MetaData()

tasks_table = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("description", String),
    Column("status", Integer),
    Column("deadline", Date)
)

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String)
)

products_table = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String)
)
