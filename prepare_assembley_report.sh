#!/bin/bash

# Check if input and output file arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 input_file output_file"
    exit 1
fi

input_file="$1"
output_file="$2"

# Use awk to remove all but the last instance of lines starting with #
awk '
{
    if ($0 ~ /^#/) {
        last_comment = substr($0, 2)
    } else {
        if (last_comment != "") {
            print last_comment
            last_comment = ""
        }
        print
    }
}
END {
    if (last_comment != "") {
        print last_comment
    }
}
' "$input_file" > "$output_file"