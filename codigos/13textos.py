def process_data_file(input_file, output_file):
    counter = 0
    for line in input_file:
        counter = counter + int(line)
    output_file.write(str(counter))
input_file = open("input.txt")
output_file = open("output.txt", "w")
process_data_file(input_file, output_file)
input_file.close()
output_file.close()