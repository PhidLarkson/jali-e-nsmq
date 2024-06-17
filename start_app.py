import subprocess
# import os

# Run the Streamlit program
subprocess.Popen(["streamlit", "run", "main.py"])

# Open a new terminal instance and change directory
subprocess.Popen(["gnome-terminal", "--", "bash", "-c", "cd /home/pnlarbi/Music/AFRICAIED\ HACKATHON/social-platform/wikilan; python manage.py runserver"])

print("All processes have been started successfully!")
