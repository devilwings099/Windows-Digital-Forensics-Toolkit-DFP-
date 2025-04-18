import subprocess

def run_network_forensics():
    while True:
        print("\nNetwork Forensics Options:")
        print("1. List active connections (netstat)")
        print("2. Display open ports (netstat -an)")
        print("3. Exit to main menu")
        choice = input("Select an option: ")
        if choice == "1":
            subprocess.run("netstat", shell=True)
        elif choice == "2":
            subprocess.run("netstat -an", shell=True)
        elif choice == "3":
            return  # Exits to main menu
        else:
            print("Invalid choice.")

def run_disk_forensics():
    while True:
        print("\nDisk Forensics Options:")
        print("1. List drives (wmic logicaldisk get name)")
        print("2. Display file system info (fsutil)")
        print("3. Exit to main menu")
        choice = input("Select an option: ")
        if choice == "1":
            subprocess.run("wmic logicaldisk get name", shell=True)
        elif choice == "2":
            drive = input("Enter drive letter (e.g., C:): ")
            subprocess.run(f"fsutil fsinfo drives", shell=True)
        elif choice == "3":
            return  # Exits to main menu
        else:
            print("Invalid choice.")

def run_memory_forensics():
    while True:
        print("\nMemory Forensics Options:")
        print("1. List running processes (tasklist)")
        print("2. Dump memory information (systeminfo)")
        print("3. Exit to main menu")
        choice = input("Select an option: ")
        if choice == "1":
            subprocess.run("tasklist", shell=True)
        elif choice == "2":
            subprocess.run("systeminfo", shell=True)
        elif choice == "3":
            return  # Exits to main menu
        else:
            print("Invalid choice.")

def run_registry_forensics():
    while True:
        print("\nWindows Registry Forensics Options:")
        print("1. Query registry key (reg query)")
        print("2. List startup entries")
        print("3. Exit to main menu")
        choice = input("Select an option: ")
        if choice == "1":
            hive = input("Enter registry hive (e.g., HKEY_LOCAL_MACHINE): ")
            key = input("Enter registry key: ")
            subprocess.run(f"reg query {hive}\\{key}", shell=True)
        elif choice == "2":
            subprocess.run('reg query "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"', shell=True)
        elif choice == "3":
            return  # Exits to main menu
        else:
            print("Invalid choice.")

def run_event_log_analysis():
    while True:
        print("\nEvent Log Analysis Options:")
        print("1. Query system logs (wevtutil)")
        print("2. List log names (wevtutil el)")
        print("3. Exit to main menu")
        choice = input("Select an option: ")
        if choice == "1":
            log_name = input("Enter log name (e.g., System, Security): ")
            subprocess.run(f"wevtutil qe {log_name}", shell=True)
        elif choice == "2":
            subprocess.run("wevtutil el", shell=True)
        elif choice == "3":
            return  # Exits to main menu
        else:
            print("Invalid choice.")

def run_usb_device_analysis():
    while True:
        print("\nUSB Device Analysis Options:")
        print("1. Query USB storage history from registry (usbstor)")
        print("2. List currently connected USB devices")
        print("3. Exit to main menu")
        choice = input("Select an option: ")
        if choice == "1":
            subprocess.run('reg query "HKLM\\SYSTEM\\CurrentControlSet\\Enum\\USBSTOR"', shell=True)
        elif choice == "2":
            subprocess.run("wmic path CIM_LogicalDevice where \"Description='USB Mass Storage Device'\" get /value", shell=True)
        elif choice == "3":
            return  # Exits to main menu
        else:
            print("Invalid choice.")

def run_prefetch_analysis():
    while True:
        print("\nWindows Prefetch Analysis:")
        print("1. List prefetch files")
        print("2. Exit to main menu")
        choice = input("Select an option: ")
        if choice == "1":
            prefetch_dir = r"C:\Windows\Prefetch"
            subprocess.run(f'dir "{prefetch_dir}"', shell=True)
        elif choice == "2":
            return  # Exits to main menu
        else:
            print("Invalid choice.")

def run_timeline_analysis():
    while True:
        print("\nTimeline Analysis Options:")
        print("1. Gather recent file changes (dir /T)")
        print("2. Query Event Logs (wevtutil)")
        print("3. Exit to main menu")
        choice = input("Select an option: ")
        if choice == "1":
            drive = input("Enter drive letter to scan (e.g., C:): ")
            subprocess.run(f'dir {drive}\\ /S /T:W', shell=True)
        elif choice == "2":
            log_name = input("Enter log name (e.g., System, Security): ")
            subprocess.run(f"wevtutil qe {log_name} /f:text", shell=True)
        elif choice == "3":
            return  # Exits to main menu
        else:
            print("Invalid choice.")

def run_process_analysis():
    while True:
        print("\nProcess Analysis Options:")
        print("1. List running processes (tasklist)")
        print("2. Show detailed process info (wmic process)")
        print("3. Exit to main menu")
        choice = input("Select an option: ")
        if choice == "1":
            subprocess.run("tasklist", shell=True)
        elif choice == "2":
            subprocess.run("wmic process list full", shell=True)
        elif choice == "3":
            return  # Exits to main menu
        else:
            print("Invalid choice.")

def run_persistence_analysis():
    while True:
        print("\nPersistence Mechanisms Options:")
        print("1. List startup programs")
        print("2. List scheduled tasks")
        print("3. Exit to main menu")
        choice = input("Select an option: ")
        if choice == "1":
            subprocess.run('reg query "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"', shell=True)
        elif choice == "2":
            subprocess.run("schtasks /query /fo LIST /v", shell=True)
        elif choice == "3":
            return  # Exits to main menu
        else:
            print("Invalid choice.")

def main():
    while True:
        print("\nDigital Forensic Application")
        print("1. Network Forensics")
        print("2. Disk Forensics")
        print("3. Memory Forensics")
        print("4. Windows Registry Forensics")
        print("5. Event Log Analysis")
        print("6. USB Device Analysis")
        print("7. Windows Prefetch Files Analysis")
        print("8. Timeline Analysis")
        print("9. Process Analysis")
        print("10. Persistence Mechanisms Analysis")
        print("11. Exit Application")
        choice = input("Select an option: ")

        if choice == "1":
            run_network_forensics()
        elif choice == "2":
            run_disk_forensics()
        elif choice == "3":
            run_memory_forensics()
        elif choice == "4":
            run_registry_forensics()
        elif choice == "5":
            run_event_log_analysis()
        elif choice == "6":
            run_usb_device_analysis()
        elif choice == "7":
            run_prefetch_analysis()
        elif choice == "8":
            run_timeline_analysis()
        elif choice == "9":
            run_process_analysis()
        elif choice == "10":
            run_persistence_analysis()
        elif choice == "11":
            print("Exiting application.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
