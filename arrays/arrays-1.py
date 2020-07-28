expenses = [2200,2350,2600,2130,2190]
juneExpense = [1980]
expenseWithJune = expenses + juneExpense
location = []
correctedExpenses = []
extraSpentInFebComparedToJan = expenses[1] - expenses[0]
totalExpenseInFirstQuarter = 0
for i in range(len(expenses)-2):
    totalExpenseInFirstQuarter = totalExpenseInFirstQuarter + expenses[i]

#locate the month with 2000 expenses
for i in range(len(expenses)):
    if expenses[i]==2000:
        location.append(i)
    else:
        pass     

#actual number of the month
actualLocation = []
for value in location:
    actualLocation.append(value+1)

#correction in month of april. adding 200$
for i in range(len(expenses)):
    if i == 3:
        correctedExpenses.append(expenses[i] + 200)
    else:
        correctedExpenses.append(expenses[i])

print('Extra spent in feb wrt jan :', extraSpentInFebComparedToJan)
print('Total expense in first quarter : ', totalExpenseInFirstQuarter)
if len(actualLocation)>1:
    print('2000 was spent in months : ', actualLocation)
else:
    print('2000 was not spent in any month.')
print('expenses with 1980 (june) : ',(expenseWithJune))
print('expenses with corrected april expense : ' + correctedExpenses)

