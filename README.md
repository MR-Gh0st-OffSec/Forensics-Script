# System Investigation Commands

This guide provides essential Linux commands for investigating user accounts, log entries, system resources, processes, services, files, network settings, and more. These commands are useful for security auditing, system monitoring, and troubleshooting.

---

## User Accounts
Commands to investigate user activities, permissions, and unusual actions:

- `cat /etc/passwd` - List user accounts.
- `passwd -S [User_Name]` - Check password status for a user.
- `lastlog` - Show the most recent logins for all users.
- `last` - Display a list of last logged-in users.
- `who` - Show users currently logged on.
- `w` - Show who is logged on and what they are doing.

---

## Log Entries
Commands to review system and application logs:

- `cat /var/log/messages` - Display system messages.
- `cat /var/log/auth.log` - Show user authentication logs.
- `cat /var/log/secure` - Show authentication logs (Red Hat-based systems).
- `cat /var/log/boot.log` - Display system boot log.
- `cat /var/log/dmesg` - Show kernel ring buffer messages.
- `cat /var/log/kern.log` - View kernel log.

---

## System Resources
Commands to check system performance and resource usage:

- `top` - Display real-time view of Linux tasks.
- `htop` - Interactive process viewer.
- `uptime` - Show system uptime.
- `ps aux` - List all currently running processes.
- `pstree` - Show processes as a tree.
- `free -m` - Display memory usage in MB.

---

## Processes
Commands to investigate running processes:

- `ps -ef` - Show all currently running processes.
- `pstree -p` - Display process tree with PIDs.
- `top -n 1` - Display top processes.
- `ps -eo pid,tt,user,fname,rsz` - Show processes in a custom format.
- `lsof -i` - List open files associated with network connections.

---

## Services
Commands to inspect services running on the system:

- `chkconfig --list` - List all services and their current states (SysVinit systems).
- `service --status-all` - Show the status of all services.
- `systemctl list-units --type=service` - List running services (systemd).

---

## Files
Commands for file investigation:

- `ls -alh` - Show all files in a human-readable format.
- `find / -name [filename]` - Find a specific file.
- `find / -mtime -[N]` - Find files modified in the last N days.
- `find / -atime -[N]` - Find files accessed in the last N days.
- `find / -size +[N]c` - Find files larger than N bytes.

---

## Network Settings
Commands to review network configurations and connections:

- `ifconfig -a` - Show all network interfaces.
- `netstat -antup` - Display active network connections.
- `iptables -L -n -v` - Show all iptables rules.
- `route -n` - Display routing table.
- `ss -tuln` - Show listening ports and established connections.

---

## Additional Commands
Useful commands for advanced system inspection:

- `grep :0: /etc/passwd` - Find root accounts.
- `find / -nouser -print` - Find files with no associated user.
- `cat /etc/shadow` - View encrypted passwords and account expiration info.
- `cat /etc/group` - View group information.
- `cat /etc/sudoers` - View sudoers file.
- `tail /var/log/auth.log` - View last entries in authentication log.
- `history | less` - View command history.
- `cat /proc/meminfo` - Display memory information.
- `cat /proc/mounts` - Display mounted filesystems.
- `lsof -p [pid]` - List open files for a specific process by PID.
- `service --status-all` - List all services and their statuses.
- `cat /etc/crontab` - View scheduled tasks in cron.
- `more /etc/resolv.conf` - View DNS settings.
- `more /etc/hosts` - View host file entries.
- `iptables -L -n` - List all iptables rules without resolving IP addresses.
- `find /home/ -type f -size +512k -exec ls -lh {} \;` - Find files larger than 512KB in home directories.
- `find /etc/ -readable -type f 2>/dev/null` - Find readable files in `/etc`.
- `find / -mtime -2 -ls` - Find files modified in the last 2 days.
- `netstat -nap` - Show network connections and associated programs.
- `arp -a` - View the ARP table.
- `echo $PATH` - Display the PATH environment variable.

---

These commands offer insights into user activities, system health, and network security, providing a comprehensive toolset for system administrators and security analysts.

# Forensics Command Reference

