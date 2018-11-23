import time
from netCDF4 import Dataset
from datetime import datetime, timedelta
import numpy as np
from csv import reader

def convert_time(tm):
    tm = datetime.strptime(tm, "%Y-%m-%dT%H:%M:%S.%f")
    return tm

def cels_to_kelv(t_C):
    t_K = float(t_C) + 273.15
    return t_K

input_filename = "temp_output.tsv"

temps = []
times = []

with open(input_filename, "r") as csvfile:
    csvreader = reader(csvfile, delimiter="\t")
    for line in csvreader:
        times.append(convert_time(line[0]))
        line[1] = line[1][1:-1]                   # remove '+' from beginning and 'C' from end
        temps.append(cels_to_kelv(line[1]))

# Set reference time and convert datetime values to offset values from reference time
#reference time is the first time in the input data
base_time = times[0]
time_values = []

for t in times:
    value = t - base_time
    ts = value.total_seconds()
    time_values.append(ts)

time_units = "seconds since " + base_time.strftime('%Y-%m-%d %H:%M:%S')

# Create the output file (NetCDF dataset)
output_file = "sensor_data.nc"
dataset = Dataset(output_file, "w", format='NETCDF4_CLASSIC')

# Create the time dimension - with unlimited length
time_dim = dataset.createDimension("time", None)

# Create the time variable
time_var = dataset.createVariable("time", np.float64, ("time",))
time_var[:] = time_values
time_var.units = time_units
time_var.standard_name = "time"
time_var.calendar = "standard"

# Create the temp variable
temp = dataset.createVariable("temp", np.float32, ("time",))
temp[:] = temps

#  Set   the   variable attributes
temp.var_id =  "temp"   
temp.long_name =  "Temperature   of sensor   (K)"  
temp.units  =  "K"   
temp.standard_name   =  "air_temperature" 
#  Set   the   global   attributes
dataset.Conventions  =  "CF-1.6" 
dataset.institution  =  "NCAS"   
dataset.title  =  "My   first CF-netCDF   file" 
dataset.history   =  "%s:  Written  with  script:  temp_file_reader.py"  %  (datetime.now().strftime("%x  %X"))

# Write the file
dataset.close()

print("Wrote: %s" % output_file)
print("Try: ncdump %s" % output_file)


