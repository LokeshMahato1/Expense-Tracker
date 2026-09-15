import csv
from Models.expense import Expenses

class CSVManager:

    def __init__(self,filename="expenses.csv"):
        self.filename=filename

    def save(self, expenses):
        with open(self.filename
                  ,"w",
                  newline="") as file:
            
            writer=csv.writer(file)

            writer.writerow([
                "Category",
                "Amount",
                "Description",
                "Method",
                "TXN ID",
                "Date"
            ])

            for expense in expenses:
                writer.writerow([
                    expense.category,
                    expense.amount,
                    expense.description,
                    expense.method,
                    expense.txn_id,
                    expense.date
                ])


    def load(self):
        expenses=[]

        try:
            with open(
                self.filename,
                "r",
                newline=""
            ) as file:

                reader=csv.DictReader(file)

                for row in reader:
                    expense=Expenses(
                        category=row["Category"],
                        amount=float(row["Amount"]),
                        description=row["Description"],
                        method=row["Method"],
                        txn_id=row["TXN ID"],
                        date=row["Date"]
                    )

                    expenses.append(expense)
        except FileNotFoundError:
            pass

        return expenses


    

    