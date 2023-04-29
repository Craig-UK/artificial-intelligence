import React from 'react'
import { Link } from 'react-router-dom'
import { Stack } from '@mui/material'

const About = () => {
  return (
    <>
        <Stack spacing={2}>
            <h1>Group 6 - About</h1>
            <h3>The Team</h3>
            <ul>
                <li>Devlin Cortens</li>
                <li>Jamie Ashford</li>
                <li>Lewis Smith</li>
                <li>Craig Climie</li>
                <li>Owen Murphy</li>
            </ul>
            <p>This team has created this system currently being used on this page. It allows a user to pick one of 3 presentations and use the emotions detected from them to weight a stock prediction system from any stock ticker you choose!</p>
        </Stack>
    </>
  )
}

export default About