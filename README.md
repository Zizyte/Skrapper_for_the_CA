

# XKCD Comic Scraper

This is a Python project that scrapes comics from [xkcd.com](https://xkcd.com) using `requests` and `BeautifulSoup`.  
The comics are downloaded and saved to a local folder.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/xkcd-scraper.git
cd xkcd-scraper
````

### 2. Set up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Configure Settings

Make sure the `config.json` file contains the delay setting, for example:

```json
{
  "delay_seconds": 3
}
```

### 5. Run the Script

```bash
python main.py
```

## Features

* Scrapes XKCD comics using BeautifulSoup
* Automatically navigates to the next comic
* Downloads and saves images to a local `comics/` folder
* Respects server load with configurable delay
* Logs errors to `main.log`


---



