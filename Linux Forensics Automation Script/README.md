# Linux Forensics Automation Script

## Overview
This script automates the collection of forensic data from a Linux system for incident response, security analysis, and auditing. It checks various components of the system, including user accounts, logs, system resources, network ports, active processes, disk usage, and more. The script generates a forensic report that can be saved and reviewed for analysis.

## Features
- **Service Check**: Verifies if essential services like SSH, FTP, Postfix are running.
- **User Accounts**: Retrieves a list of all user accounts on the system.
- **Network Ports**: Checks active network connections and open ports.
- **System Resources**: Gathers CPU, memory, and disk usage information.
- **Log Entries**: Collects logs related to user activities, failed login attempts, and service logs.
- **Active Processes**: Lists all currently running processes on the system.
- **Kernel Modules**: Displays the currently loaded kernel modules.
- **Disk Usage**: Checks the disk usage of the system's root directory.
- **Mail Settings**: Fetches mail server configurations from Postfix.
- **Login History**: Displays a history of user logins.
- **Failed Logins**: Collects failed login attempts from the system logs.

The collected data is saved in a text file, which can be reviewed later for further analysis.

## Installation
To use this script, follow these steps:

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/linux-forensics.git
cd linux-forensics

2. Install required dependencies
The script relies on certain Linux utilities (ps, netstat, systemctl, journalctl, etc.). Ensure these utilities are installed and available in your PATH.

For Debian-based systems (Ubuntu, Kali, etc.):

sudo apt update
sudo apt install -y net-tools procps lsof systemd

3. Make the script executable


chmod +x linux_forensics.py

Usage

Run the Script: To run the script and generate the forensic report, use the following command:

sudo python3 linux_forensics.py

Report Output: The report will be saved as linux_forensics_report.txt in the /tmp/ directory. You can modify the script to change the output file path if needed.

Example Output: The output will include detailed information about

User Accounts
Network Ports
System Resources (CPU, Memory, Disk)
Log Entries (related to SSH, FTP, and Postfix services)
Active Processes
Kernel Modules
Disk Usage
Mail Settings
Active Logins
Login History
Failed Login Attempts
Customization

You can modify the script to add or remove checks as per your requirements. For example:

To add a check for a specific service, you can extend the check_service() function.
You can modify the generate_report() function to include more system checks.

File Structure

linux-forensics/
│
├── linux_forensics.py           # Main Python script for collecting forensic data
├── README.md                   # This README file
└── requirements.txt            # Optional - List of required Python packages (if needed)

Example Forensics Report
The generated report might look like this:


Linux Forensics Report - 2024-11-07 15:32:10

User Accounts

- root
- admin
- user1
- user2

Network Ports

Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN

System Resources (CPU, RAM, Disk)

CPU Info
top - 15:32:10 up 2 days,  3:20,  1 user,  load average: 0.23, 0.12, 0.08

Memory Info

free -h
              total        used        free      shared  buff/cache   available
Mem:            8.0G        2.4G        3.5G        123M        2.0G        4.2G
Swap:           2.0G          0B        2.0G

Disk Info

Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   20G   28G  42% /

Active Processes and Services

USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1  16908  1020 ?        Ss   10:50   0:01 /sbin/init

Kernel Modules

lsmod

Disk Usage

du -sh /

Mail Settings

postconf -n

Login History

last

Failed Login Attempts

journalctl | grep 'Failed

Contributing
Feel free to fork this repository, submit pull requests, or open issues if you encounter any problems or have suggestions for improvement.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Author
MR Gh0st

Note: The report is generated using subprocess in Python, which means the script requires Python 3.x and root privileges to access system information and logs.



### How to Use This README:
1. Copy the above `README.md` content.
2. Create a new file called `README.md` in the root of your GitHub repository.
3. Paste the content into that file and commit it.

This will help users understand what your script does, how to use it, and how to customize it for their needs.