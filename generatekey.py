import uuid
from datetime import datetime, timedelta
import os
import argparse
import sys
from dateutil.relativedelta import relativedelta  # for months/years

# --- CLI Arguments ---
parser = argparse.ArgumentParser(description="Generate a key with an expiration date.")
parser.add_argument("--type", type=str, choices=["days", "weeks", "months", "years"], default="days",
                    help="Duration type (days, weeks, months, years)")
parser.add_argument("--value", type=int, default=1,
                    help="Number of units for duration")
args = parser.parse_args()

# --- Ensure keys directory exists ---
os.makedirs("keys", exist_ok=True)

# --- Generate a random UUID key ---
key = str(uuid.uuid4())

# --- Current time (UTC+8, Philippines time) ---
utc_now = datetime.utcnow() + timedelta(hours=8)

# --- Expiry calculation ---
if args.type == "days":
    expiry_date = utc_now + timedelta(days=args.value)
elif args.type == "weeks":
    expiry_date = utc_now + timedelta(weeks=args.value)
elif args.type == "months":
    expiry_date = utc_now + relativedelta(months=args.value)
elif args.type == "years":
    expiry_date = utc_now + relativedelta(years=args.value)
else:
    raise ValueError("Invalid duration type")

# --- Unique filename with timestamp ---
date_str = utc_now.strftime("%Y-%m-%d_%H%M%S")
filename = f"keys/key_{date_str}_{args.value}{args.type}.txt"

# --- Save key to file ---
with open(filename, "w") as f:
    f.write(f"Key: {key}\n")
    f.write(f"Issued: {utc_now.strftime('%Y-%m-%d %H:%M:%S')} UTC+8\n")
    f.write(f"Expires: {expiry_date.strftime('%Y-%m-%d %H:%M:%S')} UTC+8\n")
    f.write(f"Duration: {args.value} {args.type}\n")

# --- Detect if running inside GitHub Actions ---
if os.getenv("GITHUB_ACTIONS") == "true":
    # Only print filename for workflow parsing
    print(filename)
else:
    # Pretty output for manual run
    print(f"✅ Key generated: {filename}")
    print(f"   Duration : {args.value} {args.type}")
    print(f"   Issued   : {utc_now.strftime('%Y-%m-%d %H:%M:%S')} UTC+8")
    print(f"   Expires  : {expiry_date.strftime('%Y-%m-%d %H:%M:%S')} UTC+8")
