# DevOps Environment Setup Tool

This tool simplifies the process of setting up a Linux environment tailored for DevOps engineers. It allows you to easily install and manage a selection of commonly used DevOps tools.

## Features

*   **Interactive Package Selection:** Choose which packages to install via an interactive prompt.
*   **Package Installation:** Installs selected packages using pre-defined installation scripts.
*   **Package Listing:** Lists installed, available updates (currently stubbed), and supported packages.
*   **Package Update (Stubbed):** Provides a framework for updating packages, though the functionality is currently not fully implemented.
*   **Installation Script Driven:** Package installations are handled by individual shell scripts, allowing for flexibility and customization.
*   **Package Status Check:** Detects if a package is already installed and displays its version.
*   **Spinner for Loading:** Uses a spinner to indicate progress during package loading.
*   **Colorized Output:** Uses colorized output for better readability and highlighting of important information.

## Supported Packages

The following packages are currently supported (though not all installation scripts may be fully implemented yet):

terraform
jenkins
ansible
docker
git
elasticsearch
logstash
kibana
datadog-agent
grafana
prometheus
google-cloud-cli
google-cloud-sdk
kubectl
awscli
azure-cli
gcloud
jq
yq
openssh-client
vim
k9s
flux
tfswitch
helm
kustomize
python3
vscode
rancher


**Important Note:** Not all tools listed above have fully implemented installation scripts at this time.  The tool is still under development, and support for more packages will be added in the future.

## How to Run

1.  **Prerequisites:** Ensure you have Python 3 installed. You'll also need to install the required Python packages:

    ```bash
    pip install click inquirer yaspin
    ```

2.  **Clone the Repository:** Clone the repository containing the tool's code.

3.  **Navigate to the Directory:** Change your current directory to the cloned repository's directory.

4.  **Create `packages.txt`:** Create a file named `packages.txt` in the same directory as the script. List the supported packages (one per line) that you want the tool to manage. This file is used to define the available packages for installation.  For example:

    ```
    terraform
    docker
    git
    awscli
    ```

5.  **Run the Tool:** Execute the main script:

    ```bash
    python <script_name>.py  # Replace main.py with the actual name of your script.
    ```

## Usage

The tool uses a command-line interface with subcommands.

*   **`install`:** Installs packages.  You can install specific packages by name or select them interactively.
    *   Interactive Installation: `python main.py install` (prompts for package selection)
    *   Specific Package Installation: `python <script_name>.py install <package_name>`
*   **`list`:** Lists packages.
    *   List Installed Packages: `python main.py list` (then select "Installed Packages")
    *   List Supported Packages: `python main.py list` (then select "Supported Packages")
    *   List Available Updates: `python main.py list` (then select "Available Updates" - currently stubbed)
*   **`update`:** Updates packages (currently not fully implemented). `python <script_name>.py update`

## Code Overview

The script is written in Python and uses the `click`, `inquirer`, and `yaspin` libraries.

*   **`is_apt_package_installed()`:** Checks if a package is installed using `dpkg-query`.
*   **`get_package_version()`:** Retrieves the installed version of a package using `dpkg -l`.
*   **`read_packages_file()`:** Reads the `packages.txt` file.
*   **`install_package()`:** Executes the installation script for a given package.
*   **`cli` group:** Defines the command-line interface using `click`.
*   **`install` command:** Implements the package installation logic.
*   **`list` command:** Implements the package listing logic.
*   **`update` command:** Implements the package update logic (currently stubbed).


## Future Improvements

*   **Complete Package Installation Scripts:** Implement installation scripts for all supported packages.
*   **Implement `update` command:** Fully implement the package update functionality.
*   **Add Configuration:** Allow users to configure the tool (e.g., location of installation scripts).
*   **Improved Error Handling:** Add more robust error handling.
*   **Package Dependencies:** Handle package dependencies during installation.
*   **Testing:** Add unit and integration tests.



[Your Name/GitHub Profile (Optional)]
