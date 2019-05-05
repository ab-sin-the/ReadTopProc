__author__ = 'Yiwen Chen'

from bean import Bean
from store import db

class TopProcRecorder(Bean):
    _tbl = 'top_proc'
    _cols = 'id, rank, procname, pid, user, cpu_usage, mem_usage, datatime'

    def __init__(self, _id, rank, procname, pid, user, cpu_usage, mem_usage, datatime):
        self.id = _id
        self.rank = rank
        self.procname = procname
        self.pid = pid
        self.user = user
        self.cpu_usage = cpu_usage
        self.mem_usage = mem_usage
        self.datatime = datatime
        
