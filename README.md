# 📘 LeetCode DSA Practice Roadmap

Welcome to my LeetCode **Data Structures & Algorithms (DSA)** journey!  
This repository tracks my progress through a structured learning path with automation, clean solutions, and visual documentation — all aimed at mastering DSA for technical interviews.

---

## 🚀 Overview

- **🎯 Goal**: Solve 200+ LeetCode problems to build a strong DSA foundation.
- **🧠 Approach**: Follow a curated roadmap, write clean Python solutions, and document explanations.
- **⚙️ Tools**: Python, GitHub Actions (automation), and Mermaid.js (visualization).

---

## 🧭 DSA Roadmap (Visual)

> ℹ️ GitHub doesn't render Mermaid directly — use [Mermaid Live Editor](https://mermaid.live/edit) to view this chart.

<details>
<summary>🗺️ Click to view the visual roadmap</summary>

```mermaid
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
````

</details>

---

## ✅ Topic Progress

| Topic                    | Status         | Notes                               |
| ------------------------ | -------------- | ----------------------------------- |
| Arrays & Strings         | 🟩 In Progress | Sliding window, string manipulation |
| Hash Maps                | ⬜ Pending      | Frequency maps, fast lookups        |
| Two Pointers             | ⬜ Pending      | Opposite ends, sorted arrays        |
| Stacks & Queues          | ⬜ Pending      | Monotonic stacks, BFS logic         |
| Binary Search            | ⬜ Pending      | Search space optimization           |
| Linked Lists             | ⬜ Pending      | Slow/fast pointers, reversals       |
| Trees - DFS/BFS          | ⬜ Pending      | Traversals, recursion               |
| Recursion & Backtracking | ⬜ Pending      | Subsets, permutations               |
| Dynamic Programming (DP) | ⬜ Pending      | Memoization, tabulation             |
| Graphs                   | ⬜ Pending      | DFS, BFS, shortest paths            |

---

## 📂 Repository Structure

Organized by topic for easy navigation:

```
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
```

Each folder contains:

* 🔗 LeetCode problem links
* 💻 Python solutions
* 🧠 Explanations
* ⏱️ Time/Space complexity analysis

---

## 📚 Resources

Here are some great resources I rely on:

* [📘 LeetCode Profile](https://leetcode.com/)
* [📺 NeetCode DSA Roadmap](https://neetcode.io/)
* [📙 GeeksForGeeks](https://www.geeksforgeeks.org/)
* [🧮 Visualgo](https://visualgo.net/en)

---

## 📈 GitHub Stats & Automation

This repo uses **GitHub Actions** to auto-update problem and last-update badges every day.

### GitHub Workflow

```yaml
# .github/workflows/update-badge.yml
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
```

### Initialize badges manually (one-time):

```bash
mkdir -p .github/badges
echo '{"label":"Problems Solved","message":"0","color":"blue"}' > .github/badges/problems_solved.json
echo '{"label":"Last Updated","message":"N/A","color":"green"}' > .github/badges/last_updated.json
```

---

## 🙌 Let's Connect

Feel free to:

* ⭐ Star this repo
* 🛠️ Fork and contribute
* 💬 Connect on [GitHub](https://github.com/Laudarisd) or [LeetCode](https://leetcode.com/)

Happy coding! 🚀


