import controller as ctr
import reshuffling as rs
import time
window_s_ = "250" #input("Put in window size:")
step_s_ = "40" #input("Put in step size:")
iterations_ = 2 #int(input("Put in number of iterations:"))
file_path_ = "C:/Users/Administrator/Desktop/Work/"
file_name_ = "reshuffled_for_scan.sse"
app_path_ = "C:/Program Files (x86)/SSE/PB10 SSE_v1.3.exe"
saving_path_ = file_path_ + "scans/"+window_s_+"_"+step_s_+"/"
#for i in range(4):
for i in range(iterations_):
    rs.reshuffling_sse(file_path_, "Verified_groupscan_m.sse")
    ctr.controller(file_path_, file_name_, app_path_, saving_path_, window_s_, step_s_)
    rs.removing_file("C:/Users/Administrator/Desktop/Work/", "reshuffled_for_scan.sse")
    #time.sleep(12000)
    #ctr.closing_app(app_path_)
    #time.sleep(100)


