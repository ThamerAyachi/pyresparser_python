from flask import Flask, jsonify, request
from manager.files import save_file, delete_file
from extracter.resume_parser import parser_resume
from extracter.clean import main as merge_and_filter_skills
from flask_cors import CORS
from contents.resums import reform

app = Flask(__name__)
CORS(app)


@app.route('/process', methods=['POST'])
def process():
    if 'resume' not in request.files:
        return jsonify({'error': 'Resume file is required'}), 400

    resume = request.files['resume']
    resume_path = save_file(resume)

    data = parser_resume(resume_path)

    delete_file(resume_path)

    skills = merge_and_filter_skills(data)

    return jsonify(skills)


@app.route('/about', methods=['POST'])
def about():
    data = request.json
    job_title = data.get('job_title')

    result = {"description": reform(job_title)}

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
