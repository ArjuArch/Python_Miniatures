from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password(nr_letters, nr_symbols, nr_numbers):
    st = ""
    for _ in range(nr_letters):
        st += random.choice(letters)

    for _ in range(nr_symbols):
        st += random.choice(symbols)

    for _ in range(nr_numbers):
        st += random.choice(numbers)

    password_list = list(st)
    random.shuffle(password_list)
    return ''.join(password_list)

index_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Generator</title>
    <script>
        function generatePassword() {
            var nr_letters = document.getElementById("nr_letters").value;
            var nr_symbols = document.getElementById("nr_symbols").value;
            var nr_numbers = document.getElementById("nr_numbers").value;

            fetch("/generate", {
                method: "POST",
                body: JSON.stringify({ nr_letters: nr_letters, nr_symbols: nr_symbols, nr_numbers: nr_numbers }),
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("password_result").textContent = data.password;
            });
        }
    </script>
    <style>
    * {
            margin: 0;
            padding: 0;
            font-family: cursive;
        }
        body {
            position: relative;
            height: 100vh; 
        }h1{
        color:white;
        text-align:center;
        padding:131px 0 20px 0;
        }

        #video_container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }
    #password_result {
    color: white;
    font-size: 21px;
    padding-left: 7%;
    padding-top: 25px;
        }
        
        #dup{
        padding-top: 38px;
        color: white;
        font-size: 21px;
        padding-left: 47%;
        }

        #video_bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: -1;
        }

        #content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            z-index: 1; /* Ensure content is above the video */
            color: white; /* Set text color */
        }

        form {
        width:600px;
            margin-left: 31%;
            margin-top:5%;
            background-color: rgba(255, 255, 255, 0.5);
            padding: 20px;
            border-radius: 10px;
        }input[type="number"]{
        width: 85px;
    height: 24px;
    padding-left: 63px;
    border: none;
    border-radius: 10px;
        }#but{
        padding-left: 41%;
    padding-top: 10px;
        }#qa{
        padding-left:42px;
        padding-bottom:10px;
        }button{
        height: 33px;
    width: 155px;
    border-radius: 8px;
    border: 1px solid rgb(231, 231, 231);
        }button:hover{
        mix-blend-mode:overlay;
        cursor:pointer;
        }
    </style>
</head>
<body>
<div>
        <video id="video_bg"
          autoplay
          muted
          loop>
          <source
          src="https://tospace.in/Video/My%20Video.mp4"
          type="video/mp4">
          <source id="video_bg"
          src="https://tospace.in/Video/My%20Video.webm"
          type="video/webm">
        </video>
      </div>
      <div id="full">
    <h1>Welcome to the PyPassword Generator!</h1>
    <form>
        <div id="qa"><label for="nr_letters">How many letters would you like in your password?</label>
        <span id="one"><input type="number" id="nr_letters" name="nr_letters" min="1" required><br></span></div>

        <div id="qa"><label for="nr_symbols">How many symbols would you like?</label>
        <input style="margin-left:117px" type="number" id="nr_symbols" name="nr_symbols" min="1" required><br></div>

        <div id="qa"><label for="nr_numbers">How many numbers would you like?</label>
        <input style="margin-left:117px" type="number" id="nr_numbers" name="nr_numbers" min="1" required><br></div>

        <div id="but"><button type="button" onclick="generatePassword()">Generate Password</button></div>
    </form>
    <div id="dup"><p>Generated Password :<p> <div><div id="password_result"></div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(index_template)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    nr_letters = int(data['nr_letters'])
    nr_symbols = int(data['nr_symbols'])
    nr_numbers = int(data['nr_numbers'])
    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    return {'password': password}

if __name__ == '__main__':
    app.run(debug=True)
