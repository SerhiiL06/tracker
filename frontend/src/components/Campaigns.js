import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Campaigns.css'
import CampaignsTable from './CampaignsTable';


function Campaigns() {

    const requestUrl = 'http://127.0.0.1:8000/api/v1/campaigns/'
    const [campaignsList, setCampaignsList] = useState([]);

    const [isFull, setIsFull] = useState(false);

    useEffect(() => {
        fetchData();
    }, [isFull]);


    async function fetchData() {
        try {
            const response = await axios.get(isFull ? requestUrl + '?full=True' : requestUrl);
            console.log(`data: ${response}`)
            setCampaignsList(response.data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }


    return (
        <div style={{ display: 'flex' }}>
            <div style={{ flex: 1 }}>
                <button className='campaigns-button' onClick={() => {
                    setIsFull(!isFull)
                }}> {isFull ? 'Only actually' : 'Show full'}</button>
                <CampaignsTable list={campaignsList} />
            </div>
            <div className="app-block filter" style={{ marginLeft: '20px' }}>
                <div className="filter-group">
                    <input id="title" type='text' placeholder="filter by title" />
                </div>
                <div className="filter-group">
                    <input id='author' type='text' placeholder="filter by author" />
                </div>
                <div className="filter-group">
                    <label htmlFor="sortBy">Sort By: </label>
                    <select id="sortBy">
                        <option value="title">Title</option>
                        <option value="author">Author</option>
                        <option value="date">Date</option>
                    </select>
                </div>
                <div className="filter-group">
                    <label htmlFor="sortOrder">Sort Order: </label>
                    <select id="sortOrder">
                        <option value="asc">Ascending</option>
                        <option value="desc">Descending</option>
                    </select>
                </div>
                <button>Clear filter</button>
            </div>
        </div>
    );
}
export default Campaigns;