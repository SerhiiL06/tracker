import { Link } from "react-router-dom";


function OffersTable({ list }) {

    const retrieveCampaign = '/campaigns/offers'
    return <table className="campaigns-table">
        <thead>
            <tr>
                <th>campaign</th>
                <th>title</th>
                <th>Description</th>
                <th>created at</th>

            </tr>
        </thead>
        <tbody>
            {list.map(campaign => (
                <tr key={campaign.id}>
                    <td>{campaign.campaign}</td>
                    <td><Link to={`${retrieveCampaign}/${campaign.slug}`}>{campaign.title}</Link></td>
                    <td>{campaign.description}</td>
                    <td>{campaign.created_at}</td>
                </tr>
            ))}
        </tbody>
    </table>
}


export default OffersTable;