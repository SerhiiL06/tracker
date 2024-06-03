import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Clicks.css'
import Filter from '../Filter'


function Clicks() {
    const requestUrl = 'http://127.0.0.1:8000/api/v1/clicks/';
    const [clicksList, setClicksList] = useState([]);
    const [nextPage, setNextPage] = useState(null);
    const [orderBy, changeOrderBy] = useState('desc')

    useEffect(() => {
        fetchData();
    }, [orderBy]);

    async function fetchData() {
        try {
            let req = undefined
            if (orderBy) {
                if (orderBy && 'asc') {
                    req = requestUrl + '?ordering=click_on'
                } else {
                    req = requestUrl + '?ordering=-click_on'
                }
            }
            const response = await axios.get(req);
            setClicksList(response.data.results);
            setNextPage(response.data.next);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    async function fetchNextPage() {
        try {
            const response = await axios.get(nextPage);
            setClicksList(prevList => [...prevList, ...response.data.results]);
            setNextPage(response.data.next);
        } catch (error) {
            console.error('Error fetching next page:', error);
        }
    }

    return (
        <div>
            <h1>Clicks Data</h1>
            <div style={{ display: 'flex' }}>
                <div style={{ flex: 1 }}>
                    <table className="clicks-table">
                        <thead>
                            <tr>
                                <th>Click date</th>
                                <th>Interest Level</th>
                                <th>Lead</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            {clicksList.map(click => (
                                <tr key={click.id}>
                                    <td>{click.click_on}</td>
                                    <td>{click.interest_level}</td>
                                    <td>{click.lead_info}</td>
                                    <td>{click.end_date}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                    {nextPage && (
                        <button onClick={fetchNextPage}>Load More</button>
                    )}
                </div>
            </div>
        </div>
    );

}

export default Clicks;
