import os
import sys

REQUIRED_MODULES = ['discord', 'openai', 'dotenv']
missing = []
for mod in REQUIRED_MODULES:
    try:
        __import__(mod)
    except ImportError:
        missing.append(mod)
if missing:
    print(f"Error: Missing Python modules: {', '.join(missing)}")
    print("Install them with: pip install -r requirements.txt")
    sys.exit(1)

REQUIRED_ENVS = ['DISCORD_TOKEN', 'OPENAI_API_KEY']
missing_env = [e for e in REQUIRED_ENVS if not os.getenv(e)]
if missing_env:
    print(f"Error: Missing environment variables: {', '.join(missing_env)}")
    print("Create a .env file or set them in your shell environment.")
    sys.exit(1)

print("Setup check passed. You have all dependencies and environment variables configured.")