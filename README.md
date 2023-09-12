# GPT-NewsLetter
*A fully automated AI generated Newsletter covering Macroeconomics and Stock Market News.*

## Introduction
The GPT NewsLetter project leverages the capabilities of AI and various APIs to create a daily newsletter that covers Macroeconomics and Stock Market-related topics. The project uses AI language generation to craft newsletter content, pulls relevant news from the New York Times "Top Stories" API, gathers stock ticker data from AlphaVantage API, and extracts insights from Langchain-connected GPT-4 model. The project also includes a daily market heatmap obtained through Google's Gmail API, extracted from stocktwits.com emails.

## Features
+ AI-Generated Content: The newsletter content is fully autonomous, generated using OPENAI's GPT-4 model, ensuring engaging and relevant updates.
+ Data Aggregation: The project aggregates macroeconomic news from the New York Times API and stock data from the AlphaVantage API.
+ In-depth Insights: Langchain framework is employed to extract deeper insights from the top stories retrieved from the New York Times API.
+ Daily Market Heatmap: The newsletter includes a daily market heatmap image obtained through the Gmail API, extracted from emails sent by stocktwits.com.
+ User Signup Webpage: A basic webpage is available for users to sign up for the newsletter, enhancing accessibility.
+ Automation: Apache Airflow is used to schedule the entire process, ensuring the newsletter is sent out at a specific time daily.

## Technologies Used
+ OPENAI GPT-4: AI language model for generating newsletter content.
+ New York Times API: Source of macroeconomic and stock-related news.
+ AlphaVantage API: Provides stock ticker data for QQQ and SPY.
+ Langchain: Framework connecting GPT-4 with the internet to extract insights.
+ Google's Gmail API: Used to scrape daily market heatmap image from stocktwits.com emails.
+ Python: Main programming language for scripting and data processing.
+ HTML: Used for formatting the newsletter email content.
+ Apache Airflow: Automation tool for scheduling and managing the daily newsletter generation.
+ GitHub Pages: Hosts the basic signup webpage for user subscriptions.

## Setup Instructions
*To set up the GPT NewsLetter project locally, follow these steps:*

1) Clone the repository: git clone https://github.com/your-username/GPT-NewsLetter.git
2) Set up the required APIs: Obtain API keys for New York Times, AlphaVantage, and Google's Gmail API.
3) Configure the Langchain framework with GPT-4 API.
4) Set up Apache Airflow and configure the scheduled task for the newsletter generation.
5) Customize the HTML template for the newsletter email.

## Usage
+ Ensure all APIs and frameworks are set up and configured properly.
+ Run the Python scripts to pull news from the New York Times API and stock data from AlphaVantage API.
+ Use Langchain to gather insights from the retrieved news.
+ Scrape the daily market heatmap image using Google's Gmail API.
+ Generate the newsletter content using GPT-4.
+ Format the email content with HTML and attach the market heatmap image.
+ Deploy the newsletter through the scheduled Apache Airflow task.

## Automation
The GPT NewsLetter project is designed to be fully automated using Apache Airflow. The scheduled workflow involves running the necessary Python scripts and generating the newsletter content at a specific time every day. This automation ensures consistent and timely delivery of the newsletter to subscribers.

## Contributing
Contributions to this project are welcome! If you have ideas for improvements or new features, please follow these steps:

+ Fork the repository.
+ Create a new branch for your feature: git checkout -b feature-name
+ Commit your changes: git commit -m "Add new feature"
+ Push to the branch: git push origin feature-name
+ Open a pull request, describing your feature and the changes you've made.
+ Contact Information

For questions, suggestions, or feedback, please contact the project maintainer at your@email.com. We appreciate your interest and contributions!
Thank you for using GPT NewsLetter for staying updated on Macroeconomics and Stock Market news!
