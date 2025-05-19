# LeetCode DSA Practice Roadmap

![Problems Solved](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Laudarisd/leetcode/main/.github/badges/problems_solved.json)
![Last Updated](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Laudarisd/leetcode/main/.github/badges/last_updated.json)
![GitHub Workflow](https://github.com/Laudarisd/leetcode/actions/workflows/update-badge.yml/badge.svg)

This repository tracks my journey through LeetCode's **Data Structures & Algorithms (DSA)** challenges using a structured roadmap and automated progress tracking.

---

## 🧭 DSA Roadmap (via Mermaid.js)

```mermaid
graph TD
  A[Arrays & Strings] --> B[Hash Maps]
  B --> C[Two Pointers]
  C --> D[Stacks & Queues]
  D --> E[Binary Search]
  E --> F[Linked Lists]
  F --> G[Trees (DFS/BFS)]
  G --> H[Recursion & Backtracking]
  H --> I[Dynamic Programming (DP)]
  I --> J[Graphs]
````

---

## ✅ Topic Tracker

| Topic                    | Status        | Notes                           |
| ------------------------ | ------------- | ------------------------------- |
| Arrays & Strings         | ✅ In Progress | Basic patterns, sliding window  |
| Hash Maps                | ⬜️ Pending    | Frequency maps, lookups         |
| Two Pointers             | ⬜️ Pending    | Sorting, opposite ends          |
| Stacks & Queues          | ⬜️ Pending    | Monotonic stacks, BFS logic     |
| Binary Search            | ⬜️ Pending    | Search space, upper/lower bound |
| Linked Lists             | ⬜️ Pending    | Slow/fast pointers              |
| Trees (DFS/BFS)          | ⬜️ Pending    | Traversals, recursion           |
| Recursion & Backtracking | ⬜️ Pending    | Subsets, permutations           |
| Dynamic Programming (DP) | ⬜️ Pending    | Memoization, tabulation         |
| Graphs                   | ⬜️ Pending    | DFS, BFS, Dijkstra, Union-Find  |

---

## 📂 Folder Structure

```
📁 leetcode/
├── Arrays-Strings/
├── HashMaps/
├── TwoPointers/
├── Stacks-Queues/
├── BinarySearch/
├── LinkedLists/
├── Trees/
├── Recursion/
├── DP/
├── Graphs/
└── README.md
```

---

## 📘 Notes & Resources

Each solution includes:

* 🔗 Problem link
* 💻 Code
* 🧠 Explanation
* ⏱️ Time/Space complexity

Helpful Resources:

* [LeetCode](https://leetcode.com/u/dbBO1xrtst/)
* [NeetCode Roadmap](https://neetcode.io/)
* [GeeksForGeeks](https://www.geeksforgeeks.org/)
* [Visualgo](https://visualgo.net/en)

---

## 📈 GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Laudarisd\&show_icons=true\&theme=radical)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Laudarisd\&layout=compact\&theme=radical)

---

## ⚙️ GitHub Action: Auto Update Progress

Create the workflow file at `.github/workflows/update-badge.yml`:

```yaml
name: Update Problem Count Badge

on:
  push:
    paths:
      - '**.py'
  schedule:
    - cron: '0 0 * * *'  # every day at midnight UTC

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Count .py files (1 problem = 1 solution)
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
          git commit -m "🔄 Auto update problem count"
          git push
```

Also, create dummy JSON badge files:

```bash
mkdir -p .github/badges
echo '{"label":"Problems Solved","message":"0","color":"blue"}' > .github/badges/problems_solved.json
echo '{"label":"Last Updated","message":"N/A","color":"green"}' > .github/badges/last_updated.json
```

---

## 🏁 Goal

🎯 Solve **200+ structured LeetCode problems** to master Data Structures & Algorithms and ace technical interviews.

---

## 🙌 Let's Connect

If you find this helpful, feel free to fork this repo, submit PRs, or follow my journey.

Happy coding! 🚀

```

