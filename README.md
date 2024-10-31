# Analyze Code

A Streamlit app that analyzes Python code and suggests improvements using AI.

## Features

- Analyzes Python code for improvements
- Multiple focus areas:
  - Error handling
  - Testing
  - Code structure
  - Performance
  - Security
- Provides specific code examples
- Severity levels for suggestions

## Setup

1. Clone the repository:
```bash
git clone [your-repo-url]
cd [repo-name]
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Get an API key from Together AI (https://together.ai)
Add to src/config.py
```
# API Keys
TOGETHER_API_KEY = ""
GITHUB_TOKEN = ""

# Analysis Settings
MAX_FILES_TO_ANALYZE = 50
ANALYSIS_DELAY = 0.1  # seconds between API calls
```

4. Run the app:
```bash
streamlit run src/streamlit_app.py
```

## Usage

1. Enter your Together AI API key
2. Paste your Python code
3. Select focus areas
4. Click "Analyze Code"
5. Review suggestions and improvements

## Example

```python
def divide(a, b):
    return a / b
```

The analyzer will suggest:
- Error handling improvements
- Test cases
- Code structure enhancements