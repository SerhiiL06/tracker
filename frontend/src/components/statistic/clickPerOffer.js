import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import Chart from 'chart.js/auto';


function ClickPerOffer() {
    const requestUrl = 'http://localhost:8000/api/v1/statistic/clicks-per-offer/';
    const [data, setData] = useState([]);
    const chartRef = useRef(null);

    useEffect(() => {
        fetchData();
    }, []);

    async function fetchData() {
        try {
            const response = await axios.get(requestUrl);
            setData(response.data);
        } catch (error) {
            console.log(error);
        }
    }

    useEffect(() => {
        if (chartRef.current) {
            chartRef.current.destroy();
        }
        renderChart();
    }, [data]);

    function renderChart() {
        const chartData = {
            labels: data.map(item => item.offer),
            datasets: [
                {
                    label: 'Clicks per offer',
                    data: data.map(item => item.count),
                    fill: false,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1,
                    backgroundColor: [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',

                    ],
                }
            ]
        };

        const ctx = document.getElementById('clicks-chart');
        chartRef.current = new Chart(ctx, {
            type: 'bar',
            data: chartData,
        });
    }

    return (
        <div style={{
            width: '700px', height: '500px', margin: 'auto'
        }}>
            <h2>Clicks per Offers</h2>
            <canvas id="clicks-chart"></canvas>
        </div>
    );
}

export default ClickPerOffer;
