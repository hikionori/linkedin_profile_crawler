# LinkedIn Profile Crawler

This is a simple LinkedIn profile crawler that uses the LinkedIn API to get the profile information of a user. The crawler is written in Python and uses the requests library to make HTTP requests to the LinkedIn API.

## Requirements
- Python 3.6 or higher

## Usage
For using this crawler, you need to have a LinkedIn account. After that you can use the crawler to get the profile information of a user by providing the user's LinkedIn public id.

### Installation
To install the required libraries, run the following command:
```bash
pip install -r requirements.txt
```

### Running the Crawler
You have 3 options to run the crawler:
1. Run the `main.py` file and provide all data as arguments:
```bash
python main.py --email <your_email> --password <your_password> --profile_id <user_id>
```
2. Predefine data as environment variables and run the `main.py` file:
```bash
export LINKEDIN_EMAIL=<your_email>
export LINKEDIN_PASSWORD=<your_password>
export LINKEDIN_PROFILE_ID=<user_id>
python main.py
```
3. Partially predefine data as environment variables and run the `main.py` file:
```bash
export LINKEDIN_EMAIL=<your_email>
python main.py --password <your_password> --profile_id <user_id>
```