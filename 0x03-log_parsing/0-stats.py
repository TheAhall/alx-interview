#!/usr/bin/python3
"""
Log parsing script that reads from stdin and computes metrics.
"""

import sys

def print_stats(total_size, status_codes):
    """Prints the accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def log_parsing():
    """Parses logs from stdin and computes metrics."""
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 7:
                # Extract file size and status code
                try:
                    file_size = int(parts[-1])
                    status_code = int(parts[-2])

                    total_size += file_size

                    if status_code in status_codes:
                        status_codes[status_code] += 1

                except ValueError:
                    continue

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)

if __name__ == "__main__":
    log_parsing()
