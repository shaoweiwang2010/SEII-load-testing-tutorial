import psutil
import subprocess 
import time

perf_log = "./perfcounter.csv"


def get_pid(process_name):
    cmd = "ps aux | grep '%s' | grep -v grep" % process_name
    info = subprocess.getoutput(cmd)

    processes = info.split('\n')
    for process in processes:
        process_id = process.split()[1]
        return process_id  # return process id
    return -1


def perf(process_id):
    print(process_id)

    psutil_capture_pid = psutil.Process(process_id)
    
    psutil_capture_pid.memory_percent()

    with open(perf_log, 'a') as f:
        while True:
            print("listening...")
            record  = str(psutil_capture_pid.io_counters())  + ',' + str(  psutil_capture_pid.memory_percent()) + ','+ str(psutil_capture_pid.cpu_percent(interval=1)) + '\n'
            f.write(record)
            print(record)
            time.sleep(5)


if __name__ == "__main__":
    process_name = "openmrs-standalone.jar"

    pid = get_pid(process_name)

 #hard code for windows
    perf(27104)
