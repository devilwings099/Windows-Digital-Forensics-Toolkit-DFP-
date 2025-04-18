# Windows-Digital-Forensics-Toolkit-DFP-
A Python-based CLI tool for Windows digital forensics, offering modules for network, disk, memory, registry, logs, USB, prefetch, timeline, process, and persistence analysis.


## Description

The **Windows Digital Forensics Toolkit (DFP)** is a command-line application developed in Python that provides a comprehensive set of tools for conducting digital forensic investigations on Windows systems. Designed with modularity and ease of use in mind, this toolkit enables forensic investigators, incident responders, and cybersecurity enthusiasts to gather critical system information quickly and efficiently.

## Key Features

- **Network Forensics**: View active network connections and open ports using built-in Windows networking commands.
- **Disk Forensics**: Enumerate connected drives and retrieve file system details.
- **Memory Forensics**: List running processes and extract system information from memory.
- **Registry Forensics**: Query specific registry keys and examine startup entries.
- **Event Log Analysis**: Analyze Windows Event Logs and list available log sources.
- **USB Device Analysis**: Retrieve historical and current information on USB devices from the system registry.
- **Prefetch File Analysis**: Inspect Windows prefetch files to determine application execution history.
- **Timeline Analysis**: Analyze file activity timelines and correlate them with event logs.
- **Process Analysis**: Investigate process behavior through detailed task and process listings.
- **Persistence Mechanisms**: Identify common persistence techniques such as startup entries and scheduled tasks.

## Usage

The application runs through a simple menu-driven interface, allowing users to select different forensic modules. Each module further offers specific investigative options, enabling targeted data acquisition.

## Platform

- **Windows**

## Language

- **Python** (using `subprocess` module for system command execution)
