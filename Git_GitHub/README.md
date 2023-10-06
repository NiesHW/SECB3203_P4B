# GitHub
GitHub is a web-based platform that provides hosting for software development and version control using Git. It is a popular platform for collaboration and sharing of code among developers. GitHub was launched in 2008 and was later acquired by Microsoft in 2018.
GitHub provides a range of features that make it easy for developers to collaborate on projects, manage version control, and streamline their software development workflows. Some of the key features of GitHub include:
1. **Repositories**: GitHub provides a platform for developers to store and manage their code repositories. Each repository contains a collection of files that make up a project or a portion of a project.
2. **Pull requests**: GitHub's pull request feature allows developers to review and discuss code changes before they are merged into the main codebase. This can help ensure that code changes are of high quality and don't introduce bugs or conflicts.
3. **Issue tracking**: GitHub's issue tracking system allows developers to create and track bugs, feature requests, and other issues related to a project. Issues can be assigned to specific developers, labelled, and prioritized to help manage the development process.
4. **Collaboration tools**: GitHub provides a range of collaboration tools, such as inline commenting and mentions, that allow developers to communicate and collaborate on code changes in real time.
5. **Continuous integration and deployment**: GitHub integrates with a range of continuous integration and deployment tools, such as Travis CI and CircleCI. This allows developers to automate their build and deployment processes and ensure that their code is always up-to-date and error-free.
6. **Project management**: GitHub provides a range of project management tools, such as boards, milestones, and deadlines, to help developers track and manage their software development projects.
7. **Analytics and insights**: GitHub provides a range of analytics and insights tools, such as code frequency graphs and commit activity charts, to help developers track their progress and identify areas for improvement.
8. **Documentation and Wikis**: GitHub includes features for creating documentation and wikis associated with projects. This helps developers maintain comprehensive documentation and share knowledge with other team members and users.
9. **Extensibility**: GitHub offers an extensive ecosystem of integrations, plugins, and APIs. Developers can enhance their workflow by integrating GitHub with various tools and services, such as project management platforms, code quality analyzers, and communication tools.
10. **Social Coding**: GitHub encourages social interaction and knowledge sharing within the developer community. Developers can follow repositories, star projects they find interesting, and contribute to open-source projects. They can also discover trending repositories, explore different programming languages, and learn from other developers' code.
Overall, GitHub has become a central hub for software development, particularly for open-source projects. Its features and tools make it easy for developers to collaborate and share code, manage version control, and streamline their software development workflows.


## GitHub Cheat Sheet
A GitHub cheat sheet is a reference guide that provides a quick overview of the most commonly used commands and features in GitHub. It can be a handy resource for developers who are new to GitHub or who want a quick reference to the most important commands and features. Some common items that might be included in a GitHub cheat sheet include:
1. [**Git commands**](https://education.github.com/git-cheat-sheet-education.pdf): Many GitHub cheat sheets include a list of basic Git commands, such as git add, git commit, git push, and git pull. These commands are used to manage version control in GitHub repositories.
2. [**GitHub commands**](https://training.github.com/downloads/github-git-cheat-sheet/): The cheat sheet might also include a list of basic GitHub commands, such as git clone, git fork, and git merge. These commands are used to collaborate on GitHub projects and manage issues and pull requests.
3. [**Markdown syntax**](https://www.markdownguide.org/cheat-sheet/): GitHub uses a flavor of Markdown for formatting text in issues, pull requests, and README files. A cheat sheet might include a list of basic Markdown syntax, such as how to create headers, links, and lists.
4. [**Keyboard shortcuts**](https://docs.github.com/en/get-started/using-github/keyboard-shortcuts): GitHub has a number of keyboard shortcuts that can help speed up your workflow. A cheat sheet might include a list of common shortcuts, such as how to navigate between tabs, search for code, and create new files.


# Git
Git is a free and open-source version control system, originally created by Linus Torvalds in 2005. Unlike older centralized version control systems such as SVN and CVS, Git is distributed: every developer has the full history of their code repository locally. This makes the initial clone of the repository slower, but subsequent operations such as commit, blame, diff, merge, and log dramatically faster.
Git also has excellent support for branching, merging, and rewriting repository history, which has led to many innovative and powerful workflows and tools. Pull requests are one such popular tool that allows teams to collaborate on Git branches and efficiently review each other's code. Git is the most widely used version control system in the world today and is considered the modern standard for software development.


## Git Cheat Sheet
A Git cheat sheet is a quick reference guide that summarises commonly used Git commands and their syntax. It is a useful tool for developers who are new to Git or want to quickly look up a command without searching through the Git documentation.
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


### Some popular Git tutorials include:
1. [**Git Tutorial by Atlassian**](https://www.atlassian.com/git/tutorials): This tutorial covers the basics of Git, including creating a repository, making changes, and collaborating with others. It also includes advanced topics such as branching and merging, resolving conflicts, and using Git hooks.
2. [**Git Immersion**](https://gitimmersion.com/): This interactive tutorial provides a step-by-step guide to learning Git, including creating repositories, making changes, and working with remote repositories. It also includes exercises and quizzes to help you practice Git commands and concepts.
3. [**GitLab Git Handbook**](https://about.gitlab.com/handbook/): This comprehensive guide provides an in-depth overview of Git, including best practices and tips for using Git effectively. It covers topics such as Git workflows, branching strategies, and using Git with CI/CD pipelines.
4. [**Pro Git book**](https://git-scm.com/book/en/v2): This free online book covers Git in depth, including advanced topics such as rebasing, tagging, and using Git with submodules. It also includes examples and case studies that illustrate how Git can be used in real-world software development projects.
5. [Git, GitHub, & GitHub Desktop for beginners](https://youtu.be/8Dd7KRpKeaE)
6. [Git Explained in 100 Seconds](https://youtu.be/hwP7WQkmECE)
7. [Git It? How to use Git and Github](https://youtu.be/HkdAHXoRtos)
8. [13 Advanced (but useful) Git Techniques and Shortcuts](https://youtu.be/ecK3EnyGD8o)
| [git log --graph --oneline](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History) | This shows a summarized view of the commit history for a repo. |
