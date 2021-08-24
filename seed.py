import sqlite3

connection = sqlite3.connect('flask_app.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        username,
        password, 
        favorite_color 
        )VALUES(
            'Samuel',
            'Opare',
            'Black'    
        );"""

)


cursor.execute(
    """INSERT INTO users(
        username,
        password, 
        favorite_color 
        )VALUES(
            'Ironman',
            'Tony',
            'Gold'    
        );"""

)

connection.commit()
cursor.close()
connection.close()