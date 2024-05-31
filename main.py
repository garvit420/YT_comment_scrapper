import json
from itertools import islice
from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR
import concurrent.futures

# Initialize the downloader
downloader = YoutubeCommentDownloader()

# Get comments from the YouTube video
video_url = 'https://www.youtube.com/watch?v=kffacxfA7G4'

# Define the number of comments to fetch
num_comments = 10000

# Fetch comments concurrently
def fetch_comments():
    return list(islice(downloader.get_comments_from_url(video_url, sort_by=SORT_BY_POPULAR), num_comments))

# Use ThreadPoolExecutor for concurrent processing
with concurrent.futures.ThreadPoolExecutor() as executor:
    comments_list = executor.submit(fetch_comments).result()

# Save the comments to a JSON file
with open('comments.json', 'w') as json_file:
    json.dump(comments_list, json_file, indent=4)

print("Comments have been saved to comments.json")
