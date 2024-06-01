import React from 'react';
import widgets from '../utils/widgets';

function Dashboard() {


    return (
        <div className="dashboard">
            <h2>Dashboard</h2>
            <div className="widgets">
                {widgets.map((widget, index) => (
                    <div className="widget" key={index}>
                        <h3>{widget}</h3>

                    </div>
                ))}
            </div>
        </div>
    );
}


export default Dashboard;
