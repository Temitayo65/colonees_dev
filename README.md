# Colonees AI API

## Overview

Colonees AI API is a revolutionary project designed to simplify team building through advanced artificial intelligence (AI). This API provides a comprehensive set of endpoints to seamlessly create and manage teams, leveraging AI for enhanced collaboration and efficiency.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup (Heroku)](#database-setup-heroku)
- [Usage](#usage)
- [Contributing](#contributing)
- [Pull Request Template](#pull-request-template)

## Installation

Clone the repository to your local machine and navigate to the project directory. Install the project dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the Colonees AI API, make sure to configure the necessary environment variables. The following variables should be set with your specific values:

```bash
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=admin_password
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=database_password
DATABASE_NAME=database_name
DATABASE_USERNAME=database_username
SECRET_KEY=your_secret_key
ALGORITHM=HS256
# Set the expiration time in minutes
ACCESS_TOKEN_EXPIRATION_TIME=15  # 15 minutes


ZOHO_SMTP_SENDER_EMAIL = admin@example.com
ZOHO_SMTP_USERNAME = admin@example.com
ZOHO_SMTP_OUTGOING_SERVER_NAME = admin@example.com
ZOHO_SMTP_PASSWORD = zoho_smtp_password
ZOHO_SMTP_PORT_WITH_SSL = ssl_port
ZOHO_SMTP_PORT_WITH_TLS = tsl_port
ZOHO_SMTP_REQUIRE_AUTHENTICATION = Yes
```


## Database Setup (Heroku)
If you are hosting the Colonees AI API on Heroku with a Postgres database, follow these steps to set up the database.

### Step 1: Apply Migrations

Run the following command to apply database migrations:

```bash
heroku run alembic upgrade head --app your-heroku-app-name
```

## Usage

Colonees AI API serves as a powerful API for team building. Follow the instructions below to utilize the API effectively.

### Documentation

Access the API documentation by navigating to the root endpoint with the forward slash in front of the URL containing "docs," as in `/docs`. Explore the provided endpoints and learn how to leverage AI capabilities in creating, managing, and optimizing teams.

### Example

Navigate to the documentation endpoint:

```bash
https://your-api-url/docs
```

### Contributing


## Contributing

We welcome contributions from the community to enhance and improve the Colonees AI API. Before making any contributions, please follow the guidelines outlined below.

### How to Contribute

1. **Fork the Repository:** Start by forking the project on GitHub to create your copy of the repository. Click on the "Fork" button at the top right corner of the repository page.

2. **Clone Your Fork:** Clone your forked repository to your local machine. Use the following command, replacing `<your-username>` with your GitHub username:

    ```bash
    git clone https://github.com/<your-username>/Colonees/api.git
    ```

3. **Create a Branch:** Create a new branch for your feature or bug fix. Use a descriptive name for your branch:

    ```bash
    git checkout -b feature/your-feature
    ```

4. **Make Changes:** Implement your changes or additions. Ensure that your code follows the project's coding style and conventions.

5. **Run Tests:** If applicable, run the tests to ensure your changes do not introduce new issues:

    ```bash
    # Example command for running tests
    python -m unittest discover tests/
    ```

6. **Update Documentation:** If your changes affect the project's documentation, ensure it is updated accordingly.

7. **Commit Changes:** Commit your changes with a clear and concise commit message. Use present tense and follow the [Conventional Commits](https://www.conventionalcommits.org/) format:

    ```bash
    git commit -m "feat: add new feature"
    ```

8. **Push Changes:** Push your changes to your forked repository on GitHub:

    ```bash
    git push origin feature/your-feature
    ```

9. **Submit a Pull Request (PR):** Open a pull request against the `main` branch of the original repository. Ensure your PR has a clear title and description summarizing your changes.

10. **Code Review:** Your PR will be reviewed by project maintainers. Address any feedback or comments provided during the review.

### Pull Request Template

When submitting a pull request, use the following template:


## Description

Provide a clear and concise description of the changes introduced by this pull request.

## Related Issue

If this pull request is related to an existing issue, link the issue here.

## Type of Change

- [ ] Bug Fix
- [ ] New Feature
- [ ] Documentation Update
- [ ] Other (please specify)

## Checklist

- [ ] I have tested my changes.
- [ ] I have updated the documentation.
- [ ] My code follows the project's coding style.
- [ ] I have added/modified tests to cover my changes.

## Screenshots (if applicable)

Provide any screenshots or visual representations of your changes (if applicable).
