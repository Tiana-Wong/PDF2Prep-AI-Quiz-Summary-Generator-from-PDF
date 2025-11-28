#!/usr/bin/env python3
"""
Batch Quiz and Summary Generator for Math Materials
Processes all PDFs in Math_Materials folder and generates:
- Math-focused quizzes with multiple choice questions
- Comprehensive summaries
- Mathematical formulas and concepts
- Practice problems for revision
"""

import os
import json
import sys
from pathlib import Path
from src.llama_quiz_generator import QuizGenerator
import PyPDF2
import io

class MathMaterialsProcessor:
    def __init__(self):
        self.quiz_generator = QuizGenerator()
        self.materials_dir = Path(__file__).parent / "Math_Materials"
        self.output_dir = Path(__file__).parent / "generated_materials"
        self.output_dir.mkdir(exist_ok=True)
        
    def extract_pdf_text(self, pdf_path):
        """Extract text from PDF file."""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                return text
        except Exception as e:
            print(f"Error extracting text from {pdf_path}: {e}")
            return None

    def get_pdf_files(self):
        """Get all PDF files from Math_Materials folder."""
        pdf_files = sorted(self.materials_dir.glob("*.pdf"))
        return pdf_files

    def generate_math_quiz(self, text, question_count=10, difficulty="medium"):
        """Generate a math-focused quiz with emphasis on calculations and concepts."""
        prompt = f"""
        Generate {question_count} multiple choice questions specifically for MATHEMATICS in games and animations.
        Focus on: calculations, formulas, numerical problems, mathematical concepts, and practical applications.
        The questions should be of {difficulty} difficulty.
        
        For each question, provide:
        1. The question text (include numerical values where applicable)
        2. Four options labeled A, B, C, D (include calculations or formulas)
        3. The correct answer letter
        
        Format the output as a list of dictionaries:
        [
            {{"question": "What is the result of...?", 
              "options": ["A) Value1", "B) Value2", "C) Value3", "D) Value4"],
              "answer": "A"}}
        ]

        Text: {text[:5000]}
        """
        
        try:
            response = self.quiz_generator.co.generate(
                model='command',
                prompt=prompt,
                max_tokens=3000,
                temperature=0.7,
                k=0,
                stop_sequences=[],
                return_likelihoods='NONE'
            )
            generated_text = response.generations[0].text
            quiz_text = generated_text.replace("```json", "").replace("```", "").strip()
            quiz_data = json.loads(quiz_text)
            if isinstance(quiz_data, list):
                return quiz_data
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            # Fallback to general quiz generation
            return self.quiz_generator.generate_quiz(text, question_count, difficulty)
        except Exception as e:
            print(f"Error generating math quiz: {e}")
            return []

    def generate_math_summary(self, text):
        """Generate a comprehensive summary with mathematical formulas and concepts."""
        prompt = f"""
        Create a comprehensive summary of the following mathematics material for games and animations.
        Include:
        1. Main mathematical concepts
        2. Key formulas (write them clearly)
        3. Practical applications
        4. Important definitions
        5. Tips for revision
        
        Organize the summary clearly with sections. Make it suitable for exam revision.
        
        Content:
        {text[:4000]}
        """
        
        try:
            response = self.quiz_generator.co.generate(
                model='command',
                prompt=prompt,
                max_tokens=800,
                temperature=0.5,
                k=0,
                stop_sequences=[],
                return_likelihoods='NONE'
            )
            return response.generations[0].text.strip()
        except Exception as e:
            print(f"Error generating summary: {e}")
            return "Summary generation failed."

    def generate_key_formulas(self, text):
        """Extract and format key mathematical formulas."""
        prompt = f"""
        Extract and list ALL mathematical formulas and equations from the following text.
        Format each formula clearly with:
        1. The formula
        2. What it represents
        3. When to use it
        
        Example format:
        - Formula: distance = speed × time
          Represents: The relationship between distance, speed, and time
          When to use: When calculating travel distance in animations
        
        Content:
        {text[:4000]}
        """
        
        try:
            response = self.quiz_generator.co.generate(
                model='command',
                prompt=prompt,
                max_tokens=800,
                temperature=0.3,
                k=0,
                stop_sequences=[],
                return_likelihoods='NONE'
            )
            return response.generations[0].text.strip()
        except Exception as e:
            print(f"Error extracting formulas: {e}")
            return "Formula extraction failed."

    def generate_practice_problems(self, text):
        """Generate practical math problems for revision."""
        prompt = f"""
        Create 5 practical math problems for revision based on the following material.
        Each problem should:
        1. Be based on real-world game/animation scenarios
        2. Require mathematical calculation
        3. Include a solution with step-by-step explanation
        
        Format:
        Problem 1:
        [Problem statement]
        Solution:
        [Step-by-step solution]
        
        Content:
        {text[:4000]}
        """
        
        try:
            response = self.quiz_generator.co.generate(
                model='command',
                prompt=prompt,
                max_tokens=800,
                temperature=0.7,
                k=0,
                stop_sequences=[],
                return_likelihoods='NONE'
            )
            return response.generations[0].text.strip()
        except Exception as e:
            print(f"Error generating practice problems: {e}")
            return "Practice problems generation failed."

    def process_all_materials(self):
        """Process all PDF materials and generate quizzes and summaries."""
        pdf_files = self.get_pdf_files()
        
        if not pdf_files:
            print("No PDF files found in Math_Materials folder!")
            return
        
        print(f"Found {len(pdf_files)} PDF files. Processing...")
        print("=" * 80)
        
        all_results = {}
        
        for idx, pdf_file in enumerate(pdf_files, 1):
            print(f"\n[{idx}/{len(pdf_files)}] Processing: {pdf_file.name}")
            print("-" * 80)
            
            # Extract text
            text = self.extract_pdf_text(pdf_file)
            if not text or len(text.strip()) < 100:
                print(f"  ⚠️  Could not extract sufficient text from {pdf_file.name}")
                continue
            
            file_stem = pdf_file.stem
            print(f"  ✓ Extracted text ({len(text)} characters)")
            
            # Create file-specific output
            file_output = {
                "filename": pdf_file.name,
                "file_stem": file_stem,
            }
            
            # Generate quiz
            print("  → Generating math quiz...")
            quiz = self.generate_math_quiz(text, question_count=8)
            file_output["quiz"] = quiz
            print(f"  ✓ Generated {len(quiz)} quiz questions")
            
            # Generate summary
            print("  → Generating comprehensive summary...")
            summary = self.generate_math_summary(text)
            file_output["summary"] = summary
            print(f"  ✓ Generated summary ({len(summary)} characters)")
            
            # Generate formulas
            print("  → Extracting mathematical formulas...")
            formulas = self.generate_key_formulas(text)
            file_output["formulas"] = formulas
            print(f"  ✓ Extracted formulas ({len(formulas)} characters)")
            
            # Generate practice problems
            print("  → Generating practice problems...")
            practice = self.generate_practice_problems(text)
            file_output["practice_problems"] = practice
            print(f"  ✓ Generated practice problems ({len(practice)} characters)")
            
            all_results[file_stem] = file_output
            
            # Save individual file results
            output_file = self.output_dir / f"{file_stem}_materials.json"
            with open(output_file, 'w') as f:
                json.dump(file_output, f, indent=2)
            print(f"  ✓ Saved to {output_file.name}")
        
        # Save combined results
        combined_file = self.output_dir / "all_materials_combined.json"
        with open(combined_file, 'w') as f:
            json.dump(all_results, f, indent=2)
        print("\n" + "=" * 80)
        print(f"✓ All materials processed successfully!")
        print(f"  Combined results saved to: {combined_file.name}")
        print(f"  Individual files saved in: {self.output_dir}/")
        
        return all_results

    def generate_html_revision_guide(self, results):
        """Generate an HTML revision guide from all materials."""
        html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Math Materials Revision Guide</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            padding: 40px;
        }
        h1 {
            color: #667eea;
            margin-bottom: 10px;
            text-align: center;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            font-size: 14px;
        }
        .material-section {
            margin-bottom: 40px;
            border-left: 4px solid #667eea;
            padding-left: 20px;
        }
        .material-section h2 {
            color: #667eea;
            margin-bottom: 15px;
            font-size: 24px;
        }
        .subsection {
            margin-bottom: 25px;
        }
        .subsection h3 {
            color: #764ba2;
            margin-bottom: 10px;
            font-size: 18px;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 5px;
        }
        .quiz-question {
            background: #f5f5f5;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
            border-left: 3px solid #667eea;
        }
        .quiz-question strong {
            display: block;
            margin-bottom: 10px;
            color: #333;
        }
        .options {
            margin-left: 20px;
        }
        .option {
            padding: 5px 0;
            color: #555;
        }
        .answer {
            color: #28a745;
            font-weight: bold;
            margin-top: 5px;
        }
        .formula-box {
            background: #f0f4ff;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
            border-left: 3px solid #764ba2;
            font-family: 'Courier New', monospace;
        }
        .practice-problem {
            background: #fff9f0;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
            border-left: 3px solid #ff9800;
        }
        .summary-text {
            background: #f9f9f9;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
            line-height: 1.8;
        }
        .table-of-contents {
            background: #f5f5f5;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 30px;
        }
        .table-of-contents h3 {
            margin-bottom: 15px;
            color: #667eea;
        }
        .table-of-contents ul {
            list-style: none;
        }
        .table-of-contents li {
            margin: 8px 0;
        }
        .table-of-contents a {
            color: #667eea;
            text-decoration: none;
        }
        .table-of-contents a:hover {
            text-decoration: underline;
        }
        footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
            color: #999;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📚 Math Materials Revision Guide</h1>
        <p class="subtitle">Complete Study Guide for Mathematics in Games and Animations</p>
