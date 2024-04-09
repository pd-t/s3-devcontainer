# S3 Devcontainer Project

Welcome to the S3 Devcontainer Project! This initiative is all about providing you with Python scripts that facilitate seamless interactions with AWS S3. By leveraging the power of `boto3` for S3 operations and `python-dotenv` for efficient environment variable management, we aim to streamline your development workflows and enhance productivity.

## Prerequisites

Before diving into this project, there are a couple of key prerequisites to ensure you have the smoothest experience possible:

- **Familiarity with Dev Containers**: An understanding of how to use development containers (Dev Containers) will greatly benefit your workflow. If you're new to this concept, consider exploring resources on using Dev Containers or Docker for development.
- **Python & Poetry Installation**: Ensure that Python and Poetry are installed on your development machine. These tools are essential for managing the project's dependencies and environments.

## Getting Started

Follow these steps to get your project up and running:

### 1. Clone the Repository

Begin by cloning this repository to your local machine. This step is your gateway to starting work with the S3 Devcontainer Project.

### 2. Setup the Environment

Depending on your setup, you have two paths to choose from:

- **Using Dev Containers**: If you're familiar with Dev Containers, proceed to run your dev container which should handle the environment setup automatically.
- **Manual Setup with Poetry**: Alternatively, run the following command in your terminal to install the project dependencies:

```bash
poetry install
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory of your project. This file should contain your AWS credentials, which are necessary for the scripts to interact with AWS S3:

```plaintext
AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY>
AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESS_KEY>
```

### 4. Running the Example Script

Once your environment is configured, you can start executing the scripts. To run the example script, use the following command:

```bash
poetry run src/example.py
```

This command will initiate the script located at `src/example.py`, demonstrating a basic interaction with AWS S3.

---

Dive in and explore the capabilities of interacting with AWS S3 through Python scripts. Whether you're managing files, automating workflows, or simply learning about cloud storage operations, this project is designed to provide a hands-on approach to mastering AWS S3.