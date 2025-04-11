# Fastq Search Application

## Overview
The Fastq Search application is a desktop application built using PyQt5 for the graphical user interface (GUI) and Flask for the backend server. It is designed to facilitate the search and management of FASTQ files, which are commonly used in bioinformatics for storing nucleotide sequences.

## Project Structure
```
fastq_search
├── backend
│   ├── app.py                # Main application logic for PyQt5 and Flask
│   ├── copy_fastq.py         # Logic for handling FASTQ file operations
│   ├── requirements.txt       # Python dependencies for the backend
│   └── __init__.py           # Marks the backend directory as a package
├── frontend
│   ├── static                # Directory for static files (CSS/JS)
│   ├── templates             # Directory for HTML templates
│   └── __init__.py           # Marks the frontend directory as a package
├── .gitignore                # Files and directories to be ignored by Git
├── README.md                 # Documentation for the project
└── LICENSE                   # Licensing information for the project
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastq_search.git
   cd fastq_search
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r backend/requirements.txt
   ```

## Usage
1. Start the Flask server:
   ```
   python3 backend/copy_fastq.py
   ```

2. Launch the PyQt5 application:
   ```
   python3 backend/app.py
   ```

3. The application will open a window where you can interact with the FASTQ file management features.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.