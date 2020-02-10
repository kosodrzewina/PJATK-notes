import os
import re
import subprocess
from datetime import datetime

docs_path = 'docs'
excluded_dirs = ['.git', 'docs', '.vscode']
summary = {}

for root, dirs, files in os.walk('.'):
    if root == '.':
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

    curr_docs = os.path.join(docs_path, root[2:])
    os.makedirs(curr_docs, exist_ok=True)

    for f in filter(lambda f: f.endswith('md'), files):
        curr_file = os.path.join(root, f)
        curr_out = os.path.join(
            curr_docs, re.compile(r'[\\/]').split(curr_file)[-1][:-2] + 'html')
        subprocess.run(['pandoc', curr_file, '-s',
                        '--katex', '-o', curr_out, '--metadata', f'pagetitle={f[:-3]}', '-H', '.github/workflows/headers.html'])
        if root in summary:
            summary[root].append(f[:-2] + 'html')
        else:
            summary[root] = [f[:-2] + 'html']

with open(os.path.join(docs_path, 'index.html'), mode='w+') as f:
    html_summary = ''
    for key in summary:
        if key != '.':
            html_summary += f'<li>{key[2:]}<ul>'
        for topic in summary[key]:
            html_summary += f'<li><a href="{os.path.join(key, topic)}">{topic[:-5]}</a></li>'
        if key != '.':
            html_summary += '</ul></li>'

    with open('.github/workflows/headers.html') as h:
        f.write(f"""\
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link rel="icon" href="https://raw.githubusercontent.com/kosodrzewina/PJATK-notes/master/fav.ico">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>PJATK notes</title>
        {h.read()}
    </head>
    <body>
        Available notes:

        <ul>{html_summary}</ul>


        <footer>
            <a href="https://github.com/kosodrzewina/PJATK-notes">Repo on GitHub</a> <br/>
            Last update: {datetime.now().strftime("%H:%M %B %d, %Y")}
        </footer>
    </body>
    </html>
    """)
