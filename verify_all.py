import subprocess, re, sys

output = subprocess.check_output(['euler', '--verify-all'])
print(output)
if re.search('^Problems.*I', output, re.MULTILINE):
    sys.exit(1)
