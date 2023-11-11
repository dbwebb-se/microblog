# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- _No unreleased changes at this time._

## [1.0.0] - 2023-11-11

**Branch:** Push development branch to master branch to reflect kmom01 is done [PR 14 - "Development to Master (kmom01)"](https://github.com/FalkenDev/microblog/issues/14)
**Docs:** Changelog updated to reflect the new release [PR 13 - "Changelog Update"](https://github.com/FalkenDev/microblog/issues/13)

## [0.2.0] - 2023-11-08

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
