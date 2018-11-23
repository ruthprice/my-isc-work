import serial
from datetime import datetime
import io

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii', newline='\r')
sio._CHUNK_SIZE = 1

output_file = "temp_output.tsv"

with open(output_file, "a") as writefile:
    while ser.isOpen():
        datastring = sio.readline()
        writefile.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n')
        writefile.flush()

ser.close()


