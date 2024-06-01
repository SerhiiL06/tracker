import React, { useState, useEffect } from 'react';
import axios from 'axios';
function Clicks() {



    const requestUrl = 'http://127.0.0.1:8000/api/v1/clicks/'
    const [clicksList, setCampaignsList] = useState([]);

    useEffect(() => {
        fetchData();
    }, []);


    async function fetchData() {
        try {
            const response = await axios.get(requestUrl);
            console.log(`data: ${response}`)
            setCampaignsList(response.data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }


    return <table className="campaigns-table">
        <thead>
            <tr>
                <th>Title</th>
                <th>Description</th>
                <th>Start Date</th>
                <th>End Date</th>
            </tr>
        </thead>
        <tbody>
            {clicksList.map(click => (
                <tr key={click.id}>
                    <td>{click.id}</td>
                    <td>{click.interest_level}</td>
                    <td>{click.start_date}</td>
                    <td>{click.end_date}</td>
                </tr>
            ))}
        </tbody>
    </table>
}


export default Clicks;