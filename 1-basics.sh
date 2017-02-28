#!/usr/bin/env bash
set -x

echo "Eval directly works"
redis-cli eval "return {KEYS[1] + KEYS[2]}" 2 2 2

echo "Registering a script"
output=$(redis-cli script load "return {KEYS[1] + KEYS[2]}")

echo "Execute a script"
redis-cli evalsha "$output" 2 2 2
