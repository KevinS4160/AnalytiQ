from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import utils
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify a particular origin, e.g., ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """ Uploads CSV or JSON file and returns data insights. """
    if not file.filename.endswith((".csv", ".json")):
        raise HTTPException(status_code=400, detail="Only CSV or JSON files are allowed")

    file_location = os.path.join(UPLOAD_FOLDER, file.filename)

    # Use async file reading
    contents = await file.read()
    with open(file_location, "wb") as f:
        f.write(contents)

    data_summary = utils.process_data(file_location)
    return JSONResponse(content={"filename": file.filename, "data": data_summary})

@app.get("/visualization/{filename}/{chart_type}/{columns}")
def generate_visualization(filename: str, chart_type: str, columns: str = None):
    """ Generates different types of visualizations based on user selection. """
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    df = utils.load_dataframe(file_path)
    
    if chart_type == "heatmap":
        plot_path = utils.generate_heatmap(df)
    elif chart_type == "histogram":
        if not columns:
            raise HTTPException(status_code=400, detail="Column name required for histogram")
        plot_path = utils.generate_histogram(df, columns)
    elif chart_type == "scatter":
        if not columns or "," not in columns:
            raise HTTPException(status_code=400, detail="Three columns required for 3D scatter plot")
        col_x, col_y, col_z = columns.split(",")
        plot_path = utils.generate_3d_scatter(df, col_x, col_y, col_z)
    elif chart_type == "boxplot":
        if not columns:
            raise HTTPException(status_code=400, detail="Column name required for box plot")
        plot_path = utils.generate_box_plot(df, columns)
    elif chart_type == "lineplot":
        if not columns or "," not in columns:
            raise HTTPException(status_code=400, detail="Two columns required for line plot")
        col_x, col_y = columns.split(",")
        plot_path = utils.generate_line_plot(df, col_x, col_y)
    elif chart_type == "pairplot":
        plot_path = utils.generate_pair_plot(df)
    elif chart_type == "barchart":
        if not columns or "," not in columns:
            raise HTTPException(status_code=400, detail="Two columns required for bar chart")
        col_x, col_y = columns.split(",")
        plot_path = utils.generate_bar_chart(df, col_x, col_y)
    elif chart_type == "density":
        if not columns:
            raise HTTPException(status_code=400, detail="Column name required for density plot")
        plot_path = utils.generate_density_plot(df, columns)
    else:
        raise HTTPException(status_code=400, detail="Invalid visualization type or missing columns")

    return FileResponse(plot_path, media_type="image/png")
