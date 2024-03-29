import React, { useState, useEffect } from 'react'
import { Box, TextField, Button, Stack, LinearProgress } from '@mui/material'
import TheChart from './TheChart';
import { Link } from 'react-router-dom';

const text = 'rgba(255, 255, 255, 0.87)'

const Holder2 = () => {
    const [value, setValue] = useState('');
    const [emValue, setEmValue] = useState('');
    const [res, setRes] = useState('');
    const [ticker, setTicker] = useState('');
    const [emotion, setEmotion] = useState('');

    const [theData, setTheData] = useState({
        labels: [],
        datasets: []
    })
    const [options, setOptions] = useState({
        plugins: {}
    })

    const [loading, setLoading] = useState(false);

    const submitTicker = async(presNo) => {
        if(ticker) {
            setLoading(true)
            const creds = { ticker, presNo }
            const data = await fetch("http://127.0.0.1:8000/backend/three/", {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(creds)
            })
            
            const jdata = await data.json()

            if(jdata.result) {
                setLoading(false)
                alert("Invalid stock ticker, please enter a valid stock ticker.")
            }
            else {
                setLoading(false)
                setTheData({
                    labels: jdata.original.map((e,i) => i),
                    datasets: [{
                        label: "Original Predictions",
                        data: jdata.original
                    },
                    {
                    label: "Weighted Values",
                    data: jdata.predictions 
                    }]
                })

                setOptions({
                    plugins: {
                        title: {
                            display: true,
                            text: `${ticker.toUpperCase()} Stock Prediction`
                        }
                    }
                })

                console.log(jdata.sentiment)
                setRes(jdata.sentiment)
                setEmotion(jdata.emotion)
            }
        }
        else {
            alert("No stock ticker entered")
        }
    }
  
    return (
    <Box>
        <h1>Predict Stock Prices From Emotion</h1>
        <h3>Enter Ticker to Analyse Stock From a Presentation</h3>
        <Link to='/videos'>
            <h4>Presentations</h4>
        </Link>
        <Stack spacing={2}>
            <TextField 
                label="Stock Ticker of Company" 
                variant="outlined"
                value={ticker}
                onChange={(e) => setTicker(e.target.value)}
                InputLabelProps={{ style: { color: text } }}
                sx={{ fieldset: { borderColor: text }, input: { color: text } }}
            />
            <Button variant='contained' onClick={() => submitTicker(1)}>Presentation A</Button>
            <Button variant='contained' onClick={() => submitTicker(2)}>Presentation B</Button>
            <Button variant='contained' onClick={() => submitTicker(3)}>Presentation C</Button>
            {loading && 
            <LinearProgress />
            }
            <TextField 
                label="Sentiment Analysis Score" 
                variant="outlined"
                value={res}
                InputProps={{ readOnly: true }}
                InputLabelProps={{ style: { color: text } }}
                sx={{ fieldset: { borderColor: text }, input: { color: text } }}
            />
            <TextField 
                label="Emotion Felt" 
                variant="outlined"
                value={emotion}
                InputProps={{ readOnly: true }}
                InputLabelProps={{ style: { color: text } }}
                sx={{ fieldset: { borderColor: text }, input: { color: text } }}
            />
            <TheChart data={theData} options={options} />
        </Stack>
    </Box>
  )
}

export default Holder2