import requests

api_key = "c0caf24fb979ec3d9cdb917c810f18f6"

api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjMGNhZjI0ZmI5NzllYzNkOWNkYjkxN2M4MTBmMThmNiIsInN1YiI6IjVmNDE2NjIxMGJiMDc2MDAzM2QyZTRiNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.sQOmrHe2N3wabdwryAdbISoMNvfhNT2SnX_jEnGpyCo"


#  end point:
"""
GET
/movie/{movie_id}
https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
"""
api_version = 3
movie_id = 500
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"

r = requests.get(endpoint)

print(endpoint)

print(r.status_code)
print(r.text)
