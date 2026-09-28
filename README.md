# lab04-penguin

Lab 4 group project for Automated Software Testing — collaborative Git/GitHub workflow, pytest fixtures, tests, and merge conflict practice.

## Group Name

**PENGUINS**

---

## Who Did What

| Member Name | Student ID | GitHub Username | Role | Main File / Responsibility |
|---|---|---|---|---|
| Muhammad Hashir Khan | 6705142019 | hashirkhnn | Member A | `test_deposit.py` |
| Aung Khant Paing | 6705140082 | Trevor0v0 | Member B | `test_withdraw.py` |
| Sai Soom Rath | 6705142034 | SaiSoomRath | Member C | `test_teardown.py` |
| Pyae Phyo Paing | 6705142024 | Percy022 | Member D | `test_shared.py` |
| Ye Myat Aung | 6705142009 | bruh65251-cloud | Member E | `conftest.py` |

---

## Our Merge Conflict

A merge conflict occurred in `README.md` because multiple group members edited the **Who Did What** table at around the same time.

### Conflict Markers

```text
<<<<<<< HEAD
| <Pyae Phyo Paing> | <6705142024> | <Percy022> | Member D | test_shared.py |
| <Name> | <Student ID> | <username> | Member E | conftest.py |
=======
| <Name> | <Student ID> | <username> | Member D | test_shared.py |
| Ye Myat Aung | 6705142009 | bruh65251-cloud | Member E | conftest.py |
>>>>>>> 6d6481e9165fb4f66213226f95e2e30cc2f3f5f6
```

### Resolution

We first used `git merge --abort` to cancel the unfinished merge and return the repository to its previous state so we could review the conflicting changes clearly.

We then repeated the merge and resolved the conflict by combining the valid information from both versions of the table. The completed **Member D** row from the `HEAD` version and the completed **Member E** row from the incoming version were both kept, while the placeholder rows and conflict markers were removed.

After confirming that both members appeared correctly in the final `Who Did What` table, the resolved `README.md` was staged, committed as the merge-conflict resolution, and pushed to the shared GitHub repository.

---

## Git Contribution Summary

Output from `git shortlog -sn`:

```text
12  Ye Myat Aung - 6705142009
11  6705142034-Sai Soom Rath
 9  Pyae Phyo Paing - 6705142024
 9  Trevor0v0
 4  Muhammad Hashir Khan - 6705142019
 1  bruh65251-cloud
```
Note: bruh65251-cloud is an earlier commit made by Ye Myat Aung under the GitHub username, while Trevor0v0 corresponds to Aung Khant Paing (6705140082).

---

## Reflection Questions

### 1. Why was your push rejected, and how did you fix it?

The push was rejected because another group member had already pushed newer changes to the shared repository, so our local branch was out of date. We fixed it by running `git pull`, resolving the incoming changes if necessary, and then running `git push` again.

### 2. Why could Git not resolve the README conflict automatically?

Git could not resolve the conflict automatically because different group members changed the same section of the `Who Did What` table in `README.md`. Both versions contained valid but different updates in the same location, so Git could not decide which version should be kept and required us to resolve the conflict manually.

### 3. What is the difference between committing and pushing?

A commit saves a snapshot of the changes in the local Git repository on our computer. A push uploads those committed changes to the shared GitHub repository so the other group members can access them.

### 4. How do fixtures reduce duplicated setup code in tests?

Fixtures define reusable setup once and provide it automatically to any test that needs it. This avoids repeating the same object creation or preparation code in multiple test functions and keeps the tests cleaner and easier to maintain.