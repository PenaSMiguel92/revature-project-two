These are the steps I follow:

git clone {link}
cd {repo folder}
You can check the status and which branch you are on using:

git status
git branch
git branch -a
Note: Here if you make changes in your local repo before moving to the new branch, the following steps should still work.

If "git branch" shows master, and you want to create+move to another branch:

git checkout -b {branch name}
Check branch again using "git branch" It should now show that you are in the new branch.

Now add, commit and push:

git add .
git commit -m "added new branch"
git push -u origin {branch name}

To pull changes:

git checkout main

git pull

To update your branch with changes.

git checkout {branch}

git rebase main