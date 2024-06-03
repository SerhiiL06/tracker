import axios from "axios";
import { useState, useEffect } from "react";

import DataTable from 'react-data-table-component';

function LeadsList() {

    const requestUrl = 'http://localhost:8000/api/v1/leads'
    const [leadsList, setLeadsList] = useState([])


    const columns = [
        {
            name: 'Ip adderss',
            selector: row => row.ip_address,
        },
        {
            name: 'Operation System',
            selector: row => row.os,
        },
        {
            name: 'Agent',
            selector: row => row.agent
        }
    ]

    useEffect(() => {
        fetchLeadsList()
    }, []);


    async function fetchLeadsList() {

        try {
            const response = await axios.get(requestUrl)
            setLeadsList(response.data)
        } catch (error) {
            console.log(error)
        }


    }

    console.log(leadsList)
    return (<DataTable data={leadsList} columns={columns} />)
}


export default LeadsList;