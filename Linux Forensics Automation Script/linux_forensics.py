import os
import subprocess
import datetime


# Function to check if a service is running
def check_service(service):
    try:
        result = subprocess.run(['systemctl', 'is-active', service], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stdout.decode().strip() == "active":
            return f"{service} is running"
        else:
            return f"{service} is not running"
    except Exception as e:
        return f"Error checking {service}: {e}"


# Function to get system user accounts
def get_user_accounts():
    users = []
    try:
        result = subprocess.run(['cat', '/etc/passwd'], stdout=subprocess.PIPE)
        for line in result.stdout.decode().splitlines():
            user_info = line.split(":")
            users.append(user_info[0])
    except Exception as e:
        return f"Error fetching user accounts: {e}"
    return users


# Function to get active network connections and ports
def get_network_ports():
    try:
        result = subprocess.run(['netstat', '-tulnp'], stdout=subprocess.PIPE)
        return result.stdout.decode()
    except Exception as e:
        return f"Error fetching network ports: {e}"


# Function to check system resources like CPU, RAM, and swap
def get_system_resources():
    try:
        cpu_info = subprocess.run(['top', '-n', '1', '-b'], stdout=subprocess.PIPE)
        memory_info = subprocess.run(['free', '-h'], stdout=subprocess.PIPE)
        disk_info = subprocess.run(['df', '-h'], stdout=subprocess.PIPE)
        return cpu_info.stdout.decode(), memory_info.stdout.decode(), disk_info.stdout.decode()
    except Exception as e:
        return f"Error fetching system resources: {e}"


# Function to get log entries related to user activities
def get_user_log_entries():
    log_entries = []
    try:
        log_entries.append(subprocess.run(['journalctl', '-u', 'sshd'], stdout=subprocess.PIPE).stdout.decode())
        log_entries.append(subprocess.run(['journalctl', '-u', 'vsftpd'], stdout=subprocess.PIPE).stdout.decode())
        log_entries.append(subprocess.run(['journalctl', '-u', 'postfix'], stdout=subprocess.PIPE).stdout.decode())
    except Exception as e:
        return f"Error fetching log entries: {e}"
    return log_entries


# Function to get active processes and services
def get_active_processes():
    try:
        result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE)
        return result.stdout.decode()
    except Exception as e:
        return f"Error fetching active processes: {e}"


# Function to check the status of kernel modules
def check_kernel_modules():
    try:
        result = subprocess.run(['lsmod'], stdout=subprocess.PIPE)
        return result.stdout.decode()
    except Exception as e:
        return f"Error fetching kernel modules: {e}"


# Function to get disk usage
def get_disk_usage():
    try:
        result = subprocess.run(['du', '-sh', '/'], stdout=subprocess.PIPE)
        return result.stdout.decode()
    except Exception as e:
        return f"Error fetching disk usage: {e}"


# Function to check the system's mail settings
def check_mail_settings():
    try:
        result = subprocess.run(['postconf'], stdout=subprocess.PIPE)
        return result.stdout.decode()
    except Exception as e:
        return f"Error fetching mail settings: {e}"


# Function to check for active logins
def check_active_logins():
    try:
        result = subprocess.run(['w'], stdout=subprocess.PIPE)
        return result.stdout.decode()
    except Exception as e:
        return f"Error fetching active logins: {e}"


# Function to check for any open file descriptors
def check_open_files():
    try:
        result = subprocess.run(['lsof'], stdout=subprocess.PIPE)
        return result.stdout.decode()
    except Exception as e:
        return f"Error fetching open files: {e}"


# Function to check system login history
def check_login_history():
    try:
        result = subprocess.run(['last'], stdout=subprocess.PIPE)
        return result.stdout.decode()
    except Exception as e:
        return f"Error fetching login history: {e}"


# Function to check mail logs (SMTP, Postfix)
def check_mail_logs():
    try:
        result = subprocess.run(['journalctl', '-u', 'postfix'], stdout=subprocess.PIPE)
        return result.stdout.decode()
    except Exception as e:
        return f"Error fetching mail logs: {e}"


# Function to check for failed login attempts
def check_failed_logins():
    try:
        result = subprocess.run(['journalctl', 'grep', 'Failed'], stdout=subprocess.PIPE)
        return result.stdout.decode()
    except Exception as e:
        return f"Error fetching failed logins: {e}"


# Function to gather all the necessary forensic data and save to a report
def generate_report():
    report = ""
    report += f"Linux Forensics Report - {datetime.datetime.now()}\n\n"

    # Get user accounts
    report += "User Accounts:\n"
    users = get_user_accounts()
    for user in users:
        report += f"- {user}\n"

    # Network Ports
    report += "\nNetwork Ports:\n"
    network_ports = get_network_ports()
    report += network_ports + "\n"

    # System Resources (CPU, RAM, Disk)
    report += "\nSystem Resources (CPU, RAM, Disk):\n"
    cpu_info, memory_info, disk_info = get_system_resources()
    report += f"CPU Info:\n{cpu_info}\n"
    report += f"Memory Info:\n{memory_info}\n"
    report += f"Disk Info:\n{disk_info}\n"

    # Log Entries (SSH, FTP, Postfix)
    report += "\nLog Entries (SSH, FTP, Postfix):\n"
    logs = get_user_log_entries()
    for log in logs:
        report += f"{log}\n"

    # Active Processes and Services
    report += "\nActive Processes and Services:\n"
    active_processes = get_active_processes()
    report += active_processes + "\n"

    # Kernel Modules
    report += "\nKernel Modules:\n"
    kernel_modules = check_kernel_modules()
    report += kernel_modules + "\n"

    # Disk Usage
    report += "\nDisk Usage:\n"
    disk_usage = get_disk_usage()
    report += disk_usage + "\n"

    # Mail Settings
    report += "\nMail Settings:\n"
    mail_settings = check_mail_settings()
    report += mail_settings + "\n"

    # Active Logins
    report += "\nActive Logins:\n"
    active_logins = check_active_logins()
    report += active_logins + "\n"

    # Open Files
    report += "\nOpen Files:\n"
    open_files = check_open_files()
    report += open_files + "\n"

    # Login History
    report += "\nLogin History:\n"
    login_history = check_login_history()
    report += login_history + "\n"

    # Mail Logs (SMTP, Postfix)
    report += "\nMail Logs (Postfix):\n"
    mail_logs = check_mail_logs()
    report += mail_logs + "\n"

    # Failed Login Attempts
    report += "\nFailed Login Attempts:\n"
    failed_logins = check_failed_logins()
    report += failed_logins + "\n"

    # Save the report to a file
    report_filename = "/tmp/linux_forensics_report.txt"
    with open(report_filename, "w") as file:
        file.write(report)

    print(f"Forensics report saved as {report_filename}")


# Main function to execute the script
if __name__ == "__main__":
    print("Starting Linux Forensics Script...")
    generate_report()
    print("Forensics report generation complete.")
