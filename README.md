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

1.Open the program in command prompt
2.use the cd command to change the command prompt directory to where the program is\n
3.type python githubRepo.py to run the program
4.the program will output into a csv file in the same directory
5.the output file is called github_Repo_Output.csv


Generating Tokens:
generate a GitHub token here: https://github.com/settings/tokens
generate the token and make sure to enable access to public repositories
This is a token github uses to authenticate requests for the github REST API.
you need to have a github account to do this.
only do this if the token in the code has expired.
Edit the program by pasting your token there.

