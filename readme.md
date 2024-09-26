# YouTube Video Upload Script

This project allows you to upload videos to YouTube using Python. It utilizes the YouTube Data API and requires authentication through the Google Developer Console.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Google Developer Console](#setup-google-developer-console)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Prerequisites

- Python 3.x installed on your machine.
- Basic knowledge of Python and command-line interface.

## Setup Google Developer Console

1. **Create a Google Account**: If you don't have one, create a [Google Account](https://accounts.google.com/signup).

2. **Access Google Developer Console**:
   - Go to the [Google Developer Console](https://console.developers.google.com/).
   - Click on `Select a project` and then `New Project`.
   - Give your project a name and click `Create`.

3. **Enable YouTube Data API v3**:
   - In the dashboard of your project, click on `Library` in the left sidebar.
   - Search for `YouTube Data API v3` and click on it.
   - Click `Enable` to enable the API for your project.

4. **Create Credentials**:
   - In the left sidebar, click on `Credentials`.
   - Click `Create credentials` and select `OAuth client ID`.
   - If prompted to configure the consent screen, do so:
     - Fill in the required fields and save.
   - For application type, select `Desktop app`.
   - Click `Create`.
   - Click `OK` and then download the `client_secrets.json` file. Save it in the same directory as your script.

## Installation

1. Clone this repository or download the script file.

2. Install the required packages:
    ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open the script file (youtube.py) and modify the following variables in the main() function:
    - file_path: Path to your video file (e.g., video.mp4).
    - title: Title of your video.
    - description: Description for your video.
    - category: YouTube category ID (e.g., 22 for People & Blogs).
    - keywords: List of keywords related to your video.

2. Run the script:
    ```bash
    python youtube.py
    ```

3. A browser window will open for authentication. Log in with your Google account and allow access.

4. If successful, the script will upload your video and display the Video ID.

## License

This project is licensed under the MIT License.

Feel free to adjust any sections to better fit your project or personal preferences!