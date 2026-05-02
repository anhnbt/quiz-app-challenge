import re
import subprocess
import time

def get_existing_issues():
    cmd = ["gh", "issue", "list", "--limit", "100", "--json", "title"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return []
    import json
    issues = json.loads(result.stdout)
    return [i["title"] for i in issues]

def create_issue(title, body, priority):
    labels = ["user-story"]
    if priority == "P0":
        labels.append("p0")
    elif priority == "P1":
        labels.append("p1")
    elif priority == "P2":
        labels.append("p2")
    
    cmd = [
        "gh", "issue", "create",
        "--title", title,
        "--body", body,
        "--label", ",".join(labels)
    ]
    
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Created: {title}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating {title}: {e.stderr}")

def main():
    existing_titles = get_existing_issues()
    
    with open("tasks/README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Improved pattern to match all rows
    pattern = r"\| \*\*([^*]+)\*\* \| \*\*([^*]+)\*\* \| ([^|]+) \| [^|]+ \| ([^|]+) \|"
    matches = re.findall(pattern, content)

    for us_id, title, priority, ac in matches:
        full_title = f"[{us_id.strip()}] {title.strip()}"
        if full_title in existing_titles:
            print(f"Skipping (exists): {full_title}")
            continue
            
        body = f"## 👤 User Story\n{title.strip()}\n\n## ✅ Acceptance Criteria (AC)\n{ac.strip().replace('<br>', '\n')}\n\n## 🚩 Priority\n{priority.strip()}"
        create_issue(full_title, body, priority.strip())
        time.sleep(1)

if __name__ == "__main__":
    main()
