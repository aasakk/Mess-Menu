# Mess Menu Registration System  

## Overview  
The **Mess Menu Registration System** is a web application designed to facilitate student meal registration in campus mess facilities. It allows students to register their mess preferences, submit food suggestions, and generate reports on their meal choices. The system integrates a **React frontend** with a **Flask backend** and a **MySQL database** to store and manage student and mess details efficiently.  

## Features  
- **Student Registration:** Students can enter their details (registration number, name, block, room number) and select their preferred mess.  
- **Mess Preferences:** Users can choose the mess name, meal type, and provide food suggestions.  
- **Data Storage:** Information is securely stored in a MySQL database.  
- **Report Generation:** The system generates Excel reports based on student registration data.  
- **REST API Integration:** The backend provides endpoints for submitting student data and generating reports.  

## Tech Stack  
- **Frontend:** React.js (Handles the UI for student registration and report generation)  
- **Backend:** Flask (Processes API requests and interacts with the database)  
- **Database:** MySQL (Stores student and mess details)  
- **Other Dependencies:** Flask-CORS, Pandas (for report generation), and MySQL Connector  

## Installation & Setup  
1. **Clone the repository**  
2. **Backend Setup:**  
   - Install required Python packages  
   - Configure the MySQL database  
   - Run the Flask server  
3. **Frontend Setup:**  
   - Install dependencies  
   - Start the React development server  
4. **Test the system by submitting a registration and generating a report**  

## Usage  
- Students fill out the registration form and submit their details.  
- The backend stores the data and responds with success/failure messages.  
- Users can generate reports and download them as Excel files.  

## Future Enhancements  
- Authentication for students and admins  
- Improved UI/UX for a seamless experience  
- More detailed meal analytics and feedback mechanisms  
