import { Link } from "react-router-dom";

function CampaignsTable({ list }) {

    const retrieveCampaign = '/campaigns/offers'

    return <table className="campaigns-table">
        <thead>
            <tr>
                <th>Id</th>
                <th>Title</th>
                <th>Description</th>
                <th>Start Date</th>
                <th>End Date</th>
            </tr>
        </thead>
        <tbody>
            {list.map(campaign => (
                <tr key={campaign.id}>
                    <td>{campaign.id}</td>
                    <td><Link to={`${retrieveCampaign}`}>{campaign.title}</Link></td>
                    <td>{campaign.description}</td>
                    <td>{campaign.start_date}</td>
                    <td>{campaign.end_date}</td>
                </tr>
            ))}
        </tbody>
    </table>
}


export default CampaignsTable;