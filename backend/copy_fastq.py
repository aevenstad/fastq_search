import os
import subprocess
import shutil
from flask import Flask, request, jsonify, send_from_directory
import humanize

app = Flask(__name__)

# Serve the HTML page
@app.route('/')
def index():
    public_folder = os.path.join(os.path.dirname(__file__), "../frontend/templates")
    return send_from_directory(public_folder, 'index.html')

def locate_files(search_string, suffix=None):
    print(f"Locating files for: {search_string}")

    # Use locate command to find files, optionally filter by suffix
    result = subprocess.run(['locate', search_string], stdout=subprocess.PIPE, text=True)
    files = result.stdout.splitlines()
    
    if suffix:
        # Filter files by the selected suffix
        files = [file for file in files if file.endswith(suffix)]


    # Debug the output of locate command
    print(f"Files found by locate: {files}")  # Debugging line



    # Get the size of each file in a human-readable format
    files_with_size = []
    for file in files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            human_readable_size = humanize.naturalsize(size)
            files_with_size.append({"file": file, "size": human_readable_size})
        else:
            print(f"File does not exist: {file}")  # Debugging line
    
    return files_with_size

@app.route('/locate_files', methods=['GET'])
def locate_files_endpoint():
    try:
        list_dir = request.args.get('list_dir', os.getcwd())
        suffix = request.args.get('suffix', None)  # Get suffix from request
        list_file_path = os.path.join(list_dir, 'list')

        with open(list_file_path, 'r') as file:
            search_strings = file.readlines()

        all_files = []
        for search_string in search_strings:
            search_string = search_string.strip()  # Remove extra whitespace or newlines
            print(f"Searching for: {search_string}")  # Debugging line
            files = locate_files(search_string, suffix)  # Filter by suffix if specified
            all_files.extend(files)  # Collect all files in one flat list

        return jsonify(all_files)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/copy_files', methods=['POST'])
def copy_files():
    data = request.get_json()
    files_to_copy = data.get('files', [])
    list_dir = data.get('list_dir', os.getcwd())

    for file_path in files_to_copy:
        try:
            if os.path.exists(file_path):
                shutil.copy(file_path, list_dir)  # Copy to the directory containing 'list'
            else:
                return jsonify({"error": f"File {file_path} does not exist."}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Files copied successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

