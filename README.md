# fastq_search

## Overview
The Fastq Search application is a desktop application built using PyQt5 for the graphical user interface (GUI) and Flask for the backend server.  
  
The main function is to locate fastq files on my local machine. I often run into the issue of having to find fastq files for a set of samples where the files can be scattered in different directories.  
  
This application solves this by taking a list of sample identifiers (or any string) and printing files matching the criteria, the files can then be easily copied.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastq_search.git
   cd fastq_search
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r backend/requirements.txt
   ```

## Usage
1. Create a text file called `list` with the sample identifiers you want to copy:
   ```
   sample01
   sample02
   sample03
   ```

2. Start the Flask server:
   ```
   python3 fastq_search/backend/copy_fastq.py
   ```

3. In a web browser go to `http://127.0.0.1:5000/` and enter the full path to the directory containing `list.
   
   Chose the suffix for the file type you want to search for and click `Load files`.  

   Select the files you want to copy and click `Copy selected files`.  

   The files will be copied to the directory with `list`  
   

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
