import os, requests
HEADERS = {'authorization': 'token ' + os.environ['ACCESS_TOKEN']}
query = """
query($login: String!, $author_id: ID!) {
    user(login: $login) {
        repository(name: "yoezequiel") {
            defaultBranchRef {
                target {
                    ... on Commit {
                        history(author: {id: $author_id}) {
                            totalCount
                        }
                    }
                }
            }
        }
    }
}
"""
req = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': {'login': 'yoezequiel', 'author_id': 'MDQ6VXNlcjY1NjI2MTE3'}}, headers=HEADERS) # wait, I don't know the exact ID, let me just fetch it first.
print(req.json())
