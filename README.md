# Discussion-Microscope

**Discussion Microscope** is a web-based application that analyzes and visualizes online discussions by classifying text into predefined topics. It leverages Natural Language Processing (NLP) using `spaCy` and provides interactive visualizations to help users explore the data.

## Features

- **File Upload**: Upload a CSV file containing discussion data with a `text` column.
- **Topic Classification**: Classifies text into predefined topics such as Technology, Health, Finance, Education, and Sports using `spaCy`.
- **Topic Distribution Visualization**: Displays a bar chart showing the distribution of topics in the dataset.
- **Word Cloud Visualization**: Generates word clouds for each topic to highlight the most frequently occurring words.

## Tech Stack

- **Python**: Programming language used for the application.
- **Streamlit**: Framework for building interactive web applications.
- **spaCy**: NLP library used for text tokenization and processing.
- **Pandas**: Library for data manipulation and analysis.
- **Plotly**: Library for creating interactive visualizations (bar charts).
- **WordCloud**: Library for generating word clouds.
- **Matplotlib**: Used to render word clouds.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd discussion_microscope
   ```

2. Install the required dependencies:
   ```bash
   pip install streamlit pandas plotly spacy wordcloud matplotlib
   python -m spacy download en_core_web_sm
   ```

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Upload a CSV file containing a `text` column with the discussion data.

3. Explore the results:
   - View the classified topics in a table.
   - Analyze the topic distribution using the bar chart.
   - Explore the word clouds for each topic.

## Example Dataset

The uploaded CSV file should have the following structure:

| text                              |
|-----------------------------------|
| AI is transforming technology.   |
| The doctor prescribed medicine.  |
| Stock markets are volatile today.|
| Students are learning online.    |
| Football is a popular sport.     |

## Screenshots

### Topic Classification Results
![Topic Classification Results](example_topic_classification.png)

### Topic Distribution
![Topic Distribution](example_topic_distribution.png)

### Word Cloud
![Word Cloud](example_word_cloud.png)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [spaCy](https://spacy.io/) for NLP processing.
- [Streamlit](https://streamlit.io/) for building the interactive web app.
- [Plotly](https://plotly.com/) and [WordCloud](https://github.com/amueller/word_cloud) for visualizations.
