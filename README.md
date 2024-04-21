# Resume Skills Extractor

## Overview

This project is a Flask-based web application that extracts skills from resumes using machine learning techniques. It provides a simple API endpoint for processing resumes and extracting skills information.

## Features

- **Resume Processing**: Upload resumes and extract skills information.
- **Skill Extraction**: Utilizes machine learning models to parse resumes and extract relevant skills.
- **Filtering**: Filters extracted skills and eliminates irrelevant or common terms.

## Installation

1. Make sure you have Python v3.11.8 installed. If not, you can download it from the [official Python website](https://www.python.org/downloads/).

2. Clone the repository:

   ```bash
   git clone https://github.com/ThamerAyachi/pyresparser_python.git
   ```

3. Navigate to the project directory:

   ```bash
   cd pyresparser_python
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. The application will start running locally. You can access it at http://localhost:5000.

3. Send a POST request to the /process endpoint with a resume file attached.Example using curl:

   ```bash
   curl -X POST -F "resume=@/path/to/your/resume.pdf" http://localhost:5000/process
   ```

4. The server will process the resume, extract skills, and return the extracted skills in JSON format.

## API Reference

### Process Resume

```
POST /process
```

### Request Parameters

| Parameter | Type | Description                           |
| :-------- | :--- | :------------------------------------ |
| resume    | file | The resume file to be processed (PDF) |

### Response

- **200 OK:** Skills extracted successfully.
- **400 Bad Request:** If no resume file is provided.

### Example Response:

```json
{
  "skills": ["Python", "Machine Learning", "Data Analysis"]
}
```
