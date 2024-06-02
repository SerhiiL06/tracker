import React from "react";
import { Link } from 'react-router-dom';



function Header() {
    return (
        <header className="app-header">
            <nav>
                <ul>
                    <Link to='/campaigns'> <li><button>Campaigns</button></li></Link>
                    <Link to='/campaigns/offers'> <li><button>Offers</button></li></Link>
                    <Link to='/leads'> <li><button>Leads</button></li></Link>
                    <Link to='/clicks'> <li><button>Clicks</button></li></Link>
                    <Link to='/statistic'> <li><button>Statistic</button></li></Link>
                </ul>
            </nav>
        </header>
    )
}

export default Header;