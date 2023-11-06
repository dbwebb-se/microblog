# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

X.X.X - Kmom.Feature.SmallFixes

## [Unreleased]

### Added

- **Refactor:** Updated to use app.config (microblog.py) [PR 2 - initial](https://github.com/FalkenDev/microblog/pull/2)
- **Chore:** Added git commit template (gitConfigs/commit-conventions.txt) [PR 2 - initial](https://github.com/FalkenDev/microblog/pull/2)
- **Build:** Docker build for prod the microblog (Dockerfile_prod) [PR 2 - initial](https://github.com/FalkenDev/microblog/pull/2)
- **Build:** Added script to start the webserver (boot.sh) [PR 2 - initial](https://github.com/FalkenDev/microblog/pull/2)
- **Docs:** Added Changelog for version history (CHANGELOG.md) [PR 2 - initial](https://github.com/FalkenDev/microblog/pull/2)
- **CI:** Added CI for python to unit tests, integration tests and validate the code. (GitHub Actions) [PR 3 - python-ci-tests](https://github.com/FalkenDev/microblog/pull/3)
- **Chore:** Added template for [PR 5 - Github-Configs](https://github.com/FalkenDev/microblog/pull/5)

### Changed

### Deprecated

### Removed

### Fixed

- **Fix:** Added version for SQLAlchemy [PR 1 - dbwebb-se:master](https://github.com/FalkenDev/microblog/pull/1)
- **CI:** Python CI Tests: Fixed the strings on branch names. Added to run unit tests and integration tests seperate. Fixed the pip install to use folder requirements when install test.txt. [PR 4 - python-ci-tests](https://github.com/FalkenDev/microblog/pull/4)

### Security