This reference provides a comprehensive list of commands for investigating different components in a Linux system, covering categories such as Kernel, Memory, Disk, User, and Service Investigations. These commands are valuable for system forensics, monitoring, and security auditing.

---

| **Category**          | **Command**                                | **Description** |
|-----------------------|--------------------------------------------|-----------------|
| **Kernel**            | `dmesg`                                    | Display kernel ring buffer messages. |
|                       | `cat /proc/version`                        | Show kernel version. |
|                       | `uname -a`                                 | Display all system information. |
|                       | `cat /proc/modules`                        | List loaded kernel modules. |
|                       | `lsmod`                                    | Display all loaded modules. |
|                       | `modinfo [module_name]`                    | Show details about a specific module. |
|                       | `sysctl -a`                                | List all system kernel parameters. |
|                       | `journalctl -k`                            | Show kernel log entries. |
| **Memory**            | `free -m`                                  | Display memory usage in MB. |
|                       | `cat /proc/meminfo`                        | Show detailed memory information. |
|                       | `vmstat`                                   | Report virtual memory statistics. |
|                       | `top`                                      | Display memory and CPU usage. |
|                       | `ps aux --sort=-%mem | head`               | Show top memory-consuming processes. |
|                       | `smem`                                     | Display detailed memory report per user. |
|                       | `pmap [pid]`                               | Show memory map of a specific process. |
| **Disk & Files**      | `df -h`                                    | Display disk space usage in human-readable format. |
|                       | `du -sh /path/to/directory`                | Display disk usage of a directory. |
|                       | `fdisk -l`                                 | Show all partitions on all disks. |
|                       | `lsblk`                                    | Display block devices. |
|                       | `mount`                                    | Show mounted filesystems. |
|                       | `find / -name [filename]`                  | Search for files by name. |
|                       | `file [filename]`                          | Determine file type. |
|                       | `stat [filename]`                          | Show detailed file information. |
|                       | `ls -l --time-style=full-iso [filename]`   | Show file timestamps. |
|                       | `find / -type f -size +100M`               | Find files larger than 100 MB. |
|                       | `lsof | grep deleted`                      | List open files marked for deletion. |
|                       | `grep -a 'string' /dev/sdX`                | Search raw disk for strings. |
|                       | `dd if=/dev/sda of=/path/to/backup.img`    | Create a disk image for forensics. |
| **Mail**              | `cat /var/mail/[user]`                     | View user's mail file. |
|                       | `grep -i 'From' /var/log/maillog`          | Search for "From" entries in mail logs. |
|                       | `tail -f /var/log/maillog`                 | Monitor mail log in real time. |
|                       | `grep 'smtp' /var/log/mail.log`            | Find SMTP-related entries in mail logs. |
|                       | `postqueue -p`                             | List emails in the mail queue (Postfix). |
|                       | `exim -bp`                                 | Show Exim mail queue. |
| **User**              | `cat /etc/passwd`                          | List user accounts. |
|                       | `cat /etc/shadow`                          | View encrypted passwords and account expiration. |
|                       | `last`                                     | Show last logged in users. |
|                       | `who`                                      | Display logged-in users. |
|                       | `lastlog`                                  | Show last login of all users. |
|                       | `grep -w 'sudo' /etc/group`                | Show users in the sudo group. |
|                       | `passwd -S [username]`                     | Check password status for a user. |
|                       | `chage -l [username]`                      | Show password aging information. |
| **All Services**      | `service --status-all`                     | List status of all services. |
|                       | `systemctl list-units --type=service`      | List active services (systemd). |
|                       | `chkconfig --list`                         | Show all services (SysVinit systems). |
|                       | `service [service_name] status`            | Show status of a specific service. |
|                       | `netstat -antup`                           | List active network connections and services. |
| **SMTP**              | `telnet smtp.example.com 25`               | Connect to SMTP server on port 25. |
|                       | `echo 'Test message' | mail -s 'Subject' [recipient]` | Send test email via SMTP. |
|                       | `grep smtp /var/log/mail.log`              | Check for SMTP log entries. |
| **FTP**               | `ftp [server_address]`                     | Connect to an FTP server. |
|                       | `lftp [server_address]`                    | Use LFTP to connect to an FTP server. |
|                       | `grep -i 'ftp' /var/log/auth.log`          | Find FTP-related authentication log entries. |
| **Telnet**            | `telnet [host]`                            | Connect to a remote host via Telnet. |
|                       | `grep -i 'telnet' /var/log/auth.log`       | Check for Telnet access in logs. |
| **SSH**               | `ssh [user]@[host]`                        | Connect to a remote host via SSH. |
|                       | `grep 'sshd' /var/log/auth.log`            | Search for SSH logs in authentication log. |
|                       | `ss -ant | grep :22`                       | Show SSH connections on port 22. |
|                       | `fail2ban-client status sshd`              | Check fail2ban SSHD service status. |
| **Networking**        | `ifconfig -a`                              | Show all network interfaces. |
|                       | `iptables -L -n -v`                        | List all iptables rules. |
|                       | `route -n`                                 | Show routing table. |
|                       | `arp -a`                                   | Display ARP cache. |
|                       | `ss -tuln`                                 | Show listening ports. |
|                       | `tcpdump -i eth0`                          | Capture packets on interface eth0. |
|                       | `nmap -sP [subnet]`                        | Ping scan a subnet. |
|                       | `traceroute [host]`                        | Trace route to a host. |
| **Processes**         | `ps aux`                                   | List running processes. |
|                       | `top`                                      | Show active processes. |
|                       | `htop`                                     | Interactive process viewer. |
|                       | `lsof -i`                                  | List open network files. |
|                       | `pstree`                                   | Display process tree. |
|                       | `pkill -9 [process_name]`                  | Forcefully terminate a process by name. |
| **System Info**       | `uname -a`                                 | Display system information. |
|                       | `hostnamectl`                              | Show hostname and OS information. |
|                       | `lsb_release -a`                           | Show distribution information. |
|                       | `dmidecode`                                | Show hardware information. |
| **Additional Commands** | `history | less`                        | View command history. |
|                       | `cat /etc/crontab`                         | View scheduled tasks in cron. |
|                       | `more /etc/hosts`                          | View host file entries. |
|                       | `more /etc/resolv.conf`                    | View DNS settings. |
|                       | `iptables -L -n`                           | List all iptables rules without IP resolution. |
|                       | `find /etc/ -readable -type f 2>/dev/null` | Find readable files in the /etc directory. |
|                       | `echo $PATH`                               | Show PATH environment variable. |

