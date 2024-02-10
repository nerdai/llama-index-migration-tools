#!/bin/sh

find /Users/nerdai/Projects/migration/llama_index -name "pyproject.toml" > pypackages.txt

cat pypackages.txt | while read line
do
        echo $line
        llamaindex-migration update-pyproject -p $line;
        sed -i '' 's/flying-delta/llama-index/g' $line;
        cd / 
done
