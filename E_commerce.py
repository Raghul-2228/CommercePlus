import pandas as pd
from sqlalchemy import create_engine

dim_customers = pd.read_csv("customers.csv")
dim_products = pd.read_csv("products.csv")
fact_sales = pd.read_csv("sales.csv")

engine = create_engine("mysql+pymysql://root:root@localhost:3306/e_commerce_db")


dim_customers.to_sql(name="dim_customers", con=engine, if_exists="replace", index=False)
dim_products.to_sql(name="dim_products", con=engine, if_exists="replace", index=False)
fact_sales.to_sql(name="fact_sales",con=engine,if_exists="replace", index=False)
