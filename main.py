import logging
import os
from linkedin_api import Linkedin
import requests
import argparse


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        filename="out.log",
        filemode="w",
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.info("Logging started")


def login_to_linkedin(username, password):
    logging.info("Login to LinkedIn")
    try:
        api = Linkedin(username, password)
        return api
    except Exception as e:
        logging.error(f"Failed to login: {e}")
        raise


def get_profile(api, profile_id):
    logging.info("Get profile")
    try:
        profile = api.get_profile(profile_id)
        name = profile.get("firstName") + " " + profile.get("lastName")
        public_id = profile.get("public_id")
        logging.info(f"Fetched profile of {name}")
        return profile, public_id
    except Exception as e:
        logging.error(f"Failed to get profile: {e}")
        raise


def get_profile_picture_url(profile):
    logging.info("Get profile picture")
    try:
        display_picture_url = profile.get("displayPictureUrl") + profile.get(
            "img_800_800"
        )
        logging.info(f"Fetched profile picture URL: {display_picture_url}")
        return display_picture_url
    except Exception as e:
        logging.error(f"Failed to get profile picture URL: {e}")
        raise


def download_profile_picture(url, cookies, headers, public_id):
    logging.info("Download profile picture")
    try:
        response = requests.get(url, cookies=cookies, headers=headers)
        response.raise_for_status()
        file_path = f"display_picture_{public_id}.jpg"
        with open(file_path, "wb") as file:
            logging.info(f"Saving profile picture to {file_path}")
            file.write(response.content)
    except Exception as e:
        logging.error(f"Failed to download profile picture: {e}")
        raise


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--email", help="LinkedIn email", dest="email")
    parser.add_argument("--password", help="LinkedIn password", dest="password")
    parser.add_argument("--profile_id", help="LinkedIn profile ID", dest="profile_id")
    return parser.parse_args()


def main():
    setup_logging()
    args = parse_args()
    username = args.email or os.getenv("LINKEDIN_EMAIL")
    password = args.password or os.getenv("LINKEDIN_PASSWORD")
    profile_id = args.profile_id or os.getenv("LINKEDIN_PROFILE_ID")

    api = login_to_linkedin(username, password)
    profile, public_id = get_profile(api, profile_id)
    display_picture_url = get_profile_picture_url(profile)
    download_profile_picture(
        display_picture_url, api.client.cookies, api.client.session.headers, public_id
    )


if __name__ == "__main__":
    main()
