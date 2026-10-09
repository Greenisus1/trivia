#!/bin/bash
# pi-app-store: 1
# pi-app-store-category: learning-games
# pi-app-store-description: Offline multiple-choice learning quizzes: arithmetic, geometry, Python basics, word puzzles and logic. Generated fixed question bank, no web or AI.
set -eu
cd -- "$(dirname -- "$0")"
case "${1:-}" in
 install) python3 -c 'from pathlib import Path;[compile(p.read_bytes(),str(p),"exec") for p in Path(".").glob("*.py")]' ;;
 run) shift; exec python3 game.py "$@" ;;
 *) echo 'Use: bash app-store.sh install OR bash app-store.sh run';exit 1 ;;
esac
