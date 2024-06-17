import requests

def check_internet():
    try:
        response = requests.get("https://www.google.com")
        return True
    except:
        return False
    
# if check_internet():
#     print("Internet is connected")

# else:
#     print("Not connected")