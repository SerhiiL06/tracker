import React, { useState, useEffect, useRef } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';
import Chart from 'chart.js/auto';


function ClickPerInterestLevel() {
    const requestUrl = 'http://localhost:8000/api/v1/statistic/click-per-interest-level/';
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
            labels: data.map(item => item.interest_level),
            datasets: [
                {
                    label: 'Clicks per interest level',
                    data: data.map(item => item.total),
                    fill: false,
                    borderColor: 'rgb(75, 192, 192)',
                    backgroundColor: [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',

                    ],
                    tension: 0.1
                }
            ]
        };

        const ctx = document.getElementById('clicks-chart');
        chartRef.current = new Chart(ctx, {
            type: 'pie',
            data: chartData,

        });
    }

    return (
        <div style={{
            width: '800px', height: '600px', margin: 'auto'
        }}>
            <h2>Clicks per Day</h2>
            <canvas id="clicks-chart"></canvas>
        </div >
    );
}

export default ClickPerInterestLevel;
