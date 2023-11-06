# Changelog for microblog

## Version 0.1.0

### Added

- **Boot.sh Script**: Added a `boot.sh` script for managing Flask database upgrades and the startup of Gunicorn server. This script simplifies the process of setting up and running the Flask application, ensuring that the database schema is always up-to-date before starting the server.

- **Docker Support**:
  - Created `Dockerfile_prod` for an Alpine-based container setup, specifically tailored for Python 3.8.
  - This Dockerfile sets up an environment optimized for running the microblog application, ensuring portability and ease of deployment across different systems.
