import React, { useState, useEffect, useRef } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';
import Chart from 'chart.js/auto';


function ClickPerDay() {
    const requestUrl = 'http://localhost:8000/api/v1/statistic/';
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
            labels: data.map(item => item.date),
            datasets: [
                {
                    label: 'Clicks per day',
                    data: data.map(item => item.count),
                    fill: false,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }
            ]
        };

        const ctx = document.getElementById('clicks-chart');
        chartRef.current = new Chart(ctx, {
            type: 'line',
            data: chartData,
        });
    }

    return (
        <div style={{
            width: '700px', height: '500px', margin: 'auto'
        }}>
            <h2>Clicks per Day</h2>
            <canvas id="clicks-chart"></canvas>
        </div>
    );
}

export default ClickPerDay;
