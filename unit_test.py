import analysis as AN
import interface
import importing as IP
import expense_tracker
import openpyxl


my_import = IP.Import("expensetracker.xlsx")
my_analyze = AN.Analyze(my_import.examine_data())

#1 Test the importing success or not 
assert my_import.file.cell(row = 1, column = 1).value == \
    "Emma's Expense Tracker" , "The Import Unsucess"

#2 Test the data are saving correctly in dictionary
assert my_import.examine_data()["Company Name"] ==\
    ['Verizon', 'Bank of America', 'Target', 'Nordstrom', 'Shell Feul', 'Allstate Insurance'],\
    "The Data Saving Incorrect"

#3 Test company function in Analyze
my_comp = my_analyze.company()
assert my_comp[0] == 'Verizon -- Checking',\
    "The Company Function Is Not Working"

#4 Test sum total amount due function in Analyze
my_total = my_analyze.sum_total_amount()
assert my_total == 999.99 , \
    "The Sum Total Is Wrong"

#5 Test sum monthly budget in Analyze
my_bud = my_analyze.sum_monthly_budget()
assert my_bud == 3035, \
    "The Monthly Budget Is Wrong"

#6 Test the account type in Analyze
my_account = my_analyze.account()
assert my_account == 'Checking, Savings' ,\
    "The Account Type Is Wrong"

#7 Test the button feauture in Interface
my_button = my_interface.button()
assert my_button == 'Button'
    "The Button Does Not Work"

print("Passed all tests")

