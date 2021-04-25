import os
import csv

file = os.path.join('..', 'Resources', 'budget_data.csv')

with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
   
    month_count = []
    profit = []
    change_profit = []
    
                      
    
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      

increase = max(change_profit)
decrease = min(change_profit)

month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1
