import React from 'react'
import { Line } from 'react-chartjs-2'
import { Chart as ChartJS, registerables } from 'chart.js'
ChartJS.register(...registerables)

const TheChart = ({data}) => {
  
    return (
    <Line data={data}/>
  )
}

export default TheChart