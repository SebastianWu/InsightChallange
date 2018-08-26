actual_value_filename = "input/actual.txt"
predicted_value_filename = "input/predicted.txt"
window_size_filename = "input/window.txt"

class stock_value:
	def __init__(self, time, stock, price):
		self.time = time
		self.stock = stock
		self.price = price
	def printAll(self):
		print(str(self.time)+"|"+self.stock+"|"+str(self.price))

## read actual stock value
actual_value_file = open(actual_value_filename,"r")
actual_stock_value_list = []
actual_stock_value_unit_list = []
previous_time_stamp = 0
for line in actual_value_file:
	time,stock,price = line.rstrip("\n").split("|")
	if int(time) != previous_time_stamp:
		previous_time_stamp +=1
		if len(actual_stock_value_unit_list) != 0:
			actual_stock_value_list.append(actual_stock_value_unit_list)
		actual_stock_value_unit_list = []
		actual_stock_value_unit_list.append(stock_value(int(time),stock,float(price)))
	else:
		actual_stock_value_unit_list.append(stock_value(int(time),stock,float(price)))
actual_stock_value_list.append(actual_stock_value_unit_list)

##for unit_list in actual_stock_value_list:
##	for stock in unit_list:
##		stock.printAll()
##	print("\n")

## read predicted stock value
predicted_value_file = open(predicted_value_filename,"r")
predicted_stock_value_list = []
predicted_stock_value_unit_list = []
previous_time_stamp = 0
for line in predicted_value_file:
	time,stock,price = line.rstrip("\n").split("|")
	if int(time) != previous_time_stamp:
		previous_time_stamp +=1
		if len(predicted_stock_value_unit_list) != 0:
			predicted_stock_value_list.append(predicted_stock_value_unit_list)
		predicted_stock_value_unit_list = []
		predicted_stock_value_unit_list.append(stock_value(int(time),stock,float(price)))
	else:
		predicted_stock_value_unit_list.append(stock_value(int(time),stock,float(price)))
predicted_stock_value_list.append(predicted_stock_value_unit_list)

##for unit_list in predicted_stock_value_list:
##	for stock in unit_list:
##		stock.printAll()
##	print("\n")

## read window size
window_size = int(open(window_size_filename,"r").readline().rstrip("\n"))

f = open("insight_testsuite/temp/output/comparison.txt","w")
sliding_window_initial_time_stamp = 1
sliding_window_length = actual_stock_value_list[-1][-1].time-window_size+1
while(sliding_window_initial_time_stamp < sliding_window_length+1):
	error = 0.0
	num = 0
	for i in range(sliding_window_initial_time_stamp-1,sliding_window_initial_time_stamp+window_size-1):
		for actual_stock_value in actual_stock_value_list[i]:
			for predicted_stock_value in predicted_stock_value_list[i]:
				if actual_stock_value.stock == predicted_stock_value.stock:
					##print(str(actual_stock_value.time)+" "+actual_stock_value.stock+" "+str(actual_stock_value.price)+" "+str(predicted_stock_value.price))
					error += abs(actual_stock_value.price-predicted_stock_value.price)
					num+=1
					break
	print(str(sliding_window_initial_time_stamp)+"|"+str(sliding_window_initial_time_stamp+window_size-1)+"|"+"{0:.2f}".format(error/num))
	f.write(str(sliding_window_initial_time_stamp)+"|"+str(sliding_window_initial_time_stamp+window_size-1)+"|"+"{0:.2f}".format(error/num)+"\n")
	##+str(round(error/num,2))
	##print("{0:.2f}".format(error/num))
	sliding_window_initial_time_stamp+=1





### method 1
##### read actual stock value
###actual_value_file = open(actual_value_filename,"r")
###actual_stock_value_list = []
###for line in actual_value_file:
###	time,stock,price = line.rstrip("\n").split("|")
###	actual_stock_value_list.append(stock_value(int(time),stock,float(price)))

###### test print
####print("actual stock value")
####for stock in actual_stock_value_list:
####	stock.printAll()

##### read predicted stock value
###predicted_value_file = open(predicted_value_filename,"r")
###predicted_stock_value_list = []
###for line in predicted_value_file:
###	time,stock,price = line.rstrip("\n").split("|")
###	predicted_stock_value_list.append(stock_value(int(time),stock,float(price)))

###### test print
####print("predict stock value")
####for stock in predicted_stock_value_list:
####	stock.printAll()

##### read window size
###window_size = int(open(window_size_filename,"r").readline().rstrip("\n"))

###### test print
####print("window size: "+str(window_size))

###sliding_window_length = actual_stock_value_list[-1].time-window_size+1

###sliding_window_initial_time_stamp = 1
###while(sliding_window_initial_time_stamp < sliding_window_length):
###	error = 0.0
###	num = 0
###	for i in range(sliding_window_initial_time_stamp, sliding_window_initial_time_stamp+window_size):
###		for actual_stock_value in actual_stock_value_list:
###			if actual_stock_value.time == i :
###				for predicted_stock_value in predicted_stock_value_list:
###					if predicted_stock_value.time == i and predicted_stock_value.stock == actual_stock_value.stock:
###						#print(str(i)+" "+actual_stock_value.stock+" "+str(actual_stock_value.price)+" "+str(predicted_stock_value.price))
###						error = error+abs(actual_stock_value.price - predicted_stock_value.price)
###						num +=1
###					if predicted_stock_value.time > (sliding_window_initial_time_stamp+window_size):
###						break
###	print(str(sliding_window_initial_time_stamp)+"|"+str(sliding_window_initial_time_stamp+window_size-1)+"|"+str(error/num))
###	sliding_window_initial_time_stamp += 1



