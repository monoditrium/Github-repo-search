# Github-repo-search
This is a python script using Github REST API to accept keywords and use it to search public repositories on Github

Requirements:  Python version 3.11.8 and PyGitHub

This script uses PyGitHub, a python library for Github REST API.

To install PyGitHub, open the command prompt in windows

type 'pip install PyGithub'

the installation should begin and wait until it's complete

# To run the program:

## Generating Tokens:

**you need to have a github account to do this.**

login to GitHub and generate a GitHub token here: https://github.com/settings/tokens
  
generate the token and make sure to enable access to public repositories

This is a token github uses to authenticate requests for the github REST API.

Edit the program by pasting your token there.


Open the program in command prompt

use the cd command to change the command prompt directory to where the program is

type `python githubRepo.py` to run the program

type the keyword with spaces in between e.g `python mongodb`

the program will output into a csv file in the same directory

the output file is called github_Repo_Output.csv

# Notes
The code runs pretty slowly

If the code shows `Request GET /search/repositories?sort=stars&order=desc&q=python+mongodb+in%3Adescription+in%3Areadme+&page=30 failed with 403: Forbidden
Setting next backoff to 25.77553s` it is running properly, I think this shows up because of the rate limit from the github REST API.

The program should print `program executed` as the last line.



