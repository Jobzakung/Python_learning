import requests

url = 'https://iqiyi.playbux.co/api/v2/watch-to-earn/contents?modeKey=th&random=true&limit=500&page=1&recs=6481abd4f3762b86f6f9128b'
headers = {
    'cookie': '__Host-next-auth.csrf-token=87c85072f6f0d368404d3cf476c94447aa487e45a40b9ae136871a4f2e95c815%7C403a29dc7399976fe4506c3a71db66ddbd0d838aa0aa2f3711ebe355f175b3c8; AMP_MKTG_468b9b7a89=JTdCJTdE; __Secure-next-auth.callback-url=https%3A%2F%2Fiqiyi.playbux.co%2F%2Fgame%3Fscene%3DGameCenter; AMP_468b9b7a89=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIzZTc4ODgzMS00N2ZjLTRhZDAtOGI3NC1hYmNiZTkxODAxOGIlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjI2NDcwM2RlNjczYjJhZjRiNGNlMzE0Y2QlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNjg2NzM2NDk1NzUzJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTY4NjczNjQ5NjAxNSU3RA==; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..h5yWoDXKPZZAzbW3.WDkYgYIK988fpS6D32cLnTnbXvzGz49yHE5MdXSSMzpgKguqwVKoDcBqo19zTh6Q00QyRoGbVbBgC-814Qb2usiex7NPH8a635wPeZQjJqiteT2CWHdW2KKcT4YgZhNirfZuD9qkH-DdsQ-JtEHN4P8e5Csyk1lioTts-fmxFj6Adg68y2VhfotD9KF2Mu7d4aVfuaBjxoXUaQnIwUsXFSPW.agsEV0wt0Q30L-MXIe6GUg'
    # Include your headers here
}

response = requests.get(url, headers=headers)

try:
    response.raise_for_status()  # Check if the request was successful
    data = response.json()

    # Extract the score and name for each item
    items = data.get('data', [])  # Get the list of items, defaulting to an empty list if 'data' is not found
    for item in items:
        score = item.get('score')
        name = item.get('name')
        print("Name:", name)
        print("Score:", score)
        print()

except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.RequestException as err:
    print("Error:", err)
