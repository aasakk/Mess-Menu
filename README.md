# Mess Menu Management System

## Project Overview
The Mess Menu Management System is a web-based application that allows students to register for mess services, specify their meal preferences, and generate reports related to their meal plans. The system consists of a frontend built with React and a backend developed using Flask, which communicates with a MySQL database for data storage and retrieval.

### Features
- **Student Registration:** Students can enter their registration details, including name, block, and room number.
- **Mess Selection:** Users can select their preferred mess, specify meal types, and provide food suggestions.
- **Data Storage:** The backend stores student and mess details in a MySQL database.
- **Report Generation:** The system allows users to generate an Excel report based on stored mess preferences.
- **Report Downloading:** Users can download the generated reports for reference.

## Technology Stack
- **Frontend:** React.js, HTML, CSS
- **Backend:** Flask (Python), Flask-CORS
- **Database:** MySQL
- **Data Handling:** Pandas for report generation

## Files in the Project
### Backend Files
- `mysql_setup.py` – Initializes the MySQL database.
- `app1.py` – Contains the Flask application, handles API endpoints, and interacts with the database.

### Frontend Files
- `index.html`, `package.json`, `react_frontend.jsx`, `styles.css`, `index.js`, `App.js`, `manifest.json`, `robots.txt` – Comprise the React-based frontend.

## Execution Instructions
### 1. Setting Up the Backend
#### Install Dependencies
Ensure you have Python installed, then install the required Python packages:
```bash
pip install flask flask-cors mysql-connector-python pandas openpyxl
```

#### Configure and Run the MySQL Database
1. Start the MySQL server.
2. Run `mysql_setup.py` to set up the required database and tables:
   ```bash
   python mysql_setup.py
   ```

#### Start the Flask Backend
Run the Flask application:
```bash
python app1.py
```
This will start the backend server at `http://127.0.0.1:5000/`.

### 2. Setting Up the Frontend
#### Install Dependencies
Navigate to the frontend directory and install dependencies:
```bash
npm install
```

#### Start the React Frontend
Run the following command to start the frontend:
```bash
npm start
```
This will start the application on `http://localhost:3000/`, where users can interact with the mess registration system.

## Usage Instructions
1. Open the web application in a browser (`http://localhost:3000/`).
2. Fill in the student registration details and mess preferences.
3. Click the **Submit Registration** button to store the data.
4. Click **Generate Report** to create an Excel report of mess registrations.
5. Click **Download Report** to retrieve the generated file.

This completes the setup and usage of the Mess Menu Management System.

Contributors:
Aasavari Khire, Drashi Manoria 

