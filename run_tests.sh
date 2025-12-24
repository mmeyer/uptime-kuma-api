#!/usr/bin/env bash

version="$1"
if [ $version ]
then
  versions=("$version")
else
  versions=(2.0.2)
fi

for version in "${versions[@]}"
do
  echo "Starting uptime kuma $version..."
  docker run -d -it --rm -p 3001:3001 --name uptimekuma "louislam/uptime-kuma:$version" > /dev/null

  while [[ "$(curl -s -L -o /dev/null -w ''%{http_code}'' 127.0.0.1:3001)" != "200" ]]
  do
    sleep 0.5
  done

  sleep 5

  # Use sqlite database
  curl -X POST -H "Content-Type: application/json" -d '{"dbConfig":{"type":"sqlite"}}' http://127.0.0.1:3001/setup-database
  echo ""  # Line Break

  sleep 10

  # Send WebSocket message to setup admin user
  echo "Setting up admin user..."
  ./scripts/test_setup_admin.py

#  sleep 5
#
#  echo "Running tests..."
#  python -m unittest discover -s tests
#
#  echo "Stopping uptime kuma..."
#  docker stop uptimekuma > /dev/null
#  sleep 1

  echo ''
done
