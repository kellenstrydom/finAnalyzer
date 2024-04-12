import unittest
from io import StringIO

# FinancialTransaction class allows for the program to read FinancialTransaction data found in test setUp and main below.
# This class does not need to be edited
class FinancialTransaction:
    def __init__(self, date, type, amount):
        self.date = date
        self.type = type
        self.amount = amount

    @staticmethod
    def from_line(line):
        parts = line.strip().split(',')
        date, type, amount = parts[0], parts[1], float(parts[2])
        return FinancialTransaction(date, type, amount)

class FinancialHealthAnalyzer:
    def __init__(self, transactions):
        self.transactions = transactions

    #Adds together all transactions labeled "Income"
    def total_revenue(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.type == "Income")

    #Adds together all transactions labeled "Expense"
    def total_expenses(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.type == "Expense")

    #Difference between revenue and expenses
    def profit(self):
        return (self.total_revenue() - self.total_expenses())

    #Divideds profit by revenue
    def profit_margin(self):
        return(self.profit() / self.total_revenue())

    #Divides the profit by the number of transactions
    def average_transaction_amount(self):
        #Average transaction amount = (total revenue - total expenses) / amount of transactions
        return (self.profit() / len(self.transactions))

    #Determines finalncial health and returns the corresponding string
    #i fixed this
    #now warning and critical return correctly
    def financial_health(self):
        profit = self.profit()
        if profit >= 0:
            return "Healthy"
        elif profit >= -1000:
            return "Warning"
        else:
            return "Critical"

class TestFinancialHealthAnalyzer(unittest.TestCase):
    #Setup data allows for code to be tested without manually writing test transaction code for every test function. 
    #setUp transaction data and structure may be changed to include more test functions.
    def setUp(self):
        #healthy test case values
        transactions_data_healthy = [
            FinancialTransaction("2024-01-01", "Income", 1000),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 1500)
        ]
        #self.transactions_healthy = transactions_data
        self.analyzer_healthy = FinancialHealthAnalyzer(transactions_data_healthy)

        #warning test case values
        transactions_data_warning = [
            FinancialTransaction("2024-01-01", "Income", 60),
            FinancialTransaction("2024-01-02", "Expense", 200),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 200)
        ]
        #self.transactions_warning = transactions_data
        self.analyzer_warning = FinancialHealthAnalyzer(transactions_data_warning)

        #critical test case values
        transactions_data_critical = [
            FinancialTransaction("2024-01-01", "Income", 50),
            FinancialTransaction("2024-01-02", "Expense", 1000),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 150)
        ]
        #self.transactions_critical = transactions_data
        self.analyzer_critical = FinancialHealthAnalyzer(transactions_data_critical)


    #Test case example that returns total revenue. Inluded as a tutorial for basis of other test cases.
    def test_total_revenue(self):
        #analyzer = FinancialHealthAnalyzer(self.transactions_healthy)
        self.assertEqual(self.analyzer_healthy.total_revenue(), 2500)
        self.assertEqual(self.analyzer_warning.total_revenue(), 260)
        self.assertEqual(self.analyzer_critical.total_revenue(), 200)

    #Tests total expenses for test cases
    def test_total_expenses(self):
        #analyzer = FinancialHealthAnalyzer(self.transactions_healthy)
        self.assertEqual(self.analyzer_healthy.total_expenses(), 800)
        self.assertEqual(self.analyzer_warning.total_expenses(), 500)
        self.assertEqual(self.analyzer_critical.total_expenses(), 1300)

    #tests profit for test cases
    def test_profit(self):
        #analyzer = FinancialHealthAnalyzer(self.transactions_healthy)
        self.assertEqual(self.analyzer_healthy.profit(), 1700)
        self.assertEqual(self.analyzer_warning.profit(), -240)
        self.assertEqual(self.analyzer_critical.profit(), -1100)

    #tests profit margin for test cases
    def test_profit_margin(self):
        #analyzer = FinancialHealthAnalyzer(self.transactions_healthy)
        self.assertEqual(self.analyzer_healthy.profit_margin(), 1700/2500)
        self.assertEqual(self.analyzer_warning.profit_margin(), -240/260)
        self.assertEqual(self.analyzer_critical.profit_margin(), -1100/200)

    #tests average transactions amount for test cases
    def test_average_transaction_amount(self):
        self.assertEqual(self.analyzer_healthy.average_transaction_amount(), 1700/4)
        self.assertEqual(self.analyzer_warning.average_transaction_amount(), -240/4)
        self.assertEqual(self.analyzer_critical.average_transaction_amount(), -1100/4)

    #tests finacial health output for the test cases
    def test_financial_health(self):
        self.assertEqual(self.analyzer_healthy.financial_health(), "Healthy")
        self.assertEqual(self.analyzer_warning.financial_health(), "Warning")
        self.assertEqual(self.analyzer_critical.financial_health(), "Critical")

    #Additional testing methods might be required. test_total_revenue can be changed/expanded

#Main function is where your code starts to run. Methods need to be compiled correctly before they can be called from main
if __name__ == '__main__':
    #Do not change the transaction data, this data needs to produce the correct output stated in the lab brief
    transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 50),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 75)
        ]
    #initialise class
    FinancialHealthAnalyzer.transactions = transactions_data
    analyzer = FinancialHealthAnalyzer(FinancialHealthAnalyzer.transactions)

    #print output
    print("Profit: " + str(analyzer.profit()))
    print("Profit margin: " + str(analyzer.profit_margin()))
    print("Average transaction amount: " + str(analyzer.average_transaction_amount()))
    print("Financial health: " + str(analyzer.financial_health()))
    unittest.main()
