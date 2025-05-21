
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-me'  # Enables flash messages

projects = [
    {
        "title": "Great Plains Data Extractor",
        "description": (
            "Python + FastAPI micro-service that streams BOM data from Microsoft Dynamics GP "
            "into a MySQL warehouse, normalising part-IDs and exposing a REST API."
        ),
        "tech": ["Python", "FastAPI", "AWS RDS"],
        "repo": "https://github.com/yourhandle/gp-extractor",
        "demo": None,
    },
    {
        "title": "Cost Analysis Dashboard",
        "description": "Interactive Tableau dashboard visualising ROI, residual income, and variance analysis.",
        "tech": ["Tableau", "SQL Server"],
        "repo": None,
        "demo": "https://public.tableau.com/profile/you#!/vizhome/CostDash",
    },
    {
        "title": "Tennessee Adventure Planner",
        "description": "Next.js + Mapbox itinerary builder optimising routes to waterfalls, trails, and nightlife.",
        "tech": ["Next.js", "Mapbox", "Tailwind"],
        "repo": None,
        "demo": None,
    },
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    print(f"[Contact] {name} <{email}> says: {message}")
    flash('Thanks for reaching out! I will respond soon.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
