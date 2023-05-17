from functools import reduce

from files import *
number_data_file = "number-data.txt"
mean_data_file = "mean-data.txt"

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_list = [str(number) for number in number_list]

# calls function that writes list to txt file
write_data_to_file(" ".join(number_list), number_data_file)

# calls function that reads txt file. it gets numbers from txt file
new_number_list = " ".join(read_file_data(number_data_file)).split()

# this line calculates average of number list
mean_value = reduce(lambda x, y: int(x) + int(y), new_number_list) / len(new_number_list)

# writes average value to the text file/mean-data.txt
write_data_to_file(mean_value,mean_data_file)

# prints result to console
print(f" average of numbers ({number_list}) is {mean_value}")