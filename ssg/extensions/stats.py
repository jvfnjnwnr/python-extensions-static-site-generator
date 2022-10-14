from ssg import hooks
import time
global start_time = None
global total_written = 0
@hooks.register("start_build")
def start_build():
    global start_time = time.now()
@hooks.register("written")
def written():
    global total_written += 1
@hooks.register("stats")
def stats():
    final_time = time.now() - start_time
    average = final_time / total_written if total_written != 0 else 0
    report = "Converted: {} · Time: {:.2f} sec · Avg: {:.4f} sec/file"
    print(report.format()
