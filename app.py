import subprocess
import pip

template = "pip install -U {packages}"

# get installed packages
installed_packages = pip.get_installed_distributions()
# generate package list
packages = " ".join(package.key for package in installed_packages)
# generate upgrade sentence
sentence = template.format(packages=packages)
# run sentence
output = subprocess.Popen(sentence, shell=True, stdout=subprocess.PIPE).stdout.read()
if type(output) == bytes:
    print(output.decode('utf-8'))
else:
    print(output)