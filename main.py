import click
from inquirer import Checkbox
from inquirer import prompt
import inquirer
import subprocess
from yaspin import yaspin
from yaspin.spinners import Spinners 

packages = []
def is_apt_package_installed(package_name):
    try:
        # Run dpkg-query command to check if the package is installed
        subprocess.run(['dpkg-query', '-W', '-f=${Status}', package_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        package_version = get_package_version(package_name)
        if not package_version == '<none>': 
            return True
        else:
            return False
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

def list_supported_packages(packages):
    return packages


    return installed_packages

def print_installed_packages(installed_packages):
    index = 0
    installed_packages_print_list = []
    for package in installed_packages:
        installed_packages[index] = '✅ ' + click.style(installed_packages[index], fg='green', bold=True) + ': ' + get_package_version(package)
        installed_packages_print_list.append(installed_packages[index])
        index = index + 1
    return installed_packages_print_list


def install_package(package_name):
    if package_name:
        script_path = f"./scripts/installation/{package_name}.sh"
        try:
            subprocess.run(['bash', script_path], check=True)
            click.echo(click.style(f"{package_name} installation script executed successfully.",  fg='green', bold=True))
        except subprocess.CalledProcessError as e:
            click.echo(f"Error executing {package_name} installation script: {e}")


# ADD inspect SO the user can view what commands gonna be excuted and maybe changing them
# ADD when git installed user will enter his name and email for config
# aws is not being added to instalation list after it installed, version checked by aws --version

@click.group()
def cli():


    pass






@cli.command()
@click.argument('package_name', required=False)
def install(package_name):
    not_installed = []

    with yaspin(Spinners.arc, text="Loading..") as sp:  
        not_installed = [package for package in packages if package not in list_installed_packages(packages)]
    if package_name is None:

        questions = [
            inquirer.Checkbox('actions',
                               message="Select packages to install",
                               choices= not_installed
            )
        ]
        answers = prompt(questions)

        wanted_to_install = answers['actions']

        for package in wanted_to_install:
            install_package(package)


    else:
        if package_name not in packages:
            click.echo(f"⚠️  Sorry, the package you specified is not supported.")
        elif package_name in list_installed_packages(packages):
            click.echo(click.style(f"{package_name}", fg='green', bold=True) + " is already installed in your system.")
        else:
            install_package(package_name)

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
        for package in list_supported_packages(packages):
            click.echo(package)
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


def option2_function():
    click.echo("You chose Option 2")



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
