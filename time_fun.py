from datetime import datetime
def time_curr():
	now = datetime.now();
	curr_time=now.strftime("%H:%M");
	#print(curr_time)
	return curr_time

