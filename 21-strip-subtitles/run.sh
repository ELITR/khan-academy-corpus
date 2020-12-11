#!/bin/bash

export PYTHONPATH=$PYTHONPATH:../scripts

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

mkdir -p $DIR/data

ls -1 $DIR"/../11-download/data" | $DIR/batch.sh