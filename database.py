import pandas as pd

class CSVAssistant:
    def __init__(self, file_path):
        try:
            self.df = pd.read_csv(file_path)
            print("\nCSV file loaded successfully!\n")
            print("First 5 rows of the dataset:\n")
            print(self.df.head())
        except Exception as e:
            print(f"Error loading file: {e}")
            self.df = None

    def get_columns(self):
        if self.df is not None:
            print("\nAvailable columns:\n")
            print(list(self.df.columns))
        else:
            print("\nNo data loaded.\n")

    def display_rows(self):
        if self.df is not None:
            try:
                num_rows = int(input("Enter the number of rows to display: "))
                print("\nDisplaying rows:\n")
                print(self.df.head(num_rows))
            except ValueError:
                print("\nInvalid input. Please enter a valid number.\n")
        else:
            print("\nNo data available to display.\n")

    def query_data(self):
        if self.df is None:
            print("\nNo data available to query.\n")
            return

        while True:
            print("\n--- Data Query Options ---")
            # print("1. View rows by condition")
            print("1. Sort data by a column")
            print("2. Display summary statistics")
            print("3. Get row by index")
            print("4. Exit query mode")

            choice = input("Enter your choice (1-4): ")

            # if choice == '1':
            #     column = input("Enter the column name to filter by: ")
            #     condition = input(f"Enter the condition (e.g., {column} > 10): ")

            #     try:
            #         result = self.df.query(condition)
            #         print("\nQuery Result:\n")
            #         print(result)
            #     except Exception as e:
            #         print(f"Error: {e}")

            if choice == '1':
                column = input("Enter the column name to sort by: ")
                order = input("Enter 'asc' for ascending or 'desc' for descending: ")

                try:
                    ascending = True if order.lower() == 'asc' else False
                    sorted_df = self.df.sort_values(by=column, ascending=ascending)
                    print("\nSorted Data:\n")
                    print(sorted_df.head(50))
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == '2':
                print("\nSummary Statistics:\n")
                print(self.df.describe())

            elif choice == '3':
                try:
                    index = int(input("Enter the row index to retrieve: "))
                    print("\nRow Data:\n")
                    print(self.df.iloc[index])
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == '4':
                print("\nExiting query mode.\n")
                break

            else:
                print("\nInvalid choice. Please try again.\n")


def database():
    file_path = input("Enter the path to the CSV file: ")
    assistant = CSVAssistant(file_path)

    while True:
        print("\n--- Main Menu ---")
        print("1. Display columns")
        print("2. Display rows")
        print("3. Query data")
        print("4. Exit")

        option = input("Enter your choice (1-4): ")

        if option == '1':
            assistant.get_columns()
        elif option == '2':
            assistant.display_rows()
        elif option == '3':
            assistant.query_data()
        elif option == '4':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    database()
