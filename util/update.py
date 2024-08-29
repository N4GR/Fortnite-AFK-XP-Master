from imports import *
log = SetupLogging("UPDATE ")

# Third-party libraries.
import requests

class Update:
    def __init__(self) -> None:
        log.debug("Checking for updates...")

        self.latest = self.GetGitHubTag()
    
    def GetGitHubTag(self):
        # GitHub API URL to get the tags
        url = f"https://api.github.com/repos/N4GR/Fortnite-AFK-Master/releases/latest"
        
        # Make a GET request to the API
        try:
            log.info("Getting latest version tag.")
            response = requests.get(url)

        except Exception as error:
            log.error(error)
            log.error("Couldn't get URL.")
            return
        
        # Check if the request was successful
        if response.status_code == 200:
            release_info = response.json()

            # Get the tag name from the release information
            latest_tag = release_info.get('tag_name', 'No tag found.')

            return latest_tag
        
        elif response.status_code == 404:
            log.error("Repository not found.")

        elif response.status_code == 403:
            log.error("Forbidden.")

        return response.status_code