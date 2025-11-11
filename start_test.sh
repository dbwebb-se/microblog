#!/bin/bash
source .venv/bin/activate

echo "Starting test container..."
make test
echo "All tests finished. Shutting down."