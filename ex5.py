## Exercise 5.1
#with open("weather.csv", "r") as reader:   # open file
#    data = reader.read();                  # read file using read
#
#print(data);                               # print
#
## Exercise 5.2
#with open("weather.csv", "r") as reader:   # open file
#    line = reader.readline();              # read using readline
#    while line != "":                      # loop until empty string i.e. end of file
#        print(line);                       # print and read next line
#        line = reader.readline();
#
#print("It's over.");


## Exercise 5.3
#with open("weather.csv", "r") as reader:   # open file
#    line = reader.readline();              # read first line (header)
#    rain = [];
#    for line in reader.readlines():
#        print(line);
#        rain_data = float(line.split(",")[3]);   # split data by comma and extract final column, convert to float
#        rain.append(rain_data);                  # store in rain
#print(rain);
#
#with open("myrain.txt", "w") as writer:    # open an output file
#    for data in rain:
#        writer.write(str(data)+"\n");          # loop over data writing each point with newline char

# Exercise 5.4
import struct

bin_data = struct.pack("bbbb",123,12,45,34); # packing some data

with open("mybinary.dat", "wb") as writer:   # open binary file for writing
    writer.write(bin_data);                  # write the data

with open("mybinary.dat", "rb") as reader:
    bin_data2 = reader.read();               # read the data from the file

data = struct.unpack("bbbb",bin_data2);      # unpack it to check
print(data);


