Backend Takehome Project
📌 Project Overview
This project fetches research papers from PubMed, filters them based on author affiliations, and saves the results as a CSV file.

🛠 Features
✅ Fetches research papers from PubMed API
✅ Filters non-academic authors (pharma/biotech affiliations)
✅ Saves results as a CSV file
✅ CLI command: get-papers-list (for that want to link cli cmd)
✅ Fully set up with Poetry and Test PyPI

📂 Folder Structure

backend-takehome/
│── backend_takehome/       # Main package folder
│   │── __init__.py
│   │── cli.py              # Command-line interface
│   │── papers_fetcher/
│   │   │── __init__.py
│   │   │── fetch.py        # Fetching data from PubMed API
│   │   │── filters.py      # Filtering non-academic authors
│   │   │── utils.py        # Utility functions (CSV saving, etc.)
│── pyproject.toml          # Poetry configuration
│── README.md               # Project documentation


🛠 How We Built It
1️⃣ Set Up Python Virtual Environment
We created a virtual environment to keep dependencies isolated:
python -m venv .venv
.venv\Scripts\activate


2️⃣ Installed Poetry & Dependencies
We used Poetry for package management:
pip install --target=".venv/Lib/site-packages" poetry
python -m poetry init
Then, we installed the required packages:
python -m poetry add requests pandas lxml rich


3️⃣ Developed the Backend Logic
fetch.py → Fetches research papers using PubMed API
filters.py → Identifies non-academic authors
utils.py → Saves results to a CSV file
cli.py → Handles user input from the command line


4️⃣ Packaged and Published to Test PyPI
We built and uploaded the package to Test PyPI:
python -m poetry build
python -m poetry publish -r testpypi


5️⃣ Installed the Package in a Test Environment
We tested the package in a new environment using:
pip install --target=".venv/Lib/site-packages" --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ backend-takehome --no-cache-dir --force-reinstall


6️⃣ Manually Linked the CLI Command
Since --target does not link CLI scripts, we manually created one:
Set-Content -Path ".venv/Scripts/get-papers-list.bat" -Value '@python "%~dp0..\Lib\site-packages\backend_takehome\cli.py" %*'


🚀 How to Use the Project
1️⃣ Clone the Repository
If you're a third-party user, first clone the project:
git clone https://github.com/Mukeshkummuru/backend-takehome.git
cd backend-takehome


2️⃣ Set Up Virtual Environment
python -m venv .venv
.venv\Scripts\activate


3️⃣ Install the Package
pip install --target=".venv/Lib/site-packages" --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ backend-takehome --no-cache-dir --force-reinstall


4️⃣ Link the CLI Command
Set-Content -Path ".venv/Scripts/get-papers-list.bat" -Value '@python "%~dp0..\Lib\site-packages\backend_takehome\cli.py" %*'


5️⃣ Run the CLI Command
get-papers-list "cancer research" -f output.csv
This will fetch papers related to "cancer research" and save the results in output.csv.

📄 Example Output (CSV Format)
PubmedID,Title,Publication Date,Non-academic Author(s),Company Affiliation(s)
12345678,"Study on Cancer Treatment",2025-03-10,"John Doe","Pfizer"
23456789,"New Drug Development",2025-03-05,"Jane Smith","Moderna"
🎯 Final Thoughts
This project successfully fetches and filters research papers based on author affiliation. The command-line interface (get-papers-list) makes it easy to search for research papers and save results in a structured format.

🔗 Useful Links
🔹 Test PyPI Package:[ Test PyPI](https://test.pypi.org/project/backend-takehome/)
🔹 GitHub Repository: [GitHub](https://github.com/Mukeshkummuru)

 