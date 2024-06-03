import { Link } from "react-router-dom";


function OffersTable({ list }) {

    const retrieveCampaign = '/campaigns/offers'
    return <table className="campaigns-table">
        <thead>
            <tr>
                <th>Campaign</th>
                <th>Title</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            {list.map(offer => (
                <tr key={offer.id}>
                    <td>{offer.campaign}</td>
                    <td><Link to={`${retrieveCampaign}/${offer.slug}`}>{offer.title}</Link></td>
                    <td>{offer.description}</td>

                </tr>
            ))}
        </tbody>
    </table>
}


export default OffersTable;