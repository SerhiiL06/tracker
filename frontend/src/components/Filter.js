import './Filter.css'

function Filter(props) {
    const { setOrdering } = { props }
    return (
        <div className="app-block filter">
            <div className="filter-group">
                <label htmlFor="sortOrder">Sort Order: </label>
                <select id="sortOrder" onChange={setOrdering}>
                    <option value="asc">Ascending</option>
                    <option value="desc">Descending</option>
                </select>
            </div>
        </div>
    )
}


export default Filter;