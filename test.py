from requests import get, post

# print(get(f"http://127.0.0.1:5050/api/jobs").json())
# print(get(f"http://127.0.0.1:5050/api/jobs/1").json())
# print(get(f"http://127.0.0.1:5050/api/jobs/123").json())
# print(get(f"http://127.0.0.1:5050/api/jobs/uniquniquniquniquniq").json())

print(post('http://127.0.0.1:5050/api/jobs', json={}).json())

print(post('http://localhost:5050/api/jobs',
           json={'job': 'Заголовок'}).json())

print(post('http://localhost:5050/api/jobs',
           json={'team_leader': 'Заголовок',
                 'work_size': 12,
                 'collaborators': '1, 2, 3',
                 'job': 'wash',
                 'is_finished': False}).json())