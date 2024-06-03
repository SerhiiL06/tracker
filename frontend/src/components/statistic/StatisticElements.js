import React from 'react';
import { Link } from 'react-router-dom';
import './StatisticElements.css';

function StatisticElements() {
    const statisticData = [
        { link: '/click-per-day', title: 'Clicks', description: 'Clicks per day' },
        { link: '/click-interest', title: 'Interest Levels', description: 'Click per interesting levels' },
        { link: '/click-offers', title: 'Offers click', description: 'Click per offers' },
    ];

    return (
        <div className="statistic-container">
            {statisticData.map(statistic => (
                <Link key={statistic.link} to={statistic.link} className="statistic-card">
                    <h3>{statistic.title}</h3>
                    <p>{statistic.description}</p>
                </Link>
            ))}
        </div>
    );
}

export default StatisticElements;
