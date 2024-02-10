from ast import main
from github import Github
import csv

token = "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" #paste your token here

g = Github(token)

def repo_search(keyword):

    query = " ".join(keyword) + " in:description in:readme "
    result = g.search_repositories(query, "stars","desc") # q, sort, order 

    file = open("github_Repo_Output.csv", "w", newline = '', encoding='utf-8')
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Full Name', 'HTML URL','Description'])
    # print(f'Full Name HTML URL Description')

    print(f"Found {result.totalCount} repo(s)")
    print("outputting into a csv file...")
    for repo in result:
        writer.writerow([repo.full_name, repo.html_url, repo.description])
        # print(f'{repo.full_name}    {repo.description}    {repo.html_url}')
        # print(repo.description)
        # print(repo.html_url)
        # print()
    
    print("result output complete")

def main():

    keywords = input("Enter keyword(s): ")
    #splitting the keywords, stripping the whitespace and put it in a list 4 lines into 1 (list comprehension)
    keywords = [keyword.strip() for keyword in keywords.split(',')] 

    print("searching repo...")
    repo_search(keywords)
    print("program executed")


if __name__ == '__main__':
    main()
# print(g.get_user().get_repos())