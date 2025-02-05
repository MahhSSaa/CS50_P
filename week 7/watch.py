import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Define a regular expression pattern to match YouTube embed URLs in iframe src attributes
    pattern = re.compile(r'<iframe[^>]+src="(https?://(?:www\.)?youtube\.com/embed/[^"]+)"')

    # Search for the pattern in the input string
    match = pattern.search(s)
    if match:
        # Extract the URL from the match
        embed_url = match.group(1)
        # Convert the embed URL to a shareable youtu.be URL
        video_id = embed_url.split('/')[-1]
        shareable_url = f"https://youtu.be/{video_id}"
        return shareable_url
    return None

if __name__ == "__main__":
    main()
