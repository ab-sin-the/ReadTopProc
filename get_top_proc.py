import os
import datetime
from top_proc_recorder import TopProcRecorder

def get_process_info(show_process_num):
    active_proc = os.popen('top -bi -n 60 -d 1').read().encode().decode().split('\n\n')[1].split('\n')
    active_proc_header = active_proc[0]
    active_proc_list = active_proc[1:-1]
    active_proc_num = len(active_proc_list)
    result = []
    for single_proc in active_proc_list:
        single_proc_prop = single_proc.split()
        Pid = single_proc_prop[0]
        User = single_proc_prop[1]
        cpu_usage = single_proc_prop[8]
        mem_usage = single_proc_prop[9]
        name = single_proc_prop[11]
        result.append([name, Pid, User, cpu_usage, mem_usage, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    if len(result) > show_process_num:
        result = result[:6]
    
    for i in range(len(result)):
        rank = i + 1
        [procname, pid, user, cpu_usage, mem_usage, datatime] = [result[i][0], result[i][1], result[i][2], result[i][3] + '%', result[i][4] + '%', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]

        if TopProcRecorder.exists('rank=%s', [rank]):    
            TopProcRecorder.update_dict({
                'procname': procname,
                'pid': pid,
                'user': user,
                'cpu_usage': cpu_usage,
                'mem_usage': mem_usage,
                'datatime': datatime
            }, 'rank=%s', [rank])
        else:
            TopProcRecorder.insert({
                'rank': rank,
                'procname': procname,
                'pid': pid,
                'user': user,
                'cpu_usage': cpu_usage,
                'mem_usage': mem_usage,
                'datatime': datatime
        })
    
    log_str = "Update DB at " +  datatime
    print(log_str)

if __name__ == "__main__":
    get_process_info(5)    

