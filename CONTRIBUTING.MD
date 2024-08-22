# How to Contribute to a Project on GitHub

*   Fork the repository
*   Clone the repository
*   Update the main branch
*   Create a branch
*   Make changes
*   Create a Pull Request

## Fork the Repository

The first step is to "Fork" the repository.

## Clone the Repository

After having the repository in our account, select the repository address "SSH or HTTP" and clone it:

`$ git clone https://github.com/User/RepoName.git`

Inside the generated folder, check the repository URL:

`$ git remote -v`

Before making modifications, add the URL of the original project repository:

`$ git remote add upstream https://github.com/User/OriginalRepo(Forked)`

Verify

`$ git remote -v`

## Update the main Branch

Before starting to work, get the latest changes from the Original Repo:

`$ git pull -r upstream main`

## Create a Branch

To create a branch, use the "checkout" option of git:

`$ git checkout -b feature-branch-name`

## Make Changes

Make all the changes you want to the project.

Add the files and commit

After committing, push to our repository indicating the branch we created.

`$ git push origin feature-branch-name`

## Create a Pull Request

Go to your repository on GitHub and click on "Compare & Pull Request".

Describe the changes in the Pull Request.

If everything is fine, send it with the "Create Pull Request" button.

Wait for the repository owner to review, accept, and merge it into the corresponding branch.