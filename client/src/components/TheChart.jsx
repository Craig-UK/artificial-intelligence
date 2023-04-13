import React from 'react'
import { Line } from 'react-chartjs-2'
import { Chart as ChartJS, registerables } from 'chart.js'
ChartJS.register(...registerables)

const TheChart = ({data, options}) => {
  
    return (
    <Line data={data} options={options}/>
  )
}

export default TheChart