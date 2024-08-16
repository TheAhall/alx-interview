#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """Prints the cumulative metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 6:
            size = parts[-1]
            status = parts[-2]
            if status.isdigit():
                status = int(status)
                if status in status_codes:
                    status_codes[status] += 1
            try:
                total_size += int(size)
            except ValueError:
                pass
            line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

print_stats(total_size, status_codes)
