import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# Exercise 1: Returns a vowel_count in a given string 
@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1

    return f'There are {count} vowels in "{text}"'

# Exercise2: Returns a sorted list
@app.route('/sort_names', methods=['POST'])
def sort_names():
    names = request.form['names']
    name_list = names.split(",")
    # print(name_list)
    name_list.sort()
    return ",".join(name_list)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

