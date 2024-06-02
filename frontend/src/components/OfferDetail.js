import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";

function OfferDetail() {
    const { offerSlug } = useParams()
    const [offerData, setOfferData] = useState({})
    const requestUrl = `http://localhost:8000/api/v1/offers/${offerSlug}`
    let notFound = false;

    useEffect(() => { fetchOfferData() }, [])


    async function fetchOfferData() {
        try {
            const response = await axios.get(requestUrl)
            setOfferData(response.data)

        } catch (error) {
            console.log(error)
            notFound = true;
        }
    }

    console.log(offerData)

    return <div><h1>Title</h1> {notFound ? <h1>Not found</h1> : offerData.title}</div>
}

export default OfferDetail;