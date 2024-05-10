import click
from inquirer import Checkbox
from inquirer import prompt
import inquirer
import subprocess

packages = []
def is_apt_package_installed(package_name):
    try:
        # Run dpkg-query command to check if the package is installed
        subprocess.run(['dpkg-query', '-W', '-f=${Status}', package_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False


def get_package_version(package_name):
    try:
        # Run dpkg -l command to get the package version
        result = subprocess.run(['dpkg', '-l', package_name], check=True, capture_output=True, text=True)

        # Extract the version using grep and awk
        version_output = subprocess.run(['grep', package_name], input=result.stdout, capture_output=True, text=True)
        version = subprocess.run(['awk', '{print $3}'], input=version_output.stdout, capture_output=True, text=True)

        return version.stdout.strip()
    except subprocess.CalledProcessError:
        return "Error: Unable to retrieve package information"


def read_packages_file(filename):
    packages = []
    with open(filename, 'r') as file:
        lines = sorted(file.readlines(), key=lambda x: x.strip()[0])
        for line in lines:
            package = line.strip()  # Remove leading/trailing whitespace and newline characters
            packages.append(package)
    return packages


def list_installed_packages(packages):
    installed_packages = [package for package in packages if is_apt_package_installed(package)]


    return installed_packages

def print_installed_packages(installed_packages):
    index = 0
    installed_packages_print_list = []
    for package in installed_packages:
        installed_packages[index] = '✅ ' + installed_packages[index] + ': ' + get_package_version(package)
        installed_packages_print_list.append(installed_packages[index])
        index = index + 1
    return installed_packages_print_list



@click.group()
def cli():
    pass

@cli.command()
def list():
    questions = [
        inquirer.List('action',
                      message="What do you want to do?",
                      choices=['Installed Packages', 'Available Updates', 'Supported Packages']
        )
    ]
    answers = prompt(questions)

    action = answers['action']

    if action == "Installed Packages":
        for package in print_installed_packages(list_installed_packages(packages)):
            click.echo(package)
    elif action == 'Available Updates':
        option2_function()
    elif action == 'Supported Packages':
        option3_function()
    else:
        click.echo("Invalid option!")

@cli.command()
def update():
    questions = [
        inquirer.Checkbox('actions',
                          message="Select actions to perform:",
                          choices=['Action 1', 'Action 2', 'Action 3']
        )
    ]
    answers = prompt(questions)

    actions = answers['actions']

    if 'Action 1' in actions:
        action1_function()
    if 'Action 2' in actions:
        action2_function()
    if 'Action 3' in actions:
        action3_function()

def option1_function():
    click.echo("You chose Option 1")

def option2_function():
    click.echo("You chose Option 2")

def option3_function():
    click.echo(packages)

def action1_function():
    click.echo("Action 1 performed")

def action2_function():
    click.echo("Action 2 performed")

def action3_function():
    click.echo("Action 3 performed")

if __name__ == "__main__":
    packages_file = "packages.txt"
    packages = read_packages_file(packages_file)
    cli()