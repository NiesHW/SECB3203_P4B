### Git


### Git Cheat Sheet
A Git cheat sheet is a quick reference guide that summarises commonly used Git commands and their syntax. It is a useful tool for developers who are new to Git or want to quickly lookup a command without searching through the Git documentation.

A typical Git cheat sheet will include commands for creating and managing repositories, making and committing changes, branching and merging code, and collaborating with others. Some of the most commonly included commands are:
- **git init**: Initializes a new Git repository in the current directory.
- **git add**: Adds files to the staging area to be committed.
- **git commit**: Commits changes to the repository with a message describing the changes.
- **git branch**: Lists or creates new branches for developing code.
- **git merge**: Merges changes from one branch into another.
- **git pull**: Fetches and merges changes from a remote repository.
- **git push**: Sends local changes to a remote repository.

Many Git cheat sheets will also include shorthand commands, such as using `-m` with the `git commit` command to add a message directly in the command line instead of opening a text editor.

### Installing Git
Installing Git is the first step to using it in your software development workflow. The Git documentation provides detailed instructions on how to install Git on various platforms, including Windows, Mac, and Linux.

The instructions typically involve downloading the Git installation package from the Git website and running the installer. The installer will guide you through the installation process, allowing you to customize the installation settings as needed.

Once Git is installed, you can use the Git command line interface to manage your repositories and perform version control tasks. You can also use Git GUI clients or integrated development environments (IDEs) that provide Git integration to make working with Git easier and more efficient.

By installing Git, you gain access to a powerful and flexible version control system that can help you track changes to your code and collaborate with others on development projects. The Git documentation provides comprehensive guidance on how to install and use Git effectively, making it easy for developers of all levels to get started with Git.

- [Git download page](https://git-scm.com/downloads)
- [Git installation instructions for each platform](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Some useful commands for getting started:

| Command | Explanation & Link |
| ----- | ----- | 
| [git clone URL](https://git-scm.com/docs/git-clone) | Git clone is used to clone a remote repository into a local workspace |
| [git push](https://git-scm.com/docs/git-push) | Git push is used to push commits from your local repo to a remote repo |
| [git pull](https://git-scm.com/docs/git-pull) | Git pull is used to fetch the newest updates from a remote repository |
| [git remote](https://git-scm.com/docs/git-remote) | List remote repos |
| [git remote -v](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emshowem) | List remote repos verbosely |
| [git remote show <name>](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emshowem) | Describes a single remote repo |
| [git remote update](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emupdateem) | Fetches the most up-to-date objects |
| [git fetch](https://git-scm.com/docs/git-fetch) | Downloads specific objects |
| [git checkout](https://git-scm.com/docs/git-checkout)| effectively used to switch branches |
| [git reset](https://git-scm.com/docs/git-reset#_examples)| basically resets the repo, throwing away some changes. It’s somewhat difficult to understand, so reading the examples in the documentation may be a bit more useful|
| [git commit --amend](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---amend)| is used to make changes to commits after-the-fact, which can be useful for making notes about a given commit.|
| [git revert](https://git-scm.com/docs/git-revert)| makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.|
| [git branch](https://git-scm.com/docs/git-branch) | Used to manage branches |
| [git branch -d <name>](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--D) | Deletes the branch |
| [git branch -D <name>](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--D) | Forcibly deletes the branch |
| [git branch -r](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--r) | Lists remote branches; can be combined with other branch arguments to manage remote branches |
| [git checkout <branch>](https://git-scm.com/docs/git-checkout) | Switches to a branch. |
| [git checkout -b <branch>](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt--bltnewbranchgt) |Creates a new branch and switches to it. |
| [git merge <branch>](https://git-scm.com/docs/git-merge) | Merge joins branches together. |
| [git merge --abort](https://git-scm.com/docs/git-merge) | If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action. |
| [git log --graph --oneline](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History) | This shows a summarized view of the commit history for a repo. |
