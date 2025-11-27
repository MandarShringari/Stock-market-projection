import sqlite3

class DatabaseManager:
    def __init__(self):
        super().__init__()
        self.connect_db = sqlite3.connect('Marketanalysis.db')
        self.cursor_obj = self.connect_db.cursor()
        #self.cursor_obj.execute("PRAGMA foreign_keys = ON;")

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
            currentprice FLOAT,
            volatility FLOAT,
            timestamp TIMESTAMP,
            FOREIGN KEY (userID) REFERENCES USER(userID)
        );
        """)

        self.cursor_obj.execute(""" 
        CREATE TABLE IF NOT EXISTS STOCK_HISTORY(
            historyID INTEGER PRIMARY KEY AUTOINCREMENT,
            stockID INTEGER NOT NULL,
            currentPrice FLOAT NOT NULL,
            marketcap FLOAT NOT NULL,
            wrange FLOAT NOT NULL,                    
            closingprice FLOAT NOT NULL,
            volume FLOAT NOT NULL,
            date TEXT,
            predictedprice FLOAT  
        );
        """)
        self.username = "mandar"
        self.salt = 132
        self.hashedpassword = "has"
        self.cursor_obj.execute("""INSERT INTO USER(username, salt, hashedPassword) VALUES(?, ?, ?)""", (self.username,self.salt,self.hashedpassword))
          
        existing = self.cursor_obj.fetchone()

        if existing is None:
            self.cursor_obj.execute(
                "INSERT INTO USER(username, salt, hashedPassword) VALUES(?, ?, ?)",
                (self.username, self.salt, self.hashedpassword)
            )
            self.connect_db.commit()

        self.cursor_obj.execute("SELECT * FROM USER;")
        rows = self.cursor_obj.fetchall()
        for row in rows:
             print(row)
    
DatabaseManager()
