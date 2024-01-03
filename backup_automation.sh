#!/bin/bash

# Function to display script usage
usage() {
    echo "Usage: $0 -d <directory1 directory2 ...> -b <backup_location> -i <interval_seconds> -n <num_backups>"
    exit 1
}

# Initialize variables with default values
directories=()
backup_location=""
interval_seconds=5 # Default: 
num_backups=5          # Default: keep 5 backup versions

# Parse command-line options
while getopts ":d:b:i:n:" opt; do
    case $opt in
        d)
            directories+=("$OPTARG")

            ;;
        b)
            backup_location="$OPTARG"
            ;;
        i)
            interval_seconds="$OPTARG"
            ;;
        n)
            num_backups="$OPTARG"
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            usage
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            usage
            ;;
    esac
done

# Ensure required options are provided
if [ "${#directories[@]}" -eq 0 ] || [ -z "$backup_location" ]; then
    usage
fi

# Infinite loop for periodic backups
while true; do
    # Create timestamp for the backup folder
    timestamp=$(date +%Y%m%d%H%M%S)
    backup_folder="$backup_location/backup_$timestamp"

    # Create backup folder
    mkdir -p "$backup_folder"

    # Copy contents of specified directories to the backup folder
    for dir in "${directories[@]}"; do
        cp -r "$dir" "$backup_folder"
    done

    # Remove older backups if more than specified number of backups exist
    backup_list=($(ls -d "$backup_location"/backup_* 2>/dev/null))
    num_backups_to_remove=$(( ${#backup_list[@]} - num_backups ))
    if [ $num_backups_to_remove -gt 0 ]; then
        # Create an array of backups and sort them by modification time
        mapfile -t sorted_backups < <(ls -t "$backup_location"/backup_* 2>/dev/null)

        # Remove the oldest backups
        for ((i = $num_backups; i < ${#sorted_backups[@]}; i++)); do
            rm -r "${sorted_backups[$i]}"
        done
    fi

    echo "Backup completed successfully! Timestamp: $timestamp"

    # Sleep for the specified interval before the next backup
    sleep "$interval_seconds"
done
