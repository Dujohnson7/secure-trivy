#!/usr/bin/env python3
from flask import Flask, send_from_directory
import os

app = Flask(__name__)
 
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beautiful Python Static Site</title>
    <style>
        /* Modern CSS with beautiful styling */
        :root {
            --primary: #4361ee;
            --secondary: #3f37c9;
            --accent: #4895ef;
            --light: #f8f9fa;
            --dark: #212529;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--dark);
            margin: 0;
            padding: 0;
            background-color: #f5f7fa;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        header {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 2rem 0;
            text-align: center;
            margin-bottom: 2rem;
            border-radius: 0 0 10px 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            margin: 0;
            font-size: 2.5rem;
        }
        
        .card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        
        .card h2 {
            color: var(--primary);
            margin-top: 0;
        }
        
        .btn {
            display: inline-block;
            background: var(--accent);
            color: white;
            padding: 0.6rem 1.2rem;
            border-radius: 4px;
            text-decoration: none;
            transition: background 0.3s ease;
            border: none;
            cursor: pointer;
            font-size: 1rem;
        }
        
        .btn:hover {
            background: var(--secondary);
        }
        
        footer {
            text-align: center;
            padding: 2rem 0;
            margin-top: 2rem;
            color: #6c757d;
            border-top: 1px solid #dee2e6;
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 1rem;
            }
            
            h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Welcome to My Beautiful Static Site</h1>
            <p>Built with Python and Flask</p>
        </div>
    </header>
    
    <main class="container">
        <div class="card">
            <h2>About This Page</h2>
            <p>This is a completely static website served from a single Python file. It includes HTML, CSS, and JavaScript all in one place.</p>
            <p>The styling is modern and responsive, working well on both desktop and mobile devices.</p>
        </div>
        
        <div class="card">
            <h2>Features</h2>
            <ul>
                <li>Single file deployment</li>
                <li>Beautiful modern design</li>
                <li>Responsive layout</li>
                <li>Interactive elements</li>
            </ul>
            <button id="demoBtn" class="btn">Click Me</button>
            <p id="demoText" style="display: none; margin-top: 1rem;">You clicked the button! This is JavaScript in action.</p>
        </div>
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2023 Beautiful Python Static Site</p>
        </div>
    </footer>
    
    <script>
        // Simple JavaScript for interactivity
        document.getElementById('demoBtn').addEventListener('click', function() {
            const demoText = document.getElementById('demoText');
            demoText.style.display = demoText.style.display === 'none' ? 'block' : 'none';
        });
        
        // Change header color on mouseover
        const header = document.querySelector('header');
        header.addEventListener('mouseover', function() {
            this.style.background = 'linear-gradient(135deg, #3a0ca3, #4361ee)';
        });
        
        header.addEventListener('mouseout', function() {
            this.style.background = 'linear-gradient(135deg, #4361ee, #3f37c9)';
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML_TEMPLATE

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                              'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)