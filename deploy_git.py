import subprocess, os

cwd = r"C:\Users\KIHYUNKIM\Desktop\Domain\출판사제안\domain-proposal-web"

def run(cmd):
    res = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True, encoding="utf-8")
    print("CMD:", cmd)
    if res.stdout:
        print("STDOUT:", res.stdout.strip())
    if res.stderr:
        print("STDERR:", res.stderr.strip())
    return res.returncode

run("git init -b main")
run("git add .")
run("git commit -m \"Initial commit: DomAIn proposal web publishing\"")
run("gh repo create domain-proposal --public --source=. --remote=origin --push")
