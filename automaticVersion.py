import datetime
import re

def get_version_code():
    # Get today's date
    today = datetime.datetime.now().strftime("%y%m%d")
    
    # Read the pubspec.yaml file
    with open("pubspec.yaml", "r") as f:
        content = f.read()

    # Extract the version code from the file
    version_code_match = re.search(r'^version:\s+(\d+\.\d+\.\d+)\+(\d+)$', content, re.MULTILINE)
    if version_code_match:
        version_code = version_code_match.group(2)
        # Check if the version code follows the convention (YYMMDDNN)
        if version_code[:6] == today:
            # Extract the build count and increment it by 1
            build_count = int(version_code[6:]) + 1
        else:
            # If it doesn't align with today's date, start from 1
            build_count = 1
    else:
        # If the version code is not found, start from 1
        build_count = 1

    # Format the version code with the date and build count
    version_code = f"{today}{build_count:02}"

    return version_code

def update_pubspec_yaml(version_name, version_code):
    # Read the pubspec.yaml file
    with open("pubspec.yaml", "r") as f:
        content = f.read()

    # Update the version field with version name + version code
    updated_content = re.sub(r'^(version:\s+\d+\.\d+\.\d+)\+\d+$', f"version: {version_name}+{version_code}", content, flags=re.MULTILINE)

    # Write the updated content back to the file
    with open("pubspec.yaml", "w") as f:
        f.write(updated_content)

# Allow user to input the version name
version_name = input("Enter the version name: ")

# Get the version code
version_code = get_version_code()

# Update pubspec.yaml with the version name and version code
update_pubspec_yaml(version_name, version_code)

print(f"Updated pubspec.yaml with version name: {version_name} and version code: {version_code}")
