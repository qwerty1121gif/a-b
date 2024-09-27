input_data = open('input.txt', 'r')
data = input_data.read()

k = int(data)
ans = str((100*k)+(90)+(9-k))

output_data = open('output.txt', 'w')
output_data.write(ans)

input_data.close()
output_data.close()