import { useLocation } from 'react-router-dom';
import queryString from 'query-string';
import { useEffect, useState } from 'react';
import axios from 'axios';
import OffersTable from './OffersTable';


function Offers() {
    const location = useLocation()
    const queryParams = queryString.parse(location.search);



    const requestUrl = 'http://localhost:8000/api/v1/offers/'
    const [offersData, setOffersData] = useState([])

    useEffect(() => {
        fetchOffersData();
    }, []);

    async function fetchOffersData() {
        try {

            const response = await axios.get(queryParams['campid'] ? requestUrl + `?camp_id=${queryParams['campid']}` : requestUrl);
            console.log(`data: ${response}`)
            setOffersData(response.data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    return (
        <div>
            <OffersTable list={offersData} />
        </div>
    );

}

export default Offers;