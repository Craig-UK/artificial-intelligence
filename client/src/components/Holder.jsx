import React, { useState, useEffect } from 'react'
import { Box, TextField, Button, Stack } from '@mui/material'

const Holder = () => {
    const [value, setValue] = useState('');
    const [res, setRes] = useState('');

    const handleClick = () => {
        submitVideo();
    }

    const submitVideo = async () => {
        const creds = { value }
        const data = await fetch("http://127.0.0.1:8000/backend/test/", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(creds)
        })

        const jdata = await data.json()

        console.log(jdata.result)

        setRes(jdata.result)
    }
  
    return (
    <Box>
        <h1>Predict Stock Prices From Emotion</h1>
        <h3>Select video to analyse</h3>
        <Stack>
            <TextField 
                label="Absolute Path of Video" 
                variant="outlined"
                value={value}
                onChange={(e) => setValue(e.target.value)}
            />
            <Button onClick={handleClick}>Analyse</Button>
            <TextField 
                label="Sentiment Analysis Score" 
                variant="outlined"
                value={res}
                onChange={(e) => setRes(e.target.value)}
            />
            <TextField label="Emotion Felt" variant="outlined"/>
        </Stack>
    </Box>
  )
}

export default Holder