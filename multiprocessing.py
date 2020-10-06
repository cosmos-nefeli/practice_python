from multiprocessing import Process, Queue
#from Queue import Queue
import time

def restore_backup(command):
    print(command)  # you will see that there is gap
    time.sleep(5)
    print("hello")
    return True

def to_do(my_queue, result_queue):
    while not my_queue.empty():
        command = my_queue.get()
        output = restore_backup(command)
        result_queue.put(output)
        time.sleep(1)

def main():
    my_queue = Queue()
    result_queue = Queue()
    result = [] # This is result
    processes = []
    for i in range(10):
        my_queue.put("backup_command_py"+ str(i)) #Put all the command in queue
    
    for _ in range(0,5):
        p = Process(target=to_do,args=(my_queue,result_queue))
        processes.append(p)
        p.start()

    ##print("Finished starting all processes")

    for p in processes:
        p.join()
    
    while not result_queue.empty():
        result.append(result_queue.get())
    
    print(result)

if __name__ == "__main__":
    main()
