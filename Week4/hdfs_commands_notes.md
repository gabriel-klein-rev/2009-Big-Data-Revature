# Advanced Linux Commands

df
	- "disk free"
	- Used to display info related to file systems about total space and available space 

mdadm
	- "Multiple Disk and Device Management"
	- Manage and monitor software RAID devices
	- RAID
		- "Redundant array of inexpensive/independent disks"

fdisk, sfdisk, cfdisk
	- "format disk"
	- Generally used for partitioning drives from scripts or for partioning table backups and recovery

lsblk
	- "List blocks"
	- List information about all available or specified block devices

ssh
	- "Secure Shell"
	- Allow two computers/systems to communicate together

## HDFS COMMANDS

hdfs fsck [location]
	- To check the health of our filesystem at a location 

hdfs dfs [-command]
	- Used to interact with hdfs

hdfs dfs -ls [hdfs location]
	- list files/dir in hdfs location

hdfs dfs -cat [hdfs file]
	- print file contents to terminal 

hdfs dfs -copyFromLocal [local file] [hdfs location]
	- Copy file from local fs and save to hdfs location

hdfs dfs -copyToLocal [hdfs file] [local location]
	- Copy file from hdfs and save to local location

hdfs dfs -mkdir [hdfs location]
	- Creates directory at hdfs location

hdfs dfs -rm [hdfs file]
	- Removes file in hdfs

hdfs dfs -rmdir [hdfs location]
	- Removes directory in hdfs 

hdfs dfs -help
	- Lists common commands/options for use with interacting with hdfs

hdfs dfs -put
	- Functionally same as copyFromLocal

hdfs dfs -get
	- Functionally same as copyToLocal





