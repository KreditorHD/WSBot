import rpi

#All stocks that are tested with the number of mentions
#TODO Get out of SQL
stocks = {}
with open("stocks.txt", "r") as f:
    for stock in f.read().split(","):
        stocks[stock] = 0
        stocks['$' + stock] = 0

#All Submissions to Scan
#TODO make customizable
rpi.getSubmissions(10)
rpi.getSubmissions(10,"rising")
rpi.getSubmissions(10,"top")

#All Submission Objects
allEntries = rpi.getEntries()

#Get mentions of each stock
for stock in stocks.keys():
    for entrie in allEntries:
        importantText = (entrie.getTitle() + entrie.getText()).split(" ")
        if importantText.__contains__(stock):
            if stock.__contains__("$"):
                #+1 in SQL 
                stocks[stock.replace("$","")] += 1
            else:
                #+1 in SQL
                stocks[stock] += 1

#Print out all mentioned stocks
for stock in stocks.keys():
    if stocks[stock] != 0:
        print(stock + ": " + str(stocks[stock]))




