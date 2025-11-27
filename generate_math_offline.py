#!/usr/bin/env python3
"""
Offline Math Materials Quiz and Summary Generator
Generates structured quizzes and comprehensive summaries from PDFs
using local processing without external API dependencies
"""

import os
import json
import re
from pathlib import Path
from collections import defaultdict
import PyPDF2

class OfflineMathMaterialsProcessor:
    def __init__(self):
        self.materials_dir = Path(__file__).parent / "Math_Materials"
        self.output_dir = Path(__file__).parent / "generated_materials"
        self.output_dir.mkdir(exist_ok=True)
        
        # Math terminology and concepts for quiz generation
        self.math_terms = {
            'vector': ['magnitude', 'direction', 'component', 'dot product'],
            'matrix': ['determinant', 'inverse', 'transpose', 'eigenvalue'],
            'coordinate': ['cartesian', 'polar', 'spherical', 'cylindrical'],
            'rotation': ['quaternion', 'euler angles', 'axis-angle', 'rotation matrix'],
            'transformation': ['translation', 'scaling', 'shear', 'perspective'],
            'collision': ['AABB', 'sphere', 'ray-casting', 'SAT'],
            'animation': ['interpolation', 'keyframe', 'easing', 'lerp'],
            'harmonic': ['oscillation', 'frequency', 'amplitude', 'phase']
        }
        
    def extract_pdf_text(self, pdf_path):
        """Extract text from PDF file."""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                metadata = {
                    'pages': len(pdf_reader.pages),
                    'title': pdf_reader.metadata.title if pdf_reader.metadata else "Unknown"
                }
                for page_num, page in enumerate(pdf_reader.pages):
                    page_text = page.extract_text()
                    if page_text:
                        text += f"[Page {page_num + 1}]\n{page_text}\n"
                return text, metadata
        except Exception as e:
            print(f"Error extracting text from {pdf_path}: {e}")
            return None, None

    def get_pdf_files(self):
        """Get all PDF files from Math_Materials folder."""
        pdf_files = sorted(self.materials_dir.glob("*.pdf"))
        return pdf_files

    def extract_sections(self, text):
        """Extract major sections/topics from text."""
        # Look for numbered sections, headings, etc.
        sections = []
        
        # Split by common heading patterns
        lines = text.split('\n')
        current_section = None
        section_content = []
        
        for line in lines:
            # Check if line is a heading (multiple capitals, numbered, etc.)
            if (re.match(r'^[A-Z\d\s\-\.]{5,}$', line.strip()) or 
                re.match(r'^\d+\s+[A-Z]', line.strip()) or
                re.match(r'^[A-Z][a-z]+\s+[A-Z]', line.strip())):
                if current_section and section_content:
                    sections.append({
                        'title': current_section,
                        'content': '\n'.join(section_content).strip()
                    })
                current_section = line.strip()
                section_content = []
            elif current_section:
                section_content.append(line)
        
        if current_section and section_content:
            sections.append({
                'title': current_section,
                'content': '\n'.join(section_content).strip()
            })
        
        return sections if sections else [{'title': 'Content', 'content': text}]

    def extract_formulas(self, text):
        """Extract mathematical formulas and equations."""
        formulas = []
        
        # Patterns for formulas
        patterns = [
            r'([a-zA-Z_]\w*)\s*=\s*([^.;:\n]+)',  # Simple equations
            r'formula[:\s]+([^.;:\n]+)',  # Explicit formula mentions
            r'equation[:\s]+([^.;:\n]+)',  # Explicit equation mentions
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                formula_text = match.group(0).strip()
                if len(formula_text) < 200 and not formula_text.endswith('?'):
                    formulas.append(formula_text)
        
        # Also extract lines with mathematical symbols
        symbol_patterns = [r'[√∑∫∂∆π∞α-ωΑ-Ω×÷±]', r'\^\d+', r'\[\s*\w+\s*\]']
        for line in text.split('\n'):
            if any(re.search(sp, line) for sp in symbol_patterns):
                clean_line = line.strip()
                if 5 < len(clean_line) < 200 and clean_line not in formulas:
                    formulas.append(clean_line)
        
        return list(set(formulas))[:20]  # Return top 20 unique formulas

    def extract_key_concepts(self, text, title):
        """Extract key mathematical concepts."""
        concepts = []
        
        # Look for mathematical terms relevant to the title
        for term, subtopics in self.math_terms.items():
            if term.lower() in text.lower():
                concepts.append({
                    'concept': term.title(),
                    'subtopics': subtopics,
                    'mentions': len(re.findall(r'\b' + term + r'\b', text, re.IGNORECASE))
                })
        
        # Extract numbers and their context (likely important values)
        numbers = re.findall(r'\b(\d+\.?\d*)\b', text)
        if numbers:
            concepts.append({
                'concept': 'Numerical Values',
                'values': sorted(set(numbers))[:10]
            })
        
        return sorted(concepts, key=lambda x: x.get('mentions', 0), reverse=True)[:10]

    def generate_math_questions(self, text, title, num_questions=8):
        """Generate math quiz questions from text content."""
        questions = []
        
        # Question templates based on content
        templates = [
            {
                'type': 'definition',
                'template': 'What does the term "{term}" refer to in this context?',
                'answer_pattern': r'{term}[^.]*\.'
            },
            {
                'type': 'formula',
                'template': 'Which of the following correctly represents {concept}?',
                'answer_pattern': r'formula|equation|represented'
            },
            {
                'type': 'application',
                'template': 'In {context}, the {concept} is used to:',
                'answer_pattern': None
            },
            {
                'type': 'calculation',
                'template': 'If {variable} equals X and {variable2} equals Y, what is the result?',
                'answer_pattern': None
            },
            {
                'type': 'concept',
                'template': 'Which characteristic is NOT true about {concept}?',
                'answer_pattern': None
            }
        ]
        
        # Extract sentences for question base
        sentences = [s.strip() for s in re.split(r'[.!?]', text) if len(s.strip()) > 20]
        
        # Generate questions based on extracted content
        question_count = 0
        for i, sentence in enumerate(sentences[:num_questions * 2]):
            if question_count >= num_questions:
                break
            
            # Create a question from meaningful content
            words = sentence.split()
            if len(words) > 5:
                # Extract potential answer
                answer_idx = min(2, len(words) - 1)
                correct_answer = words[answer_idx]
                
                question = {
                    'question': f"{sentence.split(':')[0]}?",
                    'options': [
                        f"A) {correct_answer}",
                        f"B) {words[max(0, answer_idx - 1)] if answer_idx > 0 else 'Alternative'}",
                        f"C) {words[min(len(words)-1, answer_idx + 1)] if answer_idx < len(words)-1 else 'Other'}",
                        f"D) {words[answer_idx + 2] if answer_idx + 2 < len(words) else 'None of the above'}"
                    ],
                    'answer': 'A',
                    'difficulty': 'medium'
                }
                questions.append(question)
                question_count += 1
        
        return questions

    def generate_comprehensive_summary(self, text, title):
        """Generate a comprehensive summary with key points."""
        summary = {
            'title': title,
            'overview': '',
            'key_concepts': [],
            'formulas': [],
            'applications': [],
            'revision_tips': []
        }
        
        # Generate overview from first paragraphs
        paragraphs = re.split(r'\n\n+', text)
        overview_text = ' '.join([p for p in paragraphs[:3] if len(p.strip()) > 50])
        summary['overview'] = overview_text[:500]  # First 500 chars
        
        # Extract key concepts
        concepts = self.extract_key_concepts(text, title)
        summary['key_concepts'] = [
            f"• {c['concept']}: {', '.join(c.get('subtopics', [])[:3])}"
            for c in concepts
        ]
        
        # Extract formulas
        formulas = self.extract_formulas(text)
        summary['formulas'] = formulas
        
        # Generate applications
        app_sentences = [s.strip() for s in re.split(r'[.!?]', text) 
                        if 'used' in s.lower() or 'apply' in s.lower() or 'application' in s.lower()]
        summary['applications'] = app_sentences[:5]
        
        # Add revision tips
        summary['revision_tips'] = [
            "1. Focus on understanding the core formulas and when to use them",
            "2. Practice working through numerical examples",
            "3. Understand the geometric or visual interpretation",
            "4. Relate concepts to real-world game/animation scenarios",
            "5. Create flashcards for key terms and definitions"
        ]
        
        return summary

    def generate_practice_problems(self, text, title):
        """Generate practice problems for revision."""
        problems = []
        
        # Extract numerical content
        numbers = re.findall(r'\b\d+\.?\d*\b', text)
        
        problem_templates = [
            {
                'template': 'Calculate the result when applying {concept} to the values {values}',
                'solution': 'Refer to the {concept} formula: work through step by step'
            },
            {
                'template': 'Explain how {concept} differs from {related_concept}',
                'solution': 'Consider the definitions, properties, and applications of each'
            },
            {
                'template': 'Apply {concept} to a scenario with {scenario}',
                'solution': 'Break down the problem using the relevant formula or definition'
            }
        ]
        
        concepts = self.extract_key_concepts(text, title)
        concept_names = [c['concept'] for c in concepts]
        
        for i, template in enumerate(problem_templates[:5]):
            if concept_names:
                concept = concept_names[i % len(concept_names)]
                problem = {
                    'number': i + 1,
                    'problem': template['template'].format(
                        concept=concept,
                        related_concept=concept_names[(i+1) % len(concept_names)] if len(concept_names) > 1 else 'alternative approach',
                        values=', '.join(numbers[:2]) if numbers else 'given values',
                        scenario='game animation' if i % 2 == 0 else '3D modeling'
                    ),
                    'solution': template['solution'].format(concept=concept)
                }
                problems.append(problem)
        
        return problems

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
            text, metadata = self.extract_pdf_text(pdf_file)
            if not text or len(text.strip()) < 100:
                print(f"  ⚠️  Could not extract sufficient text from {pdf_file.name}")
                continue
            
            file_stem = pdf_file.stem
            print(f"  ✓ Extracted text ({len(text)} characters, {metadata['pages']} pages)")
            
            # Create file-specific output
            file_output = {
                "filename": pdf_file.name,
                "file_stem": file_stem,
                "metadata": metadata,
            }
            
            # Generate quiz
            print("  → Generating math quiz...")
            quiz = self.generate_math_questions(text, pdf_file.name, num_questions=8)
            file_output["quiz"] = quiz
            print(f"  ✓ Generated {len(quiz)} quiz questions")
            
            # Generate summary
            print("  → Generating comprehensive summary...")
            summary = self.generate_comprehensive_summary(text, pdf_file.name)
            file_output["summary"] = summary
            print(f"  ✓ Generated comprehensive summary")
            
            # Generate practice problems
            print("  → Generating practice problems...")
            practice = self.generate_practice_problems(text, pdf_file.name)
            file_output["practice_problems"] = practice
            print(f"  ✓ Generated {len(practice)} practice problems")
            
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
    <title>Math Materials Revision Guide - Games & Animations</title>
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
            page-break-inside: avoid;
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
        .overview {
            background: #f0f4ff;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 15px;
            border-left: 3px solid #667eea;
        }
        .key-concepts {
            background: #fff4f0;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 15px;
            border-left: 3px solid #ff7043;
        }
        .key-concepts ul {
            list-style: none;
            margin-left: 20px;
        }
        .key-concepts li {
            margin: 5px 0;
            color: #555;
        }
        .quiz-question {
            background: #f5f5f5;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
            border-left: 3px solid #667eea;
            page-break-inside: avoid;
        }
        .quiz-question strong {
            display: block;
            margin-bottom: 10px;
            color: #333;
        }
        .options {
            margin-left: 20px;
            font-size: 14px;
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
            padding: 12px;
            margin-bottom: 10px;
            border-radius: 5px;
            border-left: 3px solid #764ba2;
            font-family: 'Courier New', monospace;
            font-size: 13px;
        }
        .practice-problem {
            background: #fff9f0;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
            border-left: 3px solid #ff9800;
            page-break-inside: avoid;
        }
        .problem-title {
            font-weight: bold;
            margin-bottom: 5px;
            color: #ff6f00;
        }
        .problem-solution {
            margin-top: 10px;
            padding-top: 10px;
            border-top: 1px solid #ffe0b2;
            font-size: 14px;
            color: #666;
        }
        .revision-tips {
            background: #f0fff4;
            padding: 15px;
            border-radius: 5px;
            border-left: 3px solid #4caf50;
        }
        .revision-tips ul {
            list-style: none;
            margin-left: 0;
        }
        .revision-tips li {
            margin: 8px 0;
            color: #333;
            padding-left: 20px;
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
        .applications {
            background: #f5f5f5;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 15px;
        }
        .applications ul {
            list-style: none;
            margin-left: 20px;
        }
        .applications li {
            margin: 5px 0;
            color: #555;
        }
        footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
            color: #999;
            font-size: 12px;
        }
        @media print {
            body { background: white; }
            .container { box-shadow: none; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📚 Math Materials Revision Guide</h1>
        <p class="subtitle">Complete Study Guide for Mathematics in Games and Animations</p>
        <p class="subtitle">Generated from course lectures</p>
"""
        
        # Generate table of contents
        html_content += '<div class="table-of-contents"><h3>📋 Table of Contents</h3><ul>'
        for stem, data in results.items():
            clean_name = data.get("filename", stem).replace(".pdf", "").replace("GAME2016 ", "")
            html_content += f'<li><a href="#{stem}">{clean_name}</a></li>'
        html_content += '</ul></div>'
        
        # Generate content for each material
        for stem, data in results.items():
            filename = data.get("filename", stem)
            clean_name = filename.replace(".pdf", "").replace("GAME2016 ", "")
            summary = data.get("summary", {})
            
            html_content += f'''
    <div class="material-section" id="{stem}">
        <h2>{clean_name}</h2>
        
        <div class="subsection">
            <h3>📖 Overview</h3>
            <div class="overview">{summary.get("overview", "N/A")}</div>
        </div>
        
        <div class="subsection">
            <h3>🎯 Key Concepts</h3>
            <div class="key-concepts">
                <ul>
'''
            
            for concept in summary.get("key_concepts", [])[:8]:
                html_content += f'                    <li>{concept}</li>\n'
            
            html_content += '''
                </ul>
            </div>
        </div>
        
        <div class="subsection">
            <h3>📐 Formulas & Equations</h3>
'''
            
            for formula in summary.get("formulas", [])[:10]:
                html_content += f'            <div class="formula-box">{formula}</div>\n'
            
            html_content += '''
        </div>
        
        <div class="subsection">
            <h3>💡 Applications</h3>
            <div class="applications">
                <ul>
'''
            
            for app in summary.get("applications", [])[:5]:
                html_content += f'                    <li>{app}</li>\n'
            
            html_content += '''
                </ul>
            </div>
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
                        
                        answer = question.get("answer", "A")
                        correct_opt = next((o for o in options if o.startswith(answer)), f"{answer})")
                        html_content += f'                    <div class="answer">✓ Answer: {correct_opt}</div>\n'
                        html_content += '                </div>\n            </div>\n'
            
            html_content += '''
        </div>
        
        <div class="subsection">
            <h3>🎯 Practice Problems</h3>
'''
            
            practice = data.get("practice_problems", [])
            for problem in practice:
                if isinstance(problem, dict):
                    html_content += f'''
            <div class="practice-problem">
                <div class="problem-title">Problem {problem.get("number", "?")}:</div>
                {problem.get("problem", "N/A")}
                <div class="problem-solution">
                    <strong>Solution Approach:</strong> {problem.get("solution", "N/A")}
                </div>
            </div>
'''
            
            html_content += f'''
        </div>
        
        <div class="subsection">
            <h3>✅ Revision Tips</h3>
            <div class="revision-tips">
                <ul>
'''
            
            for tip in summary.get("revision_tips", []):
                html_content += f'                    <li>{tip}</li>\n'
            
            html_content += '''
                </ul>
            </div>
        </div>
    </div>
'''
        
        html_content += '''
        <footer>
            <p>Generated by PDF2Prep Offline Math Materials Processor</p>
            <p>Use this guide for comprehensive exam revision</p>
            <p>Last generated: 2025</p>
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

    def generate_markdown_study_guide(self, results):
        """Generate a markdown study guide."""
        md_content = """# Math Materials Revision Guide
## Mathematics in Games and Animations

**A comprehensive study guide for exam revision**

---

## Table of Contents

"""
        
        # Add TOC
        for stem, data in results.items():
            clean_name = data.get("filename", stem).replace(".pdf", "").replace("GAME2016 ", "")
            toc_name = clean_name.lower().replace(" ", "-")
            md_content += f"- [{clean_name}](#{toc_name})\n"
        
        md_content += "\n---\n\n"
        
        # Add content for each material
        for stem, data in results.items():
            filename = data.get("filename", stem)
            clean_name = filename.replace(".pdf", "").replace("GAME2016 ", "")
            toc_name = clean_name.lower().replace(" ", "-")
            summary = data.get("summary", {})
            
            md_content += f"\n## {clean_name}\n\n"
            md_content += f"### Overview\n\n{summary.get('overview', 'N/A')}\n\n"
            
            md_content += "### Key Concepts\n\n"
            for concept in summary.get("key_concepts", [])[:8]:
                md_content += f"- {concept}\n"
            
            md_content += "\n### Formulas & Equations\n\n"
            for formula in summary.get("formulas", [])[:10]:
                md_content += f"```\n{formula}\n```\n"
            
            md_content += "\n### Applications\n\n"
            for app in summary.get("applications", [])[:5]:
                md_content += f"- {app}\n"
            
            md_content += "\n### Quiz Questions\n\n"
            quiz = data.get("quiz", [])
            for q_idx, question in enumerate(quiz, 1):
                if isinstance(question, dict):
                    md_content += f"\n**Q{q_idx}: {question.get('question', 'N/A')}**\n"
                    for opt in question.get("options", []):
                        md_content += f"- {opt}\n"
                    answer = question.get("answer", "A")
                    md_content += f"\n✓ **Answer: {answer}**\n"
            
            md_content += "\n### Practice Problems\n\n"
            practice = data.get("practice_problems", [])
            for problem in practice:
                if isinstance(problem, dict):
                    md_content += f"\n**Problem {problem.get('number', '?')}:**\n"
                    md_content += f"{problem.get('problem', 'N/A')}\n\n"
                    md_content += f"**Solution Approach:** {problem.get('solution', 'N/A')}\n"
            
            md_content += "\n### Revision Tips\n\n"
            for tip in summary.get("revision_tips", []):
                md_content += f"- {tip}\n"
            
            md_content += "\n---\n"
        
        md_file = self.output_dir / "revision_guide.md"
        with open(md_file, 'w') as f:
            f.write(md_content)
        print(f"✓ Markdown study guide saved to: {md_file.name}")
        return md_file


def main():
    print("\n" + "=" * 80)
    print("🚀 PDF2Prep - Offline Math Materials Batch Processor")
    print("=" * 80)
    
    try:
        processor = OfflineMathMaterialsProcessor()
        print(f"📁 Looking for PDFs in: {processor.materials_dir}")
        
        # Process all materials
        results = processor.process_all_materials()
        
        if results:
            # Generate HTML revision guide
            print("\n→ Generating HTML revision guide...")
            processor.generate_html_revision_guide(results)
            
            # Generate Markdown guide
            print("→ Generating Markdown study guide...")
            processor.generate_markdown_study_guide(results)
            
            print("\n" + "=" * 80)
            print("✅ SUCCESSFULLY COMPLETED!")
            print("=" * 80)
            print("\n📦 Generated Materials:")
            print(f"  • Combined JSON: {processor.output_dir / 'all_materials_combined.json'}")
            print(f"  • HTML Guide: {processor.output_dir / 'revision_guide.html'}")
            print(f"  • Markdown Guide: {processor.output_dir / 'revision_guide.md'}")
            print(f"  • Individual files in: {processor.output_dir}/")
            print("\n💡 Tips:")
            print("  • Open 'revision_guide.html' in your browser for the best viewing experience")
            print("  • You can print the HTML to PDF for offline studying")
            print("  • Use 'revision_guide.md' for markdown readers")
            print("  • JSON files contain structured data for programmatic access")
            print("=" * 80 + "\n")
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
