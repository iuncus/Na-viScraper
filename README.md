# Na'vi RNN - Text Generation Project

This project scrapes the "Learn Na'vi" forum, cleans the data, and trains a Recurrent Neural Network (RNN) to generate coherent text in the Na'vi language.


## Usage

### Data Scraping
To scrape forum data and extract Na'vi text:
```bash
python Na'viScraper.py
```

### Data Cleaning
Run the `Na'viCleaner.ipynb` Notebook to clean the scraped data:


### Model Training
Run `Na'viRNN_main.ipynb` to train the RNN model using the cleaned data:


## File Descriptions

- **Na'viScraper.py** - Script for scraping Na'vi language text from the forum.
- **Na'viCleaner.ipynb** - Notebook for cleaning and preprocessing data.
- **Na'viRNN_main.ipynb** - Notebook for building and training the RNN model.
- **cleaned_navi_post.tsv** - Cleaned dataset.
- **navi_post.tsv** - Raw scraped data.
- **README.md** - Project documentation.
