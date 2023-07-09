# DATA-EXTRACTION-FROM-HTML
This project aims to bridge the gap between non-technical users and their ability to extract data from websites. The project proposes a user-friendly web application that allows non-technical users to easily extract data using keywords.
# DESCRIPTION
* The "DATA-EXTRACTION-FROM-HTML" is a user-friendly web application designed to empower non-technical users to easily extract data from websites. The project aims to bridge the gap between individuals without programming knowledge and the ability to gather specific data from websites.
* Using the web application, users can input the URL of a target website and specify relevant keywords related to the data they want to extract. For example, they can extract headings, links, tables, paragraphs, or meta data by providing the corresponding keywords. The tool leverages Python and the BeautifulSoup library for web scraping functionalities.
* The application provides a simple and intuitive interface that eliminates the need for technical expertise or understanding of web technologies. It offers a form where users can enter the URL and keywords, and upon submitting the request, the tool retrieves the desired data from the website. The extracted data is then displayed to the user in a structured and easily readable format.

# INSTALLATION
### Prerequisites: Ensure you have the following software installed on your machine:
* Python (version 3.7 or higher)
* pip (package installer for Python)
  
1. Clone this project repository: https://github.com/rajput-code/DATA-EXTRACTION-FROM-HTML
2. Install the requirements.txt: *** 'pip install -r requirements.txt' ***

# USAGE
1. Run the web application by executing the 'app.py' file.
2. Access the application through your web browser using the provided URL (e.g., http://localhost:5000).
3. Enter the URL of the website you want to scrape and specify the relevant keywords for data extraction.
4. Click the "Extract Data" button to retrieve and display the desired data

Example: Let the URL be " https://www.reddit.com/ " and the keyword as headings and then clcik on the Extract data button . The following results shows up:
* Page Description: Reddit is a network of communities where people can dive into their interests, hobbies and passions. There's a community for whatever you're interested in on Reddit.
* Occurrences of 'headings': 0
* Headings:
* Overspeeding "CRETA" accident on Ludiana-Ferozpur road. Must be dumb to overspeed in rainy season.
* Man runs away with ballot box in Bengal’s Cooch Behar.What kind of democracy is this, democracy has failed in front of TMC goons in Bengal.
* TMC goons brazenly show guns and threaten an independent candidate in Barrackpore, North 24 Parganas
* Ghaziabad Station, Delhi-Meerut RapidX
* Is Delhi really "scary af" or you just wanted reddit Karma ?
* Stealth level 1000
* Movie dialogues you use in daily life

