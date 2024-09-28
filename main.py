import os
from instagrapi import Client

def load_credentials(file_path):
    """
    Load the user names and passwords for the automated accoutns we want
    :param file_path:
    :return:
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        username = lines[0].strip()
        password = lines[1].strip()
    return username, password

# Post media (either to the feed or as a story)
def post_content(client, content_path, is_story=False):
    if is_story:
        # Handle image and video uploads for stories
        if content_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            client.photo_upload_to_story(content_path)
            print(f"Uploaded photo to story: {content_path}")
        elif content_path.lower().endswith('.mp4'):
            client.video_upload_to_story(content_path)
            print(f"Uploaded video to story: {content_path}")
    else:
        # Upload to feed
        client.photo_upload(content_path, "Posted via bot")
        print(f"Posted to feed: {content_path}")

# Main function
def main():
    # Load credentials
    # username, password = load_credentials('credentials.txt')

    # username, password = 'nimbuschoen', 'mrnimbuS057!'
    username = input("Enter your insta user name: ")
    password = input("Enter your insta password: ")

    # Initialize and login to Instagram account
    client = Client()
    client.login(username, password)

    # Define your local directory containing the media
    content_directory = "./images"

    # Iterate through all files in the directory
    for filename in os.listdir(content_directory):
        content_path = os.path.join(content_directory, filename)

        # Only proceed if the file is a valid media type (e.g., jpg, mp4)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4')):
            # if "story" in filename:  # Mark files meant for stories
                post_content(client, content_path, is_story=True)
            # else:  # Otherwise post to the feed
                post_content(client, content_path)

    # Logout after the job is done
    client.logout()

if __name__ == "__main__":
    main()
