LeetCode DSA Practice Roadmap

Welcome to my LeetCode Data Structures & Algorithms (DSA) journey! This repository tracks my progress through structured challenges, with automated badges and a clear roadmap to master DSA for technical interviews.

🚀 Overview

Goal: Solve 200+ LeetCode problems to build a strong DSA foundation.
Approach: Follow a curated roadmap, write clean solutions, and document explanations.
Tools: Python, GitHub Actions for automation, Mermaid.js for visualizations.


🧭 DSA Roadmap
Visualize my learning path:
graph TD
  A[Arrays & Strings] --> B[Hash Maps]
  B --> C[Two Pointers]
  C --> D[Stacks & Queues]
  D --> E[Binary Search]
  E --> F[Linked Lists]
  F --> G[Trees - DFS/BFS]
  G --> H[Recursion & Backtracking]
  H --> I[Dynamic Programming - DP]
  I --> J[Graphs]


✅ Topic Progress
Track my progress through each DSA topic:



Topic
Status
Notes



Arrays & Strings
✅ In Progress
Sliding window, string manipulation


Hash Maps
⬜ Pending
Frequency maps, fast lookups


Two Pointers
⬜ Pending
Opposite ends, sorted arrays


Stacks & Queues
⬜ Pending
Monotonic stacks, BFS logic


Binary Search
⬜ Pending
Search space optimization


Linked Lists
⬜ Pending
Slow/fast pointers, reversals


Trees - DFS/BFS
⬜ Pending
Traversals, recursion


Recursion & Backtracking
⬜ Pending
Subsets, permutations


Dynamic Programming - DP
⬜ Pending
Memoization, tabulation


Graphs
⬜ Pending
DFS, BFS, shortest paths



📂 Repository Structure
Organized by topic for easy navigation:
📁 leetcode/
├── 📁 Arrays-Strings/
├── 📁 HashMaps/
├── 📁 TwoPointers/
├── 📁 Stacks-Queues/
├── 📁 BinarySearch/
├── 📁 LinkedLists/
├── 📁 Trees/
├── 📁 Recursion/
├── 📁 DP/
├── 📁 Graphs/
└── 📄 README.md

Each folder contains:

🔗 LeetCode problem links
💻 Solution code (Python)
🧠 Explanations
⏱️ Time/Space complexity analysis


📚 Resources
Key resources I use:

LeetCode Profile
NeetCode Roadmap
GeeksForGeeks
Visualgo


📈 GitHub Stats


⚙️ Automation: GitHub Actions
A GitHub Action updates the problem count and last-updated badges automatically:
.github/workflows/update-badge.yml:
name: Update Problem Count Badge

on:
  push:
    paths:
      - '**.py'
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight UTC

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Count .py files
        run: |
          count=$(find . -name "*.py" | wc -l)
          mkdir -p .github/badges
          echo "{\"label\":\"Problems Solved\",\"message\":\"$count\",\"color\":\"blue\"}" > .github/badges/problems_solved.json
          echo "{\"label\":\"Last Updated\",\"message\":\"$(date +'%Y-%m-%d')\",\"color\":\"green\"}" > .github/badges/last_updated.json
      - name: Commit & Push
        run: |
          git config --global user.name 'github-actions'
          git config --global user.email 'actions@github.com'
          git add .github/badges/*.json
          git commit -m "🔄 Auto-update badges"
          git push

Initialize badges:
mkdir -p .github/badges
echo '{"label":"Problems Solved","message":"0","color":"blue"}' > .github/badges/problems_solved.json
echo '{"label":"Last Updated","message":"N/A","color":"green"}' > .github/badges/last_updated.json




🙌 Let's Connect
Fork this repo, submit PRs, or follow my journey! Connect with me on LeetCode or GitHub.
Happy coding! 🚀
