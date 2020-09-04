to run the notebook, in venv mode go `jupyter notebook`
you need a spotify app to get the client_id and client_credentials
e.g. https://developer.spotify.com/dashboard/applications/dbbe41f4185d426d84a51455f3eedaa7

to convert notebooks into python file we use nbconvert: `jupyter nbconvert --to python <path/filename>`:`jupyter nbconvert --to python notebooks/spotify_client.ipynb`
to convert all notebooks: `jupyter nbconvert --to python *.ipynd`

or simply run the `convert.sh` directly