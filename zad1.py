input_data = open('input.txt', 'r')
data = input_data.read()

data = data.split()
c = str(int(data(0)) + int(data(1)))
output_data = open('output.txt', 'w')
output_data.write(c)

input_data.close()
output_data.close()