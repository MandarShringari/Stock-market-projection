import sqlite3
class DatabaseManager:
    def __init__(self):
        super().__init__()

        self.connect_db = sqlite3.connect('Marketanalysis.db')
        self.cursor_obj = self.connect_db.cursor()
 
        self.cursor_obj.execute("PRAGMA foreign_keys = ON;")
   
        self.cursor_obj.execute("""
        CREATE TABLE IF NOT EXISTS USER(
            userID INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            salt INTEGER NOT NULL,
            hashedPassword TEXT NOT NULL
        );
        """)

        self.cursor_obj.execute("""
        CREATE TABLE IF NOT EXISTS PORTFOLIO(
            stockID INTEGER PRIMARY KEY AUTOINCREMENT,
            userID INTEGER NOT NULL,
            ticker TEXT NOT NULL,
            stockName TEXT,
            currentprice REAL,
            volatility REAL,
            timestamp TIMESTAMP,
            FOREIGN KEY (userID) REFERENCES USER(userID)
        );
        """)

        self.cursor_obj.execute("""
        CREATE TABLE IF NOT EXISTS STOCK_HISTORY(
            historyID INTEGER PRIMARY KEY AUTOINCREMENT,
            stockID INTEGER NOT NULL,
            currentPrice REAL NOT NULL,
            marketcap REAL NOT NULL,
            wrange REAL NOT NULL,
            closingprice REAL NOT NULL,
            volume REAL NOT NULL,
            date TEXT,
            predictedprice REAL,
            FOREIGN KEY (stockID) REFERENCES PORTFOLIO(stockID) 
        );
        """)

        self.cursor_obj.execute("""
        CREATE TABLE IF NOT EXISTS STOCK_LIST(
            stockListID INTEGER PRIMARY KEY AUTOINCREMENT,
            tickername TEXT NOT NULL,
            companyname TEXT NOT NULL
        );
        """)

                        
            
             
            
           
            
        

        self.username = "mandar"
        self.salt = 132
        self.hashedpassword = "has"
        self.cursor_obj.execute("SELECT * FROM USER WHERE username = ?", (self.username,))
        existing_user = self.cursor_obj.fetchone()

        if existing_user is None:

            self.cursor_obj.execute(
                "INSERT INTO USER(username, salt, hashedPassword) VALUES(?, ?, ?)",
                (self.username, self.salt, self.hashedpassword)
            )
            self.connect_db.commit()

        self.cursor_obj.execute("SELECT * FROM USER;")
        rows = self.cursor_obj.fetchall()
        for row in rows:
            print(row)

        # Insert CSV stock list data
        import csv
        with open("company_tickers.csv", "r") as f:
            reader = csv.DictReader(f)
            for line in reader:
                self.cursor_obj.execute(
                    "INSERT INTO STOCK_LIST(tickername, companyname) VALUES(?, ?)",
                    (line["ticker"], line["company"])
                )
        self.connect_db.commit()
DatabaseManager()