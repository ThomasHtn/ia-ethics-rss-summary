# Description
this project aims at filtering and translating the best results of a google alert concerning the topic “ia ethics”.
To learn more about the ethics of ia, I invite you to read this [document](./research_and_development.md)
# Setup

## Virtual environment

Linux :
```bash
python3 -m venv .venv
```

MacOS-Windows
```bash
python -m venv .venv
```

## Activate Virtual environment :
Windows : 
```bash
.venv\Scripts\activate
```

macOS/Linux : 
```bash
source .venv/bin/activate
```

## Dependencies :

* Make sure you're in the project directory
* Install dependencies : `pip install -r requirements.txt`
* Alternatively, you can install the libraries yourself by reading requierements.txt file

## Structure : 
```bash
.
├── app.py
├── articles_summary.md
├── Procfile
├── README.md
├── requirements.txt
├── static
│   └── style.css
└── templates
    └── articles.html
```

## Start APP
```bash
python3 app.py
```