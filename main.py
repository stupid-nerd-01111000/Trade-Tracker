from sqlite3 import connect, Error
from datetime import datetime


# --- Setup database ---
def setap_database():
    conn = connect('data_file.db')
    cursor = conn.cursor()

    # Create table for spot trades
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS spot_jornal (
            id INTEGER PRIMARY KEY,
            coin_symbol TEXT,
            entry_price INTEGER,
            quantity INTEGER,
            stop_loss_price INTEGER,
            entry_datetime DATE,
            FOREIGN KEY (coin_symbol) REFERENCES information (coin_symbol) ON DELETE CASCADE
        )
    ''')
    # Create table for information
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS information (
            id INTEGER PRIMARY KEY,
            coin_symbol TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()


# Add symbol name to the database
def add_coin_symbol(symbol_name):
    try:
        conn = connect('data_file.db')
        cursor = conn.cursor()

        # Add symbol
        cursor.execute('INSERT INTO information (coin_symbol) VALUES(?)', (symbol_name,))
        conn.commit()
        print(f'Symbol "{symbol_name}" added successfully.')

    except Error as e:
        print(f'We have an error: {e}')
    finally:
        if conn:
            conn.close()


# Add new spot position
def add_new_spot_position():
    try:
        conn = connect('data_file.db')
        cursor = conn.cursor()

        while True:
            coin_symbol = input('Enter the coin symbol (btc, eth):\n--> ').lower()

            # Checking the existence of the symbol in the information table
            cursor.execute('SELECT coin_symbol FROM information WHERE coin_symbol = ?', (coin_symbol,))
            result = cursor.fetchone()

            if result:
                # If symbol exists input information
                entry_price = float(input('Enter the entry price:\n--> '))
                quantity = float(input('Enter the quantity of coin:\n--> '))
                stop_loss_price = float(input('Enter the stop-loss price:\n--> '))
                entry_date = input('Enter the entry date (YYYY-MM-DD):\n--> ')

                # Check the date format
                try:
                    datetime.strptime(entry_date, '%Y-%m-%d')
                except ValueError:
                    print('Invalid date format. Please use YYYY-MM-DD.')
                    continue

                # Add new position in spot_jornal table
                cursor.execute('''
                    INSERT INTO spot_jornal (coin_symbol, entry_price, quantity, stop_loss_price, entry_datetime)
                    VALUES (?, ?, ?, ?, ?)
                ''', (coin_symbol, entry_price, quantity, stop_loss_price, entry_date))
                conn.commit()

                print(f'New spot position for "{coin_symbol}" added successfully.')
                break
            else:
                # If the coin is not found, show an error and provide the user with two options
                print(f'\nError: The coin symbol "{coin_symbol}" does not exist in the coin list.')
                print('''
1. Retry
2. Return to Main Menu
                ''')
                choice = input('Enter your choice:\n--> ').strip()
                if choice == '2':
                    print('Returning to main menu...')
                    break
                elif choice != '1':
                    print('Invalid choice. Returning to main menu...')
                    break

    except Error as e:
        print(f'We have an error: {e}')
    finally:
        if conn:
            conn.close()


# Main function
def main():
    setap_database()
    while True:
        print('''
0. Exit
1. Add new symbol
2. Add new spot position
        ''')
        choice = input('Enter your choice:\n--> ').strip()
        if choice == '0':
            print('Closing the program.')
            break
        elif choice == '1':
            symbol_name = input('Enter the symbol name you want to add:\n--> ').strip().lower()
            add_coin_symbol(symbol_name)
        elif choice == '2':
            add_new_spot_position()
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
