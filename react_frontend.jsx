import React, { useState } from 'react';
import './styles.css';

const MessRegistrationForm = () => {
  const [studentDetails, setStudentDetails] = useState({
    regNo: '',
    name: '',
    block: '',
    roomNumber: ''
  });

  const [messDetails, setMessDetails] = useState({
    messName: '',
    messType: '',
    foodSuggestion: '',
    mealType: '',
    feasibility: ''
  });

  const [reportFile, setReportFile] = useState(null);

  const handleStudentChange = (e) => {
    const { name, value } = e.target;
    setStudentDetails(prev => ({ ...prev, [name]: value }));
  };

  const handleMessChange = (e) => {
    const { name, value } = e.target;
    setMessDetails(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const submissionData = { student: studentDetails, mess: messDetails, source: "submit_button" };

    try {
      const response = await fetch('http://127.0.0.1:5000/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(submissionData)
      });

      const data = await response.json();
      if (response.ok && data.message === "Registration Successful!") {
        alert(data.message);
      } else {
        alert(data.message || 'Unexpected response from server');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred during registration');
    }
  };

  const generateReport = async () => {
    if (!studentDetails.regNo) {
      alert('Please enter your registration number.');
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:5000/generate-report', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ regNo: studentDetails.regNo })
      });

      const data = await response.json();
      if (response.ok) {
        alert('Report Generated Successfully!');
        setReportFile(data.file_url);
      } else {
        alert(data.message || 'Failed to generate report');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while generating the report');
    }
  };

  const downloadReport = () => {
    if (reportFile) {
      window.open(reportFile, "_blank");
    } else {
      alert("No report available! Please generate first.");
    }
  };

  return (
    <div>
      <h2>Campus Mess Registration</h2>
      <form onSubmit={handleSubmit}>
        <fieldset>
          <legend>Student Information</legend>
          <label>Registration Number:</label>
          <input type="text" name="regNo" value={studentDetails.regNo} onChange={handleStudentChange} required />

          <label>Full Name:</label>
          <input type="text" name="name" value={studentDetails.name} onChange={handleStudentChange} required />

          <label>Residential Block:</label>
          <input type="text" name="block" value={studentDetails.block} onChange={handleStudentChange} required />

          <label>Room Number:</label>
          <input type="text" name="roomNumber" value={studentDetails.roomNumber} onChange={handleStudentChange} required />
        </fieldset>

        <fieldset>
          <legend>Mess Preferences</legend>
          <label>Mess Name:</label>
          <select name="messName" value={messDetails.messName} onChange={handleMessChange} required>
            <option value="">Select Mess</option>
            <option value="North Mess">North Mess</option>
            <option value="South Mess">South Mess</option>
            <option value="Central Mess">Central Mess</option>
            <option value="West Mess">West Mess</option>
          </select>

          <label>Mess Type:</label>
          <select name="messType" value={messDetails.messType} onChange={handleMessChange} required>
            <option value="">Select Mess Type</option>
            <option value="Veg">Vegetarian</option>
            <option value="Non-Veg">Non-Vegetarian</option>
            <option value="Special">Special Diet</option>
            <option value="Night Mess">Night Mess</option>
          </select>

          <label>Food Suggestion:</label>
          <input type="text" name="foodSuggestion" value={messDetails.foodSuggestion} onChange={handleMessChange} />

          <label>Meal Type:</label>
          <select name="mealType" value={messDetails.mealType} onChange={handleMessChange} required>
            <option value="">Select Meal Type</option>
            <option value="Lunch">Lunch</option>
            <option value="Dinner">Dinner</option>
            <option value="Night Snack">Night Snack</option>
            <option value="Breakfast">Breakfast</option>
          </select>

          <label>Feasibility:</label>
          <select name="feasibility" value={messDetails.feasibility} onChange={handleMessChange} required>
            <option value="">Select Feasibility</option>
            <option value="Yes">Yes</option>
            <option value="No">No</option>
          </select>
        </fieldset>

        <input type="submit" value="Submit Registration" />
      </form>

      <div style={{ marginTop: '20px' }}>
        <button onClick={generateReport} style={{ marginRight: '10px', padding: '8px' }}>
          Generate Report
        </button>
        <button onClick={downloadReport} style={{ padding: '8px' }} disabled={!reportFile}>
          Download Report
        </button>
      </div>
    </div>
  );
};

export default MessRegistrationForm;
