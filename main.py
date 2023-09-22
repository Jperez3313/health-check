import psutil
import logging
import shutil
from colorama import Fore

intWarning = 0

# Set up logs
def log_setup():
    logging.basicConfig(filename='health_check.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Check CPU Usage
def cpu_usage(threshold=80):
    logical_cores = psutil.cpu_count(logical=True)
    fCurrent = (psutil.cpu_percent(interval=5) * 100) / logical_cores
    if fCurrent > threshold:
        logging.warning("CPU Usage: Warning CPU usage is at" + str(fCurrent))
        print(Fore.RED + "Warning: Check Log")
        global intWarning
        intWarning += 1 
    else:
        print(Fore.GREEN + "CPU Usage: Okay")
        print(fCurrent)
        print("-----------------------")

# Check Disk Space
def disk_space(threshold_gb=20):
    try:
        total, used, free = shutil.disk_usage("/")
        total_gb = round(total / (2**30), 2)
        used_gb = round(used / (2**30), 2)
        free_gb = round(free / (2**30), 2)
        if free_gb < threshold_gb:
            logging.warning("Warning: Free disk space is below the threshold", threshold_gb)
            print(Fore.RED + "Warning: Check Log")
            logging.warning("Total:" + str(total_gb) + "Used:" + str(used_gb) + "Free:" + str(free_gb))
            global intWarning
            intWarning += 1 
        else:
            print(Fore.GREEN + "Disk Space: Okay") 
            print("Total: " + str(total_gb) + "GiB")
            print("Used: " + str(used_gb) + "GiB")
            print("Free: " + str(free_gb) + "GiB")
            print("-----------------------")
    except Exception as e:
        logging.error("Error while checking disk space: %s", str(e))

def main():
    print("Starting Health Check")
    log_setup()
    cpu_usage()
    disk_space()
    if intWarning >= 1:
        print(Fore.RED + "YOU HAVE ERRORS PLEASE CHECK LOG ")
    else: 
        print(Fore.GREEN + "Your system is healthy")
    print("Health Check Complete")
main()
