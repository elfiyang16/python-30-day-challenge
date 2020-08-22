import requests
import pprint
import pandas as pd

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

# r = requests.get(endpoint)
# print(endpoint)
# print(r.status_code)
# print(r.text)


#  v4

movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}"
headers = {
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf-8'
}
# r = requests.get(endpoint, headers=headers) # json={"api_key": api_key})
# print(r.status_code)
# print(r.text)


#  search

api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
searh_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searh_query}"
# print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.json())
if r.status_code in range(200, 299):
    data = r.json()
    results = data["results"]
    # if there's results
    if len(results) > 0:
        print(results[0].keys())
        # get movie ids undeplicated
        movie_ids = set()
        for result in results:
            _id = result["id"]
            print(result["title"], _id)
            movie_ids.add(_id)
         # convert to list
        print(list(movie_ids))

output = 'movies.csv'
movie_data = []
# get the correspondant movie info from movie id
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
      #  save result to a var data
        data = r.json()
        movie_data.append(data)

# save data to a file
df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=False)
