# python-sqlite-insert-benchmark

Result:

```
biasa elapsed time:      2.6661741733551025
bulk elapsed time:       1.5275776386260986
thread elapsed time:     23.03932785987854
process elapsed time:    <no result after more than several minutes, yield error after force-closed>


```

Error (multi-process):

```
Traceback (most recent call last):
    File "/home/gofrendi/anaconda3/lib/python3.7/multiprocessing/process.py", line 297, in _bootstrap
        self.run()
    File "/home/gofrendi/anaconda3/lib/python3.7/multiprocessing/process.py", line 99, in run
        self._target(*self._args, **self._kwargs)
    File "/home/gofrendi/anaconda3/lib/python3.7/concurrent/futures/process.py", line 233, in _process_worker
        call_item = call_queue.get(block=True)
    File "/home/gofrendi/anaconda3/lib/python3.7/multiprocessing/queues.py", line 94, in get
        res = self._recv_bytes()
    File "/home/gofrendi/anaconda3/lib/python3.7/multiprocessing/connection.py", line 216, in recv_bytes
        buf = self._recv_bytes(maxlength)
    File "/home/gofrendi/anaconda3/lib/python3.7/multiprocessing/connection.py", line 407, in _recv_bytes
        buf = self._recv(4)
    File "/home/gofrendi/anaconda3/lib/python3.7/multiprocessing/connection.py", line 379, in _recv
        chunk = read(handle, remaining)
KeyboardInterrupt
Exception in thread QueueManagerThread:
Traceback (most recent call last):
    File "/home/gofrendi/anaconda3/lib/python3.7/threading.py", line 926, in _bootstrap_inner
        self.run()
    File "/home/gofrendi/anaconda3/lib/python3.7/threading.py", line 870, in run
        self._target(*self._args, **self._kwargs)
    File "/home/gofrendi/anaconda3/lib/python3.7/concurrent/futures/process.py", line 392, in _queue_management_worker
    for work_id, work_item in pending_work_items.items():
RuntimeError: dictionary changed size during iteration

