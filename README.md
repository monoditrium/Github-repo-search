# Github-repo-search
This is a python script using Github REST API to accept keywords and use it to search public repositories on Github

Requirements:
Python version 3.11.8
PyGitHub

This script uses PyGitHub, a python library for Github REST API.
To install PyGitHub, open the command prompt in windows
type pip install PyGithub
the installation should begin and wait until it's complete

# To run the program:

Open the program in command prompt\n
use the cd command to change the command prompt directory to where the program is\n
type python githubRepo.py to run the program\n
the program will output into a csv file in the same directory\n
the output file is called github_Repo_Output.csv\n


Generating Tokens:
generate a GitHub token here: https://github.com/settings/tokens
generate the token and make sure to enable access to public repositories

This is a token github uses to authenticate requests for the github REST API
you need to have a github account to do this
only do this if the token in the code has expired
Edit the program by pasting your token there.

