# Mini Store — Git/GitHub Workflow Exercise

This repository is the starter code for the in-class Modern Software Engineering Workflow practice.

## Before changing anything

Open the **entire folder** in VS Code.

The repository is preconfigured for Python `unittest` discovery in the VS Code Testing panel.

You should see five existing tests. Run all of them before making changes:

> **main starts green**

Do not run `tests/test_store.py` directly with **Run Python File**. Use the VS Code **Testing** panel and **Run All Tests**.

## Issues

### A — Free shipping
Orders with subtotal >= 1000 must return shipping cost `0.0`. Lower orders remain `99.0`.

### B — Discount validation
`apply_discount` must raise `ValueError` when `percent < 0` or `percent > 100`.

### C — Checkout item limit
`can_checkout` must return `False` for 0 items or more than 50 items, and `True` for 1–50.

### D — Loyalty discount
`loyalty_discount` returns:
- `0` below 500 points
- `5` from 500–999 points
- `10` at 1000+ points

## Team workflow

Each student takes one issue and:

1. Starts from the latest `main`.
2. Creates a separate feature branch.
3. Implements only the assigned issue.
4. Adds or updates at least one meaningful unit test.
5. Reviews the diff before committing.
6. Commits and pushes the branch.
7. Opens a Pull Request into `main`.
8. Waits for GitHub Actions CI.
9. Receives peer review and addresses at least one reasonable requested improvement.
10. Pushes again and waits for CI to rerun.
11. Merges only after CI is green and the reviewer approves.

## Optional command-line test

Terminal is **not required** for the exercise. For troubleshooting, the equivalent command is:

```bash
python3 -m unittest discover -s tests -v
```
