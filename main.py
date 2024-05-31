# from itertools import islice
# from youtube_comment_downloader import *
# downloader = YoutubeCommentDownloader()
# comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=YxWlaYCA8MU', sort_by=SORT_BY_POPULAR)
# for comment in islice(comments, 10):
#     print(comment)

import json
from itertools import islice
from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR

# Initialize the downloader
downloader = YoutubeCommentDownloader()

# Get comments from the YouTube video
comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=kffacxfA7G4', sort_by=SORT_BY_POPULAR)

# Collect the first 10 comments
comments_list = []
for comment in islice(comments, 40000):
    comments_list.append(comment)

# Save the comments to a JSON file
with open('comments.json', 'w') as json_file:
    json.dump(comments_list, json_file, indent=4)

print("Comments have been saved to comments.json")
