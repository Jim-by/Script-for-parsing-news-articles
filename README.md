# News Articles Parser

This script is designed to scrape news articles from the [People Onliner](https://people.onliner.by/) website and save the extracted data into a CSV file.

## Requirements

To run this script, you need to have the following Python packages installed:

- `requests`
- `lxml`

You can install these packages using `pip`:

```bash
pip install -r requirements.txt
```

# Usage
1. Clone the repository:

git clone https://github.com/YOUR_USERNAME/data_science_project.git

2. Navigate to the project directory:

cd data_science_project

3. Install the required dependencies:

pip install -r requirements.txt

4. Run the script:

python parser_script.py

The script will fetch the news articles from the website, extract the titles and links, and save them into a articles.csv file in the same directory as the script.

# Output

The output file articles.csv will contain the following columns:

Title: The title of the news article.
Link: The URL of the news article.

# Error Handling
The script includes error handling for the following scenarios:

* Network errors during the request.
* Data extraction errors if the website structure has changed.
* General exceptions.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or issues, please contact vlma@tut.by.