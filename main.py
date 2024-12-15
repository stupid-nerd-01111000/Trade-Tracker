from sqlite3 import connect, Error


# ---setap database---
def setap_database():
    conn = connect('data_file.db')
    cursor = conn.cursor()
    #create table for spot trades
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS spot_jornal (
            id INTEGER PRIMARY KEY,
            coin_symbol TEXT,
            entry_price INTEGER,
            stop_loss INTEGER
            )
    ''')
    #create table for information
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS information (
            id INTEGER PRIMARY KEY,
            coin_symbol TEXT
            )
    ''')
    conn.commit()
    conn.close()



#add symbol name to the database
def add_coin_symbol(symbol_name):
    try:
        conn = connect('data_file.db')
        cursor = conn.cursor()
        #add_symbol
        cursor.execute('INSERT INTO information (coin_symbol) VALUES(?)', (symbol_name, ))
        conn.commit()
        print(f'Symbol "{symbol_name}" added successfully.')
    except Error as e:
        print(f'We have error {e}')
    finally:
        if conn:
            conn.close()

def main():
    setap_database()
    while True:
        print('''
0. Exit
1. Add new symbol
        ''')
        choice = input('Enter your choice :\n--> ')
        if choice == '0':
            print('Closing the program.')
            break
        elif choice == '1':
            symbol_name = input('Enter the symbol name you want to added :\n--> ')
            add_coin_symbol(symbol_name.lower())




if __name__ == '__main__':
    main()
