import sys

actual_value_filename = sys.argv[1] ## "/Users/sebastianwu/Desktop/InsightChallange/input/actual.txt"
predicted_value_filename = sys.argv[2] ## "/Users/sebastianwu/Desktop/InsightChallange/input/predicted.txt"
window_size_filename = sys.argv[3] ## "/Users/sebastianwu/Desktop/InsightChallange/input/window.txt"

class stock_value:
	def __init__(self, time, stock, price):
		self.time = time
		self.stock = stock
		self.price = price
	def printAll(self):
		print(str(self.time)+"|"+self.stock+"|"+str(self.price))

## read actual stock value
actual_value_file = open(actual_value_filename,"r")
actual_stock_value_dict = {}
actual_stock_value_unit_list = []
previous_time_stamp = 0
for line in actual_value_file:
	time,stock,price = line.rstrip("\n").split("|")
	if int(time) != previous_time_stamp:
		actual_stock_value_dict[previous_time_stamp] = actual_stock_value_unit_list
		previous_time_stamp = int(time)
		actual_stock_value_unit_list = []
		actual_stock_value_unit_list.append(stock_value(int(time),stock,float(price)))
	else:
		actual_stock_value_unit_list.append(stock_value(int(time),stock,float(price)))
actual_stock_value_dict[previous_time_stamp] = actual_stock_value_unit_list


## read predicted stock value
predicted_value_file = open(predicted_value_filename,"r")
predicted_stock_value_dict = {}
predicted_stock_value_unit_list = []
previous_time_stamp = 0
for line in predicted_value_file:
	time,stock,price = line.rstrip("\n").split("|")
	if int(time) != previous_time_stamp:
		predicted_stock_value_dict[previous_time_stamp] = predicted_stock_value_unit_list
		previous_time_stamp = int(time)
		predicted_stock_value_unit_list = []
		predicted_stock_value_unit_list.append(stock_value(int(time),stock,float(price)))
	else:
		predicted_stock_value_unit_list.append(stock_value(int(time),stock,float(price)))
predicted_stock_value_dict[previous_time_stamp] = predicted_stock_value_unit_list


## read window size
window_size = int(open(window_size_filename,"r").readline().rstrip("\n"))

f = open("/Users/sebastianwu/Desktop/prediction-validation-master/insight_testsuite/temp/output/comparison.txt","w")
sliding_window_initial_time_stamp = 1
sliding_window_length = int(max(actual_stock_value_dict, key = int))-window_size+1
while(sliding_window_initial_time_stamp < sliding_window_length+1):
	error = 0.0
	num = 0
	for i in range(sliding_window_initial_time_stamp,sliding_window_initial_time_stamp+window_size):
		if i not in predicted_stock_value_dict.keys():
			break
		for predicted_stock_value in predicted_stock_value_dict[i]:
			for actual_stock_value in actual_stock_value_dict[i]:
				if actual_stock_value.stock == predicted_stock_value.stock:
					##print(str(actual_stock_value.time)+" "+actual_stock_value.stock+" "+str(actual_stock_value.price)+" "+str(predicted_stock_value.price))
					error += abs(actual_stock_value.price-predicted_stock_value.price)
					num+=1
					break
	if num != 0:
		##print(str(sliding_window_initial_time_stamp)+"|"+str(sliding_window_initial_time_stamp+window_size-1)+"|"+"{0:.2f}".format(error/num))
		f.write(str(sliding_window_initial_time_stamp)+"|"+str(sliding_window_initial_time_stamp+window_size-1)+"|"+"{0:.2f}".format(error/num)+"\n")
	else:
		##print(str(sliding_window_initial_time_stamp)+"|"+str(sliding_window_initial_time_stamp+window_size-1)+"|"+"NA\n")
		f.write(str(sliding_window_initial_time_stamp)+"|"+str(sliding_window_initial_time_stamp+window_size-1)+"|"+"NA\n")
	sliding_window_initial_time_stamp+=1




