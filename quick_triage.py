{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "a9e01c7b-5427-4ca0-925c-02dda5e129b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import platform\n",
    "import time\n",
    "import psutil\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1bab9865-d131-447d-88e8-8c7685b1b4e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Windows Sistem Bilgilerini Almak İçin Yardımcı Fonksiyonlar\n",
    "def get_system_info():\n",
    "    system_info = {}\n",
    "    system_info['OS'] = platform.system()  # İşletim Sistemi\n",
    "    system_info['OS Version'] = platform.version()  # İşletim Sistemi Versiyonu\n",
    "    system_info['Machine'] = platform.machine()  # Cihazın Mimarisi\n",
    "    system_info['Processor'] = platform.processor()  # İşlemci\n",
    "    system_info['Uptime'] = time.time() - psutil.boot_time()  # Sistem Açılma Süresi\n",
    "    system_info['Current User'] = os.getlogin()  # Aktif Kullanıcı\n",
    "    return system_info\n",
    "\n",
    "# Dosya Sisteminden Önemli Verileri Almak\n",
    "def get_file_info(directory):\n",
    "    file_info = []\n",
    "    try:\n",
    "        print(f\"Taranıyor: {directory}\")\n",
    "        \n",
    "        for dirpath, dirnames, filenames in os.walk(directory):\n",
    "            for filename in filenames:\n",
    "                filepath = os.path.join(dirpath, filename)\n",
    "                try:\n",
    "                    # Dosya bilgilerini alalım\n",
    "                    file_stats = os.stat(filepath)\n",
    "                    file_info.append({\n",
    "                        'File': filepath,\n",
    "                        'Size (bytes)': file_stats.st_size,\n",
    "                        'Created': datetime.fromtimestamp(file_stats.st_ctime),\n",
    "                        'Modified': datetime.fromtimestamp(file_stats.st_mtime),\n",
    "                        'Accessed': datetime.fromtimestamp(file_stats.st_atime)\n",
    "                    })\n",
    "                except Exception as e:\n",
    "                    # Hata oluşursa hata mesajını yazdıralım\n",
    "                    print(f\"Dosyaya erişim hatası: {filepath} - {e}\")\n",
    "    except Exception as e:\n",
    "        print(f\"Dizin tarama hatası: {directory} - {e}\")\n",
    "    return file_info\n",
    "\n",
    "# Kullanıcının Seçtiği Dizin ile Tarama Yapma\n",
    "def get_user_selected_directory():\n",
    "    directory = input(\"Taramak istediğiniz dizinin tam yolunu girin: \")\n",
    "    if os.path.isdir(directory):\n",
    "        return directory\n",
    "    else:\n",
    "        print(f\"Geçersiz dizin yolu: {directory}\")\n",
    "        return None\n",
    "\n",
    "# Kullanıcı Seçimine Göre Rapor Oluşturma\n",
    "def generate_triage_report():\n",
    "    report = {}\n",
    "    \n",
    "    # Kullanıcıdan dizin yolunu al\n",
    "    directory = get_user_selected_directory()\n",
    "    if directory is None:\n",
    "        print(\"Geçerli bir dizin seçilmedi, program sonlandırılıyor.\")\n",
    "        return None\n",
    "    \n",
    "    # Sistem Bilgileri\n",
    "    system_info = get_system_info()\n",
    "    report['System Information'] = system_info\n",
    "    \n",
    "    # Dosya Bilgileri\n",
    "    file_info = get_file_info(directory)\n",
    "    report['File Information'] = file_info[:10]  # İlk 10 dosya için örnek, büyük veri için sınır koyduk\n",
    "    \n",
    "    return report\n",
    "\n",
    "# Raporu Yazdıralım\n",
    "def print_report(report):\n",
    "    if report is None:\n",
    "        return\n",
    "    \n",
    "    print(\"\\nTriyaj Raporu:\")\n",
    "    print(\"===================================\")\n",
    "    \n",
    "    # Sistem Bilgileri\n",
    "    print(\"Sistem Bilgileri:\")\n",
    "    for key, value in report['System Information'].items():\n",
    "        print(f\"{key}: {value}\")\n",
    "    \n",
    "    print(\"\\nDosya Bilgileri (İlk 10 Dosya):\")\n",
    "    for file_data in report['File Information']:\n",
    "        print(f\"Dosya: {file_data['File']}\")\n",
    "        print(f\"  Boyut: {file_data['Size (bytes)']} bytes\")\n",
    "        print(f\"  Oluşturulma: {file_data['Created']}\")\n",
    "        print(f\"  Değiştirilme: {file_data['Modified']}\")\n",
    "        print(f\"  Erişim: {file_data['Accessed']}\")\n",
    "        print(\"------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6505a2dd-d77c-411c-9cc8-f3b1d26ac78c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Raporu Oluştur ve Yazdır\n",
    "report = generate_triage_report()\n",
    "print_report(report)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a8c84d2-bee4-4cf5-a0a3-9c28ef58394c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}