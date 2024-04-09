#!/usr/bin/python3
"""
Queries the Reddit API recursively, parses the titles of all hot articles,
and prints a sorted count of given keywords.
"""

import requests
import sys

def count_words(subreddit, word_list, after=None, word_count={}):
    """Prints a sorted count of given keywords in hot articles for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Custom User Agent"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title.split():
                        if word.lower() in word_count:
                            word_count[word.lower()] += 1
                        else:
                            word_count[word.lower()] = 1
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            return
    else:
        return

if __name__ == "__main__":
    subreddit = sys.argv[1] if len(sys.argv) > 1 else None
    word_list = sys.argv[2:] if len(sys.argv) > 2 else []
    if subreddit and word_list:
        count_words(subreddit, word_list)
    else:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
