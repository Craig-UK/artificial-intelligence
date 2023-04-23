import React, { useState, useEffect } from 'react'
import { Box, TextField, Button, Stack } from '@mui/material'
import TheChart from './TheChart';

const text = 'rgba(255, 255, 255, 0.87)'

const Holder = () => {
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

    const handleClick = () => {
        submitVideo();
    }

    const handleClickEmo = () => {
        submitEmo();
    }

    const handleClickStock = () => {
        submitTicker();
    }

    const submitEmo = async () => {
        const creds = { emValue }
        const data = await fetch("http://127.0.0.1:8000/backend/emotion/", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(creds)
        })

        const jdata = await data.json()

        console.log(jdata.result)

        setEmotion(jdata.result)
    }

    const submitTicker = async() => {
        const creds = { ticker }
        const data = await fetch("http://127.0.0.1:8000/backend/stocks/", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(creds)
        })
        
        const jdata = await data.json()

        if(jdata.result) {
            alert("Invalid stock ticker, please enter a valid stock ticker.")
        }
        else {
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
        }
    }

    const submitVideo = async () => {
        const creds = { value }
        const data = await fetch("http://127.0.0.1:8000/backend/sentiment/", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(creds)
        })

        const jdata = await data.json()

        console.log(jdata.result)

        setRes(jdata.result)
        /* setTheData({
            labels: jdata.nums.map((e,i) => i),
            datasets: [{
                label: "Testing",
                data: jdata.nums 
            }]
        }) */
    }
  
    return (
    <Box>
        <h1>Predict Stock Prices From Emotion</h1>
        <h3>Select video to analyse</h3>
        <Stack spacing={2}>
            <TextField 
                label="Relative Path of Audio" 
                variant="outlined"
                value={value}
                onChange={(e) => setValue(e.target.value)}
                InputLabelProps={{ style: { color: text } }}
                sx={{ fieldset: { borderColor: text }, input: { color: text } }}
            />
            <TextField 
                label="Relative Path of Video" 
                variant="outlined"
                value={emValue}
                onChange={(e) => setEmValue(e.target.value)}
                InputLabelProps={{ style: { color: text } }}
                sx={{ fieldset: { borderColor: text }, input: { color: text } }}
            />
            <TextField 
                label="Stock Ticker of Company" 
                variant="outlined"
                value={ticker}
                onChange={(e) => setTicker(e.target.value)}
                InputLabelProps={{ style: { color: text } }}
                sx={{ fieldset: { borderColor: text }, input: { color: text } }}
            />
            <Button variant='contained' onClick={handleClick}>Sentiment</Button>
            <Button variant='contained' onClick={handleClickEmo}>Emotion</Button>
            <Button variant='contained' onClick={submitTicker}>Stock</Button>
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

export default Holder