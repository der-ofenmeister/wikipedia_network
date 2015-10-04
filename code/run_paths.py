contents1 = """# This job needs 1 compute node with 1 processor per node.
#PBS -l nodes=1:ppn=1,pmem=8gb,pvmem=9gb
# It should be allowed to run for up to 6 hours.
#PBS -l walltime=06:00:00
# Name of job.
#PBS -N find_paths"""

contents2 =""" # Join STDERR TO STDOUT.  (omit this if you want separate STDOUT AND STDERR)
#PBS -j oe   
# Send me mail on job start, job end and if job aborts
#PBS -M mark.s.ibrahim@uvm.edu
#PBS -m bea

cd /users/m/s/msibrahi/v4/code/
echo "This is myjob running on " `hostname`
python find_paths.py """

import subprocess, os


log_path = "/users/m/s/msibrahi/v4/code/vacc_logs/"
os.chdir(log_path)
n = 112

for i in range(0, n):
    with open('wikijob'+str(i)+".script", "w") as f:
        f.write(contents1 + str(i) + "\n" + contents2 + str(i))

for i in range(0, n):
    command = "qsub wikijob" + str(i) + ".script" 
    subprocess.call(command, shell=True)
