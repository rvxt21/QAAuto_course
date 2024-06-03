import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get('https://api.github.com/search/repositories',
                         params={"q": name})
        body = r.json()

        return body

    def search_emoji(self):
        r = requests.get('https://api.github.com/emojis')

        return r

    def search_list_of_commits(self, owner: str, repo: str):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')

        return r