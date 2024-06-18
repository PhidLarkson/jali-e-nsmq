# PROJECT JALI -EXTENDED [AFRICAIED HACKATHON BUILD]
## The goal is to build an open-source, AI powered tool to help students prepare for the Ghana National Maths and Science Quiz competition - This tool is meant to address the equity problem in NSMQ training. Some schools lack more resources, facilities and platforms for studies.

---

### This project is built in python.

To get started with the project, follow these steps:

1. Create a virtual environment by running the following command:
    ```
    python -m venv myenv
    ```

2. Activate the virtual environment:
    - On Windows:
      ```
      myenv\Scripts\activate
      ```
    - On macOS and Linux:
      ```
      source myenv/bin/activate
      ```

3. Install the required dependencies by running:
    ```
    pip install -r requirements.txt
    ```

4. Once the dependencies are installed, you can start the application by running:
    ```
    python startapp.py


## THE SOCIAL PLATFORM

### Downloading a Folder from Google Drive with Commands

This README explains how to download a folder directly from your Google Drive to a specific directory on your computer using two popular methods:

**Method 1: Using gdown (Python package)**

**Requirements:**

* Python 3 installed on your system
* `gdown` package installed

**Steps:**

 **Install `gdown`:**

   ```bash
   pip install gdown
   ```

 **Download the folder:**

   ```bash
   gdown --folder --id 1CzjJirt9OPBHD8ngPVHFT2LJ5BVIda2m
   ```

   * This command will download the entire folder and its contents to your current directory.

**Method 2: Using curl (command-line tool)**

**Requirements:**

* `curl` command-line tool installed on your system

**Steps:**

1. **Get the folder ID (same as Method 1):**

   * Follow steps 1 and 2 from Method 1 to obtain the folder ID.

2. **Download the folder:**

   * Open a terminal or command prompt.
   * Navigate to the main directory.

   ```bash
   curl -L "https://drive.google.com/drive/folders/1CzjJirt9OPBHD8ngPVHFT2LJ5BVIda2m?usp=sharing" >  africaied-jali.zip
   ```

   * This command will download the folder as a compressed ZIP archive named "folder.zip". You can rename the file after download.

**Extracting the ZIP Archive (Method 2):**

* Once the download is complete (Method 2), you'll need to extract the contents of the ZIP archive:

```bash
unzip africaied-jali.zip
```

This will create a new directory named "folder" containing the downloaded files.

Copy and paste the all the contents of the zip into the social-platform folder
