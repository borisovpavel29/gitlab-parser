import requests
import argparse

def get_gitlab_projects(gitlab_url, private_token):
    headers = {"PRIVATE-TOKEN": private_token}
    projects = []
    page = 1

    while True:
        response = requests.get(f"{gitlab_url}/api/v4/projects", headers=headers, params={"per_page": 100, "page": page})
        
        if response.status_code != 200:
            print(f"Ошибка: {response.status_code} {response.text}")
            return []
        
        data = response.json()
        if not data:
            break
        
        projects.extend(data)
        page += 1
    
    return projects

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Получить список проектов из GitLab")
    parser.add_argument("gitlab_url", help="URL GitLab")
    parser.add_argument("private_token", help="Приватный токен доступа")
    args = parser.parse_args()
    
    projects = get_gitlab_projects(args.gitlab_url, args.private_token)
    for project in projects:
        print(project["path_with_namespace"])
