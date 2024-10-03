# Daily Architecture Wallpaper Updater

Automatically download a new architecture photo from Unsplash every day and set it as your Windows desktop wallpaper.

![Sample Wallpaper](https://source.unsplash.com/random/800x200/?architecture)

## Table of Contents

- [Features](#features)
- [Disclaimer](#disclaimer)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Obtaining an Unsplash Access Key](#obtaining-an-unsplash-access-key)
- [Usage](#usage)
- [Automate with Windows Task Scheduler](#automate-with-windows-task-scheduler)
- [Notes](#notes)
- [License](#license)

## Features

- Downloads a high-resolution architecture image from Unsplash.
- Sets the downloaded image as your desktop wallpaper.
- Cleans up old images to save disk space.
- Configurable to use different search queries.

## Disclaimer

- **Personal Use Only**: This script is intended for personal use. Please respect Unsplash's [API Guidelines](https://unsplash.com/documentation#guidelines--crediting) and [License](https://unsplash.com/license).
- **No Redistribution**: Do not redistribute downloaded images or use them for commercial purposes.

## Requirements

- Windows 10 or later
- Python 3.x installed on your system
- Python packages:
  - `requests`

## Installation

1. **Clone or Download the Repository**

   ```bash
   git clone https://github.com/yourusername/daily-architecture-wallpaper.git
   ```

2. **Install Required Python Packages**

   Open Command Prompt and run:

   ```bash
   pip install requests
   ```

## Configuration

Before running the script, you need to configure it with your own Unsplash Access Key and adjust settings as needed.

### 1. Set Up Environment Variables

- **Unsplash Access Key**: Set an environment variable `UNSPLASH_ACCESS_KEY` with your Unsplash Access Key.
- **Optional**: If you prefer, you can modify the script to include your access key directly (not recommended), or read from a configuration file.

### 2. Edit Script Variables (Optional)

Open `download_wallpaper.py` in a text editor and adjust the following variables if needed:

- **DOWNLOAD_FOLDER**: The folder where images will be saved.
  ```python
  DOWNLOAD_FOLDER = r'C:\Users\YourUsername\Pictures\ArchitectureWallpapers'
  ```
- **QUERY**: The search term for the type of images you want.
  ```python
  QUERY = 'architecture'
  ```
- **KEEP_LATEST**: The number of recent images to keep.
  ```python
  KEEP_LATEST = 5
  ```

## Obtaining an Unsplash Access Key

1. **Sign Up for an Unsplash Account**

   - Visit the [Unsplash website](https://unsplash.com/join) and create a free account.

2. **Apply for API Access**

   - Go to the [Unsplash Developers](https://unsplash.com/developers) page.
   - Click on **"Your Apps"** and then **"New Application"**.
   - Fill out the application details:
     - **Name**: e.g., "Personal Wallpaper Updater"
     - **Description**: e.g., "A script to update my desktop wallpaper daily"
     - **API Usage**: Describe your intended use.
     - **Platform**: Select **"Other"**.
   - Agree to the terms and submit the application.

3. **Retrieve Your Access Key**

   - After approval, you'll receive an **Access Key**.
   - **Keep this key secure** and do not share it publicly.

## Usage

### Running the Script Manually

1. **Open Command Prompt**

2. **Navigate to the Script Directory**

   ```bash
   cd path\to\daily-architecture-wallpaper
   ```

3. **Run the Script**

   ```bash
   python download_wallpaper.py
   ```

   - The script will download a new image and set it as your wallpaper.

## Automate with Windows Task Scheduler

To have the script run automatically every day, set up a scheduled task.

### Steps:

1. **Open Task Scheduler**

   - Press `Win + R`, type `taskschd.msc`, and press Enter.

2. **Create a New Basic Task**

   - Click on **"Create Task..."** in the **Actions** pane.

3. **General Tab**

   - **Name**: `Daily Architecture Wallpaper`
   - **Description**: Updates wallpaper daily with a new image from Unsplash.
   - **Security Options**:
     - Check **"Run only when user is logged on"**.
     - **Uncheck** "Run with highest privileges".

4. **Triggers Tab**

   - Click **"New..."**.
   - **Begin the task**: On a schedule.
   - **Settings**:
     - **Daily**.
     - **Start**: Choose the time you want the script to run (e.g., 9:00 AM).
   - Click **"OK"**.

5. **Actions Tab**

   - Click **"New..."**.
   - **Action**: Start a program.
   - **Program/script**: Full path to your Python executable.
     - Example: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python39\python.exe`
   - **Add arguments**:
     ```plaintext
     "C:\path\to\download_wallpaper.py"
     ```
   - Click **"OK"**.

6. **Conditions and Settings Tabs**

   - Adjust settings as needed (e.g., ensure the task runs even if on battery power).

7. **Save the Task**

   - Click **"OK"** to save the task.

### Testing the Task

- **Run Manually**: In Task Scheduler, right-click the task and select **"Run"**.
- **Verify**: Check if your wallpaper updates after a few moments.

## Notes

- **API Rate Limits**: Ensure you stay within Unsplash's API rate limits (50 requests per hour for personal use).
- **Attribution**: This script is for personal use. If you display images publicly, you must follow Unsplash's [attribution guidelines](https://unsplash.com/documentation#guidelines--crediting).
- **Privacy**: Do not share your Unsplash Access Key. If sharing this script, ensure your key is excluded.
- **Environment Variables**: Setting up environment variables ensures your access key isn't hard-coded in the script.

## License

This project is licensed under the [MIT License](LICENSE).

---

**Acknowledgments**

- This script uses the [Unsplash API](https://unsplash.com/documentation).
- All images are provided by [Unsplash](https://unsplash.com) and are subject to the [Unsplash License](https://unsplash.com/license).

---

**Enjoy your new daily dose of architectural inspiration!**
