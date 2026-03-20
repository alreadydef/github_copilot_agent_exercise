import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    console.log('Fetching workouts from:', API_URL);
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => {
        console.log('Workouts data received:', data);
        const items = Array.isArray(data) ? data : data.results || [];
        setWorkouts(items);
      })
      .catch((err) => console.error('Error fetching workouts:', err));
  }, []);

  return (
    <div>
      <h2>Workouts</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Schedule</th>
            <th>Max Attendance</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map((workout, index) => (
            <tr key={workout._id || workout.id || index}>
              <td>{workout.name}</td>
              <td>{workout.description}</td>
              <td>{workout.schedule}</td>
              <td>{workout.max_attendance}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Workouts;
