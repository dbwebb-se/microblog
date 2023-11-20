# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- _No unreleased changes at this time._

## [2.0.0] - 2023-11-20

- **Branch:** Push development branch to master branch to reflect kmom02 is done [PR 36](https://github.com/FalkenDev/microblog/pull/36)
- **Docs:** Changelog updated to reflect the new release (Kmom02) - [PR 37](https://github.com/FalkenDev/microblog/pull/37)

## [1.1.3] - 2023-11-20

### Added

- **Feat:** Added app_version env and arg in dockerfile_prod - [PR 35](https://github.com/FalkenDev/microblog/pull/35)

## [1.1.2] - 2023-11-20

### Changed

- **Test** - Test code to see if the appservers in azure updates - [PR 34](https://github.com/FalkenDev/microblog/pull/34)

## [1.1.1] - 2023-11-20

### Fixed

- **Fix:** Rename DOCKER_TAG to APP_VERSION - [PR 32](https://github.com/FalkenDev/microblog/pull/32)
- **Fix:** Trying to fix app version route - [PR 33](https://github.com/FalkenDev/microblog/pull/33)

## [1.1.0] - 2023-11-20

### Added

- **CD:** Added public ssh keys for ansible - [PR 15](https://github.com/FalkenDev/microblog/pull/15)
- **Dbwebb:** New provisioning and terminate structure. More than halves execution - [PR 15](https://github.com/FalkenDev/microblog/pull/15)
- **Dbwebb:** Adds 10-first-minutes playbook - [PR 15](https://github.com/FalkenDev/microblog/pull/15)
- **Build:** Added users_users var with the ssh keys - [PR 17](https://github.com/FalkenDev/microblog/pull/17)
- **Build:** Added password to root - [PR 17](https://github.com/FalkenDev/microblog/pull/17)
- **Build:** Added task to install docker - [PR 18](https://github.com/FalkenDev/microblog/pull/18)
- **Build:** Added playbook docker-mysql - [PR 18](https://github.com/FalkenDev/microblog/pull/18)
- **Build:** Added task to run a mysql docker container - [PR 18](https://github.com/FalkenDev/microblog/pull/18)
- **Build:** Added new appserver as well as subdomains for each appserver - [PR 20](https://github.com/FalkenDev/microblog/pull/20)
- **Build:** Added published_ports for appservers to connect to mysql - [PR 21](https://github.com/FalkenDev/microblog/pull/21)
- **Build:** Added playbook for appserver for deployment - [PR 21](https://github.com/FalkenDev/microblog/pull/21)
- **Build:** Added task to start the microblog docker container - [PR 21](https://github.com/FalkenDev/microblog/pull/21)
- **Build:** Workflow file for deploying release - [PR 24](https://github.com/FalkenDev/microblog/pull/24)
- **Feat:** Creates DNS A records for appservers - [PR 24](https://github.com/FalkenDev/microblog/pull/24)
- **Fix:** Added subdomain hosts - [PR 24](https://github.com/FalkenDev/microblog/pull/24)
- **Feat:** Added subdomain for the database - [PR 25](https://github.com/FalkenDev/microblog/pull/25)

### Changed

- **Dbwebb:** Updates ansible to new structure - [PR 15](https://github.com/FalkenDev/microblog/pull/15)
- **Dbwebb:** Cleans up new ansible code - [PR 15](https://github.com/FalkenDev/microblog/pull/15)
- **Dbwebb:** Cleans up vars file from my info - [PR 15](https://github.com/FalkenDev/microblog/pull/15)
- **Build:** Updated to look for azure ssh keys using users_users var for the file names - [PR 17](https://github.com/FalkenDev/microblog/pull/17)
- **Chore:** Updated .gitignore with ansible/group_vars/all.yml and Makefile - [PR 21](https://github.com/FalkenDev/microblog/pull/21)
- **Build:** Moved the pip3 install and docker sdk to docker-install ansible - [PR 21](https://github.com/FalkenDev/microblog/pull/21)
- **Docs:** Updated Changelog to reflect the new builds and fixes - [PR 22](https://github.com/FalkenDev/microblog/pull/22)
- **Build:** Playbook for updating docker images - [PR 24](https://github.com/FalkenDev/microblog/pull/24)

### Fixed

- **Dbwebb:** Small fixes - [PR 15](https://github.com/FalkenDev/microblog/pull/15)
- **Build:** Fixed python interpreter .venv to use just venv - [PR 17](https://github.com/FalkenDev/microblog/pull/17)
- **Fix:** - Gitignore fix - [PR 23](https://github.com/FalkenDev/microblog/pull/23)
- **Fix:** Fixed subdomain hosts - [PR 24](https://github.com/FalkenDev/microblog/pull/24)

### Removed

- **Chore:** Stop tracking group_vars/all.yml because of personal data - [PR 21](https://github.com/FalkenDev/microblog/pull/21)
- **Chore:** Stop tracking Makefile because of personal data - [PR 21](https://github.com/FalkenDev/microblog/pull/21)

## [1.0.0] - 2023-11-11

### Added / Changed

- **Branch:** Push development branch to master branch to reflect kmom01 is done [PR 14 - "Development to Master (kmom01)"](https://github.com/FalkenDev/microblog/issues/14)
- **Docs:** Changelog updated to reflect the new release [PR 13 - "Changelog Update"](https://github.com/FalkenDev/microblog/issues/13)

## [0.2.0] - 2023-11-08

### Added

- **Feat:** User Follow/Unfollow Functionality [PR 12 - "Implement User Follow/Unfollow Functionality"](https://github.com/FalkenDev/microblog/pull/12)

## [0.1.0] - 2023-11-06

### Added

- **Refactor:** Microblog configuration added [PR 2 - "Update microblog configuration"](https://github.com/FalkenDev/microblog/pull/2)
- **Chore:** Introduced git commit message template to standardize contributions [PR 2 - "Add commit template"](https://github.com/FalkenDev/microblog/pull/2)
- **Build:** Production-ready Dockerfile added for Microblog deployment [PR 2 - "Add Dockerfile for production"](https://github.com/FalkenDev/microblog/pull/2)
- **Build:** Script for starting the web server (`boot.sh`) implemented [PR 2 - "Add webserver start script"](https://github.com/FalkenDev/microblog/pull/2)
- **Docs:** Changelog initiated to document project evolution [PR 2 - "Initialize CHANGELOG.md"](https://github.com/FalkenDev/microblog/pull/2)
- **CI:** Continuous integration setup with GitHub Actions for automated testing and code validation [PR 3 - "Set up Python CI"](https://github.com/FalkenDev/microblog/pull/3)
- **Chore:** GitHub Pull Request template added to standardize contributions [PR 5 - "Add Pull Request template"](https://github.com/FalkenDev/microblog/pull/5)
- **CD:** Continuous deployment workflow for Docker image publishing [PR 7 - "Setup Docker image CD"](https://github.com/FalkenDev/microblog/pull/7)
- **Build:** Essential Docker setup and configuration for production and testing environments [PR 9 - "Configure Docker setup"](https://github.com/FalkenDev/microblog/pull/9)

### Changed

- **Docs:** Changelog updated to reflect new features and bug fixes [PR 6 - "Update Changelog"](https://github.com/FalkenDev/microblog/pull/6)
- **CD:** Docker CD workflow modified to use release tag names [PR 8 - "Modify Docker CD to use tags"](https://github.com/FalkenDev/microblog/pull/8)
- **CD:** Docker image CD pipeline adjusted to publish images for both testing and production [PR 10 - "Adjust Docker image CD pipeline"](https://github.com/FalkenDev/microblog/pull/10)
- **Docs:** Changelog updated to reflect new features and bug fixes [PR 11 - "Update Changelog"](https://github.com/FalkenDev/microblog/pull/11)

### Fixed

- **Fix:** Pinned SQLAlchemy to a specific version for compatibility, incorporating changes from dbwebb-se's master branch. [PR 1 - "Fix SQLAlchemy version"](https://github.com/FalkenDev/microblog/pull/1) - [dbwebb-se - "Added version for SQLAlchemy"](https://github.com/dbwebb-se/microblog/commit/372175c4b499e62167230025ea6aeca787bbcb8b)
- **CI:** Resolved branch naming issues in CI tests, separated unit tests from integration tests, and refined pip install process for testing [PR 4 - "Fix Python CI tests"](https://github.com/FalkenDev/microblog/pull/4)
