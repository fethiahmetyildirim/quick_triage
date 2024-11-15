System and File Information Triage Script
This Python script is designed to gather key system and file information for a quick diagnostic or triage task. It retrieves and presents useful details about the operating system, hardware, and file system.

Key Features:

System Information:

Displays operating system details, processor information, and system uptime.
Retrieves the current active user on the machine.
File System Analysis:

Prompts the user to input a directory path for scanning.
Gathers metadata for the files within the directory, including size, creation, modification, and last accessed timestamps.
Limits the number of files listed to the first 10 for easier review (this can be adjusted for larger datasets).
Triage Report:

The script generates a comprehensive report, including both system and file information, formatted for easy reading and review.
Usage:
Clone or download the repository.
Run the script, which will prompt you to enter the path of the directory you wish to analyze.
The script will output a triage report, including system details and the first 10 files found within the specified directory.
This script is particularly useful for quick diagnostics, system auditing, or troubleshooting file-related issues.

Requirements:
Python 3.x

Example Output:

Triyaj Raporu:
===================================
Sistem Bilgileri:
OS: Windows
OS Version: 10.0.22000
Machine: AMD64
Processor: AMD64 Family 23 Model 24 Stepping 1, AuthenticAMD
Uptime: 68249.12539100647
Current User: Fethi Ahmet

Dosya Bilgileri (İlk 10 Dosya):
Dosya: C:\Users\Fethi Ahmet\OneDrive\Masaüstü\Masaüstü\obsidian notlarım\Cyber Security\Işık siber küme soru.md
  Boyut: 389 bytes
  Oluşturulma: 2024-11-01 20:39:10.528982
  Değiştirilme: 2024-11-01 20:42:30.322964
  Erişim: 2024-11-14 21:13:42.949663
------
Dosya: C:\Users\Fethi Ahmet\OneDrive\Masaüstü\Masaüstü\obsidian notlarım\Cyber Security\Pasted image 20241113121902.png
  Boyut: 20647 bytes
  Oluşturulma: 2024-11-13 12:19:02.449563
  Değiştirilme: 2024-11-13 12:19:02.451071
  Erişim: 2024-11-14 19:13:09.534230
------
Dosya: C:\Users\Fethi Ahmet\OneDrive\Masaüstü\Masaüstü\obsidian notlarım\Cyber Security\.obsidian\app.json
  Boyut: 56 bytes
  Oluşturulma: 2024-08-06 09:56:15.942633
  Değiştirilme: 2024-11-14 19:13:09.924259
  Erişim: 2024-11-14 19:13:09.924259
------
Dosya: C:\Users\Fethi Ahmet\OneDrive\Masaüstü\Masaüstü\obsidian notlarım\Cyber Security\.obsidian\appearance.json
  Boyut: 2 bytes
  Oluşturulma: 2024-08-06 09:56:15.949621
  Değiştirilme: 2024-11-14 19:13:09.934259
  Erişim: 2024-11-14 19:13:09.934259
------
Dosya: C:\Users\Fethi Ahmet\OneDrive\Masaüstü\Masaüstü\obsidian notlarım\Cyber Security\.obsidian\core-plugins-migration.json
  Boyut: 637 bytes
  Oluşturulma: 2024-08-06 09:56:15.516064
  Değiştirilme: 2024-10-17 20:32:12.468741
  Erişim: 2024-10-18 16:43:47.108681
------
Dosya: C:\Users\Fethi Ahmet\OneDrive\Masaüstü\Masaüstü\obsidian notlarım\Cyber Security\.obsidian\core-plugins.json
  Boyut: 637 bytes
  Oluşturulma: 2024-08-06 09:56:15.510092
  Değiştirilme: 2024-11-14 19:13:09.613235
  Erişim: 2024-11-14 19:13:09.613235
------
Dosya: C:\Users\Fethi Ahmet\OneDrive\Masaüstü\Masaüstü\obsidian notlarım\Cyber Security\.obsidian\graph.json
  Boyut: 510 bytes
  Oluşturulma: 2024-08-06 09:57:21.606737
  Değiştirilme: 2024-10-23 14:44:32.558000
  Erişim: 2024-11-14 19:13:09.003191
------
