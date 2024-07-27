# 🗓️ MediMonitor 💊 

A Python-based pharmacy inventory management tool designed to track medication expirations, manage sales, and maintain records of expired products.

## Features
- **Add Medication:** Add both OTC and Prescription medications to the inventory.
- **Delete Medication:** Remove medications from the inventory.
- **Check Expirations:** Get automatic email notifications for medications expiring in 30, 60, or 90 days using Gmail API.
- **Manage Expired Medications:** View and manage expired medications.
- **Manage OTC Sales:** Move expiring OTC products to the sales bin for discounts.
- **View Inventory:** Display all OTC and Prescription medications.
- **Import Medications:** from CSV: Bulk import medications into the inventory from a CSV file.

## Importing Medications from a CSV File
- Prepare a CSV file with the following columns: name, ndc, med_type, expiry_date.
- Select the option to import medications from CSV in the application.
- Provide the path to your CSV file when prompted.

## Monthly Task Scheduling
- Automatic Checks: The program can be configured to run on a regular basis (e.g., once a month) to check for expiring medications. You can set this up using a task scheduler like cron (Linux) or Task Scheduler (Windows) to run the check_expirations() function at your desired interval.

    # Cron Set Up
    1. To set this up using cron, open your terminal and type the following command to edit the crontab file:
    ```
    crontab -e
    ```
    2.  Add a new line to the crontab file to schedule your Python script. For example, to run the script on the 1st day of every month at midnight, you would add:
    ```
    0 0 1 * * /usr/bin/python3 /path/to/your/main.py
    ```
    3. Save and exit.
    # Explanation:
    - 0 0 1 * * specifies the schedule (midnight on the 1st of every month).
    - /usr/bin/python3 is the path to the Python 3 interpreter (adjust if necessary).
    - /path/to/your/main.py is the full path to your Python script.


## Gmail API Integration
- Email Notifications: The program uses the Gmail API to send email notifications about medications nearing their expiration dates. The email includes:
    - Products expiring within 30, 60, and 90 days.
    - Notifications for OTC products marked for discounts.
    - Instructions for handling expired and sale items.

    # Email Details: 
    - Subject: MediMonitor Expiration Notifications
    - Body: 
        - Prescription Products: Medications expiring within 30 days are moved to the expiry bin. Follow the pharmacy’s protocol for returning or disposing of expired medications.
        - Sales Products: OTC products expiring within 90 days are moved to the sales bin. Mark these products as discounted.

## Setup Instructions
- Install Dependencies: Ensure you have all required packages installed. 
'''
pip install sqlite3 csv google-api-python-client google-auth-httplib2 google-auth-oauthlib
'''
- Gmail API Setup:
    - Create a Project: Go to the Google Cloud Console, create a new project, and enable the Gmail API.
    - Create Credentials: Download the client_secret.json file from the Google Cloud Console and place it in your project directory.
    - Authentication: Follow Google's quickstart guide to authorize and set up your Gmail API credentials.
- Running the Application:
    - Execute the main script to start the application.
    ```
    python main.py
    ```
- Task Scheduling: Configure a scheduler (like cron for Linux or Task Scheduler for Windows) to run the script at desired intervals.