"""
        
        # Generate table of contents
        html_content += '<div class="table-of-contents"><h3>Table of Contents</h3><ul>'
        for stem, data in results.items():
            clean_name = data.get("filename", stem).replace(".pdf", "").replace("GAME2016 ", "")
            html_content += f'<li><a href="#{stem}">{clean_name}</a></li>'
        html_content += '</ul></div>'
        
        # Generate content for each material
        for stem, data in results.items():
            filename = data.get("filename", stem)
            clean_name = filename.replace(".pdf", "").replace("GAME2016 ", "")
            
            html_content += f'''
    <div class="material-section" id="{stem}">
        <h2>{clean_name}</h2>
        
        <div class="subsection">
            <h3>📖 Summary</h3>
            <div class="summary-text">{data.get("summary", "N/A")}</div>
        </div>
        
        <div class="subsection">
            <h3>📐 Key Formulas & Concepts</h3>
            <div class="formula-box">{data.get("formulas", "N/A").replace(chr(10), "<br>")}</div>
        </div>
        
        <div class="subsection">
            <h3>✏️ Quiz Questions</h3>
'''
            
            quiz = data.get("quiz", [])
            if isinstance(quiz, list):
                for q_idx, question in enumerate(quiz, 1):
                    if isinstance(question, dict):
                        html_content += f'''
            <div class="quiz-question">
                <strong>Q{q_idx}: {question.get("question", "N/A")}</strong>
                <div class="options">
'''
                        options = question.get("options", [])
                        if isinstance(options, list):
                            for opt in options:
                                html_content += f'                    <div class="option">{opt}</div>\n'
                        
                        answer = question.get("answer", "N/A")
                        correct_opt = next((o for o in options if o.startswith(answer + ")")), answer)
                        html_content += f'                    <div class="answer">Answer: {correct_opt}</div>\n'
                        html_content += '                </div>\n            </div>\n'
            
            html_content += '''
        </div>
        
        <div class="subsection">
            <h3>🎯 Practice Problems</h3>
            <div class="practice-problem">
'''
            practice = data.get("practice_problems", "N/A")
            html_content += practice.replace('\n', '<br>')
            html_content += '''
            </div>
        </div>
    </div>
'''
        
        html_content += '''
        <footer>
            <p>Generated by PDF2Prep Math Materials Processor</p>
            <p>Use this guide for comprehensive exam revision</p>
        </footer>
    </div>
</body>
</html>
'''
        
        html_file = self.output_dir / "revision_guide.html"
        with open(html_file, 'w') as f:
            f.write(html_content)
        print(f"✓ HTML revision guide saved to: {html_file.name}")
        return html_file

def main():
    print("\n" + "=" * 80)
    print("🚀 PDF2Prep - Math Materials Batch Processor")
    print("=" * 80)
    
    try:
        processor = MathMaterialsProcessor()
        print(f"📁 Looking for PDFs in: {processor.materials_dir}")
        
        # Process all materials
        results = processor.process_all_materials()
        
        if results:
            # Generate HTML revision guide
            print("\n→ Generating HTML revision guide...")
            processor.generate_html_revision_guide(results)
            
            print("\n" + "=" * 80)
            print("✅ SUCCESSFULLY COMPLETED!")
            print("=" * 80)
            print("\n📦 Generated Materials:")
            print(f"  • Combined JSON: {processor.output_dir / 'all_materials_combined.json'}")
            print(f"  • HTML Guide: {processor.output_dir / 'revision_guide.html'}")
            print(f"  • Individual files in: {processor.output_dir}/")
            print("\n💡 Tip: Open 'revision_guide.html' in your browser for the best viewing experience!")
            print("=" * 80 + "\n")
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
