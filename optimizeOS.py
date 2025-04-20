"""
    Class:   CS-510
    Author:  Andrea Carter
    Date:    April 17

    Description:  Each function that needs to be completed has a comment at the top with
                  TODO written in it with instructions.

                  Within the function is a section with the comment #TODO where you will
                  insert your code as per the instructions.
"""  
import os
import psutil  # requires pip install
import sys
import threading

"""
  Three provided Utility functions to use
"""
def printBlankLines(lines: int):
    for i in range(lines):
        print("")

def printMsg1(num):
    print("Thread 1 cubed: {}" .format(num * num * num))


def printMsg2(num):
    print("Thread 2 squared: {}" .format(num * num))


"""
   TODO This function will display information about a file, size and file information.
   You can provide your own or use the projecttwo.txt file.

   Use psutil to get initial file information.
"""
def getFileDiskUsageStatistics() -> None:
    print("Getting Disk Statistics")
    file_name = "./projecttwo.txt"

    # Check if file exists
    if not os.path.exists(file_name):
        print(f"File {file_name} does not exist.")
        printBlankLines(2)
        return

    # Get file size and disk usage
    try:
        file_stats = os.stat(file_name)
        disk_usage = psutil.disk_usage(os.path.dirname(file_name))

        print(f"File Name: {file_name}")
        print(f"File Size: {file_stats.st_size} bytes")
        print(f"Total Disk Space: {disk_usage.total / (1024**3):.2f} GB")
        print(f"Used Disk Space: {disk_usage.used / (1024**3):.2f} GB")
        print(f"Free Disk Space: {disk_usage.free / (1024**3):.2f} GB")
    except Exception as e:
        print(f"Error retrieving disk statistics: {e}")

    printBlankLines(2)

"""
   TODO This should use psutil to retrieve standard and 
   virtual memory statistics
"""
def getMemoryStatistics() -> None:
    print("Getting Memory Statistics")

    try:
        virtual_memory = psutil.virtual_memory()
        swap_memory = psutil.swap_memory()

        print(f"Total Memory: {virtual_memory.total / (1024**3):.2f} GB")
        print(f"Available Memory: {virtual_memory.available / (1024**3):.2f} GB")
        print(f"Used Memory: {virtual_memory.used / (1024**3):.2f} GB")
        print(f"Memory Usage Percentage: {virtual_memory.percent}%")

        print(f"Total Swap: {swap_memory.total / (1024**3):.2f} GB")
        print(f"Used Swap: {swap_memory.used / (1024**3):.2f} GB")
        print(f"Free Swap: {swap_memory.free / (1024**3):.2f} GB")
        print(f"Swap Usage Percentage: {swap_memory.percent}%")
    except Exception as e:
        print(f"Error retrieving memory statistics: {e}")

    printBlankLines(2)

"""
   TODO This should use psutil to retrieve CPU statistics, including
   information on processes.
"""
def getCpuStatistics() -> None:
    print("Getting CPU Statistics")
    
    try:
        cpu_times = psutil.cpu_times()
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count(logical=True)

        print(f"CPU Times: {cpu_times}")
        print(f"CPU Usage Percentage: {cpu_percent}%")
        print(f"Number of Logical CPUs: {cpu_count}")

        # Display top 5 processes by CPU usage
        processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']), key=lambda p: p.info['cpu_percent'], reverse=True)[:5]
        print("\nTop 5 Processes by CPU Usage:")
        for proc in processes:
            print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, CPU Percent: {proc.info['cpu_percent']}%")
    except Exception as e:
        print(f"Error retrieving CPU statistics: {e}")

    printBlankLines(2)

"""
   TODO This function will show multi threading capabilities.

   Two threads should be created.
    
   One used to call the function "printMsg1" provided above.

   A second thread should call the function "printMsg2" provided above.
"""
def showThreadingExample() -> None:
    print("Demonstrating Threading")
   
    try:
        # Create threads
        thread1 = threading.Thread(target=printMsg1, args=(3,))
        thread2 = threading.Thread(target=printMsg2, args=(4,))

        # Start threads
        thread1.start()
        thread2.start()

        # Wait for threads to complete
        thread1.join()
        thread2.join()
    except Exception as e:
        print(f"Error demonstrating threading: {e}")

    print("Done With Threading!")

    printBlankLines(2)

"""
   TODO This function shows system error handling.

   Since out of memory, or out of disk space errors are difficult to create,
   we will use a divide by zero error and show the error handling being executed.
"""
def showErrorHandling() -> None:
    print("Demonstrating Error Handling")
    try:
        # Cause a divide by zero error
        res = 1 / 0
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except MemoryError:
        print("Memory Error!")
    else:
        print("Result is", res)
    finally:
        print("Execution complete.")

    printBlankLines(2)

"""
   Main function, does not require modification.

   This calls the specific functions.
"""
def main() -> int:
    print("Starting Program")
    print("=============================")
   
    getFileDiskUsageStatistics()   
    
    getCpuStatistics()
    
    getMemoryStatistics()

    showThreadingExample()

    showErrorHandling()


if __name__ == '__main__':
    sys.exit(main()) 
