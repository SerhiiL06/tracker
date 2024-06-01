import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Campaigns.css'
import CampaignsTable from './CampaignsTable';
import DataTable from 'react-data-table-component';

function Campaigns() {

    const requestUrl = 'http://127.0.0.1:8000/api/v1/campaigns/'
    const [campaignsList, setCampaignsList] = useState([]);


    const columns = [
        {
            name: 'Title',
            selector: row => row.title,
            sortable: true,
        },
    ];

    useEffect(() => {
        fetchData(false);
    }, []);


    async function fetchData(isFull) {
        try {
            const response = await axios.get(isFull ? requestUrl + '?full=True' : requestUrl);
            console.log(`data: ${response}`)
            setCampaignsList(response.data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }




    return (
        <div>
            <button onClick={() => fetchData(true)}> Full info</button>
            <CampaignsTable list={campaignsList} />
        </div>
    );

}

export default Campaigns;