---

These commands provide a robust foundation for analyzing system activity, services, and security risks across critical system components.


# Linux Forensics Command Toolkit

This toolkit provides a collection of commands for system forensics, monitoring, and incident response. Organized into categories, it helps users investigate different aspects of a Linux system, such as network activity, user actions, and filesystem integrity.

---

## Table of Contents

1. [System Information](#system-information)
2. [Network Activity](#network-activity)
3. [User Activity](#user-activity)
4. [File and Directory Analysis](#file-and-directory-analysis)
5. [Memory & Process Investigation](#memory--process-investigation)
6. [Service & Logs Analysis](#service--logs-analysis)
7. [Service Specific Commands](#service-specific-commands)
8. [Disk & Filesystem Analysis](#disk--filesystem-analysis)
9. [Audit & Security Monitoring](#audit--security-monitoring)
10. [Additional Utilities](#additional-utilities)
11. [Examples](#examples)
12. [Contributions](#contributions)
13. [License](#license)
14. [Support](#support)

---

## 1. System Information

Commands to retrieve details about the system, including kernel version, hostname, uptime, and hardware information.

```sh
uname -a                  # Show kernel version and architecture
hostnamectl               # Display system hostname and OS details
date                      # Show system date and time


Network Activity
Commands for analyzing network interfaces, active connections, firewall settings, and traffic monitoring.



ifconfig -a               # Show all network interfaces
ss -tuln                  # List listening ports
iptables -L -n -v         # List all firewall rules



User Activity

Commands to monitor user logins, privileges, and recent activity.



cat /etc/passwd           # List user accounts
lastlog                   # Display last login times
who                       # Show currently logged-in users


File and Directory Analysis

Commands for file integrity, size checks, and modification dates.



find / -type f -size +100M # Locate files larger than 100 MB
md5sum /path/to/file       # Generate MD5 checksum of a file
stat [filename]            # Show file details


Memory & Process Investigation

Commands for examining running processes, memory usage, and open file handles.


ps aux                     # List all running processes
htop                       # Interactive process viewer
pmap [pid]                 # Show memory map of a specific process



Service & Logs Analysis

Commands to check service status and view various system logs.


service --status-all       # List status of all services
journalctl                 # Display all logs (systemd)
cat /var/log/auth.log      # View user authentication logs



Service Specific Commands

Commands for investigating specific services like SMTP, FTP, and SSH.


grep 'smtp' /var/log/mail.log # Check SMTP-related entries in mail logs
systemctl status sshd         # Check SSH service status
netstat -an | grep :80        # Check open HTTP connections






# Linux Forensics Toolkit

---

## Table of Contents
1. [System Information](#system-information)
2. [Network Activity](#network-activity)
3. [User Activity](#user-activity)
4. [File and Directory Analysis](#file-and-directory-analysis)
5. [Memory & Process Investigation](#memory--process-investigation)
6. [Service & Logs Analysis](#service--logs-analysis)
7. [Service Specific Commands](#service-specific-commands)
8. [Disk & Filesystem Analysis](#disk--filesystem-analysis)
9. [Audit & Security Monitoring](#audit--security-monitoring)
10. [Additional Utilities](#additional-utilities)
11. [Examples](#examples)
12. [Contributions](#contributions)
13. [License](#license)
14. [Support](#support)

---

### System Information

Commands to retrieve details about the system, including kernel version, hostname, uptime, and hardware information.


uname -a                  # Show kernel version and architecture
hostnamectl               # Display system hostname and OS details
date                      # Show system date and time


Network Activity

Commands for analyzing network interfaces, active connections, firewall settings, and traffic monitoring.


ifconfig -a               # Show all network interfaces
ss -tuln                  # List listening ports
iptables -L -n -v         # List all firewall rules


User Activity

Commands to monitor user logins, privileges, and recent activity.


cat /etc/passwd           # List user accounts
lastlog                   # Display last login times
who                       # Show currently logged-in users


File and Directory Analysis

Commands for file integrity, size checks, and modification dates.


find / -type f -size +100M # Locate files larger than 100 MB
md5sum /path/to/file       # Generate MD5 checksum of a file
stat [filename]            # Show file details


Memory & Process Investigation

Commands for examining running processes, memory usage, and open file handles.


ps aux                     # List all running processes
htop                       # Interactive process viewer
pmap [pid]                 # Show memory map of a specific process


Service & Logs Analysis

Commands to check service status and view various system logs.


service --status-all       # List status of all services
journalctl                 # Display all logs (systemd)
cat /var/log/auth.log      # View user authentication logs


Service Specific Commands

Commands for investigating specific services like SMTP, FTP, and SSH.


grep 'smtp' /var/log/mail.log # Check SMTP-related entries in mail logs
systemctl status sshd         # Check SSH service status
netstat -an | grep :80        # Check open HTTP connections


Disk & Filesystem Analysis

Commands to inspect disk usage, partitions, and filesystem health.


df -h                      # Show disk usage
lsblk                      # Display block devices
mount                      # List all mounted filesystems


Audit & Security Monitoring

Commands for auditing and security event monitoring, such as failed logins and privilege escalation attempts.


auditctl -l                # List all active audit rules
faillog                    # Display failed login attempts
chkrootkit                 # Check for rootkits


Additional Utilities

Various utilities for gathering system information, inspecting DNS settings, and more.


echo $PATH                 # Display system PATH variable
curl -I [URL]              # Fetch HTTP headers of a URL
arp -a                     # Display the ARP cache



Below are examples of commands used in real-life scenarios for incident response.

Checking last logins for specific accounts

lastlog | grep 'username'



Investigating open network connections

netstat -antup | grep '[port_number]'



Searching for modified files

find /path -type f -mtime -7  # Find files modified within the last 7 days


