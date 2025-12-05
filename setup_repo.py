import os
import json

TOTAL_DAYS = 100

# Create beginner practice folder
os.makedirs("beginner-small-codes", exist_ok=True)

with open("beginner-small-codes/README.md", "w") as f:
    f.write("# Beginner Small Codes\n\n")
    f.write("This folder contains small Python practice scripts.\n")

for day in range(1, TOTAL_DAYS + 1):
    folder_name = f"Day{day:02d}"
    os.makedirs(folder_name, exist_ok=True)

    with open(os.path.join(folder_name, "main.py"), "w") as f:
        f.write(f"# Day {day:02d} – Python Code\n")

    with open(os.path.join(folder_name, "notes.md"), "w") as f:
        f.write(f"# Day {day:02d} – Notes\n")

    project_info = {
        "day": day,
        "topic": "",
        "project_name": "",
        "status": "Not started",
        "summary": "",
    }

    with open(os.path.join(folder_name, "project.json"), "w") as f:
        json.dump(project_info, f, indent=4)

print("🔥 Repo structure created successfully!")
