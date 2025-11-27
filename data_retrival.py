import pandas as pd
import sqlite3

class DataRetrieval:
    def __init__ (self):
        self.conn = sqlite3.connect("Marketanalysis.db")
        self.cursor = self.conn.cursor()
        self.df = pd.read_sql_query(
            "SELECT tickername AS ticker, companyname AS company FROM STOCK_LIST",
            self.conn
        )
        self.query = "appl"

    def search(self):

        q = self.query.strip()
        mask_company = self.df["company"].str.contains(q, case=False, na=False)
        mask_ticker  = self.df["ticker"].str.contains(q, case=False, na=False)

        return self.df[mask_company | mask_ticker]
    def retrieve(self):



stock = DataRetrieval()
print(stock.search())