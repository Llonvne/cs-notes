pidwait(){
	local pid=$1
	echo "Waiting for $pid to finished..."
	
	while kill -0 $pid 2>/dev/null;do
		sleep 1
	done
	
	echo "Process $pid done!"
}
