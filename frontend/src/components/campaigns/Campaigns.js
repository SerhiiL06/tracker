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
        </div>
    );
}
export default Campaigns;