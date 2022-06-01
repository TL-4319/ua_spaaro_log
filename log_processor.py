import argparse
from datetime import datetime
import os

input_path = 'Desktop/bfs_log/'
mat_converter_path = 'Desktop/queso/spaaro/mat_converter/build'

#Parse inputs
parser = argparse.ArgumentParser(description = 'Automatically process bfs log files. Make sure to move the .bfs file from SD card to Desktop/bfs_log')
parser.add_argument ('input_name', metavar = 'file_name', type = str, help = 'Input log file name')
parser.add_argument ('vehicle',metavar = 'VEHICLE_NAME', type = str, help = 'The name of vehicle in upper case')

args = parser.parse_args()

# Prepare command to run mat converter
full_input_file = '~/'+input_path + args.input_name + '.bfs'
full_input_file_cmd = './mat_converter '+full_input_file

# Run ./mat_converter script
os.chdir("../..")
os.chdir(mat_converter_path)
os.system(full_input_file_cmd)


# Copy and replace output file with time_stamp name
os.chdir("../../../../..")
os.chdir(input_path)

now = datetime.now()
current_time = now.strftime("%Y%m%d-%H%M%S")
new_file_name = current_time+'.mat' 
full_output_file = '~/Documents/ua_spaaro_log/'+args.vehicle+'/'+new_file_name
copy_cmd = 'cp '+args.input_name+'.mat '+full_output_file

os.system(copy_cmd)

# Remove original .mat 
delete_cmd = 'rm '+args.input_name+'.mat'
os.system(delete_cmd)  

# Add new file to git
os.chdir("../..")
output_path = 'Documents/ua_spaaro_log/'+args.vehicle
os.chdir(output_path)
add_cmd = 'git add '+new_file_name
os.system(add_cmd)
