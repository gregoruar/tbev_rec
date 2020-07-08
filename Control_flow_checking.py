import controller_for_checking as ctr
window_s_ = 250
step_s_ = 40
#for window_s_, step_s_ in zip([200, 200, 200, 200, 250, 250, 250, 250, 300, 300, 300, 300, 350, 350, 350, 350, 400, 400, 400, 400], [15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60, 15, 30, 45, 60]):
file_path_ = "C:/Users/Administrator/Desktop/Work/"
file_name_ = "Verified_groupscan.sse"
app_path_ = "C:/Program Files (x86)/SSE/PB10 SSE_v1.3.exe"
saving_path_ = file_path_ + "scans/testing_for_signal/"
ctr.controller(file_path_, file_name_, app_path_, saving_path_, window_s_, step_s_)


