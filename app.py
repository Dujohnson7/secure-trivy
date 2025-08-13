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
    <title>AUCA Innovation Center</title>
    <style>
        :root {
            --auca-blue: #0056b3;
            --auca-red: #e31937;
            --accent: #ffc107;
            --dark: #212529;
            --light: #f8f9fa;
        }

        body {
            font-family: 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: var(--dark);
            background-color: var(--light);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        /* Header with AUCA Gishushu background */
        header {
            background: linear-gradient(rgba(0, 86, 179, 0.8)), 
                        url('https://encyclosource.com/link/api/v1/image/ESDA/EAQQ/EAQQL.jpg');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 5rem 0;
            text-align: center;
            position: relative;
        }

        header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.4);
        }

        .header-content {
            position: relative;
            z-index: 2;
        }

        .logo {
            font-size: 2.8rem;
            font-weight: 700;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }

        nav {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 2rem;
        }

        nav a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            padding: 0.8rem 1.5rem;
            border-radius: 4px;
            transition: all 0.3s;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(5px);
        }

        nav a:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-3px);
        }

        /* Rest of your existing CSS... */
        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }

        .card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .card-content {
            padding: 1.5rem;
        }

        .card h3 {
            color: var(--auca-blue);
            margin-top: 0;
        }

        .btn {
            display: inline-block;
            background: var(--auca-blue);
            color: white;
            padding: 0.6rem 1.2rem;
            border-radius: 4px;
            text-decoration: none;
            margin-top: 1rem;
            transition: all 0.3s;
        }

        .btn:hover {
            background: var(--auca-red);
            transform: translateY(-2px);
        }

        footer {
            background: var(--dark);
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 3rem;
        }

        @media (max-width: 768px) {
            nav {
                flex-direction: column;
                gap: 1rem;
                align-items: center;
            }

            .logo {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <div class="logo">AUCA INNOVATION CENTER</div>
            <p>Driving Technological Innovation in Rwanda</p>
            <nav>
                <a href="#projects">Our Projects</a>
                <a href="#events">Events</a>
                <a href="#incubator">Startup Incubator</a>
                <a href="#contact">Visit Us</a>
            </nav>
        </div>
    </header>

    <!-- Rest of your HTML content remains the same -->
    <main class="container">
        <section id="projects">
            <h2>Featured Innovations</h2>
            <div class="card-grid">
                <div class="card">
                    <img src="https://images.unsplash.com/photo-1620712943543-bcc4688e7485?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1200&q=80" alt="AI Research">
                    <div class="card-content">
                        <h3>AI for African Languages</h3>
                        <p>Developing natural language processing tools for Kinyarwanda and other local languages.</p>
                        <a href="#" class="btn">See Project</a>
                    </div>
                </div>

                <div class="card">
                    <img src="https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1200&q=80" alt="Renewable Energy">
                    <div class="card-content">
                        <h3>Smart Agriculture</h3>
                        <p>IoT solutions for smallholder farmers to optimize crop yields.</p>
                        <a href="#" class="btn">See Project</a>
                    </div>
                </div>

                <div class="card">
                    <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1200&q=80" alt="Digital Literacy">
                    <div class="card-content">
                        <h3>Women in Tech</h3>
                        <p>Empowering female students through coding bootcamps and mentorship.</p>
                        <a href="#" class="btn">See Project</a>
                    </div>
                </div>
            </div>
        </section>

        <section id="events" style="margin-top: 4rem;">
            <h2>Campus Events</h2>
            <div class="card-grid">
                <div class="card">
                    <div class="card-content">
                        <h3>Innovation Week</h3>
                        <p><strong>Date:</strong> October 15-20, 2025</p>
                        <p>Annual showcase of student projects and tech talks from industry leaders.</p>
                        <a href="#" class="btn">Register Now</a>
                    </div>
                </div>

                <div class="card">
                    <div class="card-content">
                        <h3>Hack the Hill</h3>
                        <p><strong>Date:</strong> November 3-5, 2025</p>
                        <p>48-hour hackathon solving challenges in education and healthcare.</p>
                        <a href="#" class="btn">Join Team</a>
                    </div>
                </div>
            </div>
        </section>

        <section id="contact" style="margin: 4rem 0;">
            <h2>Visit Our Center</h2>
            <div class="card">
                <div class="card-content">
                    <h3>Gishushu Campus</h3>
                    <p>KG 7 Ave, Kigali, Rwanda</p>
                    <p>Open Monday-Friday: 8:00 AM - 6:00 PM</p>
                    <a href="mailto:innovation@auca.rw" class="btn">Email Us</a>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2025 African University College of Africa - Innovation Center</p>
            <p>Proudly fostering the next generation of African innovators</p>
        </div>
    </footer>
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
