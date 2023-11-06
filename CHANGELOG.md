# Changelog for microblog

## Version 0.1.1

### Added
- **Docker Compose Setup**: Introduced `docker-compose.yml` to orchestrate the application, database, and testing containers. This enhancement improves local development and CI/CD processes by simplifying multi-container setups.
- **Dockerfile for Testing**: Added `Dockerfile_test` in the `docker` directory. This Dockerfile creates a dedicated environment for testing, ensuring tests run in an isolated and consistent setting.

### Chore
- **.dockerignore File**: Created a `.dockerignore` file in the `docker` directory. This file optimizes the Docker build context by excluding the `app` and `tests` directories, leading to faster image builds.

### Feature
- **Test Startup Script**: Added `test_startup.sh` script for executing tests in a Docker container. This script facilitates automated and reproducible test runs in a containerized environment.

## Version 0.1.0

### Added

- **Boot.sh Script**: Added a `boot.sh` script for managing Flask database upgrades and the startup of Gunicorn server. This script simplifies the process of setting up and running the Flask application, ensuring that the database schema is always up-to-date before starting the server.

- **Docker Support**:
  - Created `Dockerfile_prod` for an Alpine-based container setup, specifically tailored for Python 3.8.
  - This Dockerfile sets up an environment optimized for running the microblog application, ensuring portability and ease of deployment across different systems.
