n=1; for file in *.jpg; do mv "$file" "${PWD##*/}-$n.jpg"; n=$((n + 1)); done
