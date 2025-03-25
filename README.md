#📊 AnalytiQ - Smart Data Analyzer
AnalytiQ is an advanced data visualization tool that allows users to upload CSV/JSON files and generate insightful visualizations, such as heatmaps, histograms, 3D scatter plots, line charts, box plots, bar charts, pair plots, and density plots.

##🚀 Features
✔ Upload CSV/JSON files for analysis
✔ Supports multiple visualization types
✔ Interactive dark-themed frontend
✔ Built using FastAPI (Python) + HTML/JS Frontend
✔ Simple API for programmatic access

📂 Project Structure
AnalytiQ/
│── backend/
│   ├── main.py        # FastAPI Backend (API endpoints)
│   ├── utils.py       # Data processing & visualization functions
│   ├── uploads/       # Stores uploaded files (Ignored in Git)
│── frontend/
│   ├── FrontEnd.html  # User interface (Dark Theme)
│── README.md          # Project Documentation
│── requirements.txt   # Python Dependencies
│── .gitignore         # Git Ignore File

🛠 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/AnalytiQ.git
cd AnalytiQ

2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the FastAPI Backend
sh
Copy
Edit
uvicorn main:app --reload
The API will start at: http://127.0.0.1:8000

4️⃣ Open the Frontend
Simply open FrontEnd.html in your browser

OR use a local server:

sh
Copy
Edit
python -m http.server 5500
Then open: http://127.0.0.1:5500/FrontEnd.html

📡 API Endpoints
1️⃣ Upload File
URL: POST /upload/

Description: Upload a CSV/JSON file for analysis

Request (form-data):

sh
Copy
Edit
file=<selected_file>
Response:

json
Copy
Edit
{
  "filename": "dataset.csv",
  "data": { "summary": { "col1": { "mean": 4.5, "std": 1.2 } } }
}
2️⃣ Generate Visualization
URL: GET /visualization/{filename}/{chart_type}/{columns}

Example:
GET /visualization/dataset.csv/heatmap/none
GET /visualization/dataset.csv/lineplot/Time,Z

- Visualization Types Available:
- heatmap - Correlation heatmap
- histogram - Single column histogram
- scatter - 3D Scatter Plot (requires 3 columns)
- lineplot - Line chart (requires 2 columns)
- boxplot - Box plot (requires 1 column)
- barchart - Bar chart (requires 2 columns)
- pairplot - Pair plot (all numeric columns)
- density - Density (KDE) plot (requires 1 column)

🤝 Contributing
Want to improve AnalytiQ? Contributions are welcome!

- Fork the repo
- Create a new branch
- Commit your changes
- Open a Pull Request

📄 License
This project is licensed under the MIT License.



