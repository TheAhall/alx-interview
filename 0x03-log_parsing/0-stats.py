#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Print the current statistics."""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def signal_handler(sig, frame):
    """Handle the keyboard interrupt signal."""
    print_stats()
    sys.exit(0)

# Set up the signal handler for keyboard interruption (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Ensure the line has at least 2 parts (status code and file size)
        if len(parts) < 2:
            continue

        # Extract the status code and file size
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue

        # Update total file size
        total_size += file_size

        # Update the status code count
        if status_code in status_counts:
            status_counts[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle keyboard interruption
    print_stats()
    sys.exit(0)
