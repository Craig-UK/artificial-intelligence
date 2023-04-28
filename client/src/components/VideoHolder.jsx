import React from 'react'
import { Stack, CardMedia } from '@mui/material'
import { Link } from 'react-router-dom'

const VideoHolder = () => {
  return (
    <>
        <Stack spacing={1}>
            <Link to='/'>
                <h4>Return to Home</h4>
            </Link>
            <h1>Presentation Selections</h1>
            <h3>Presentation A</h3>
            <video controls>
                <source src="../../PresentationA.mp4" type="video/mp4" />
            </video>
            <hr/>
            <h3>Presentation A</h3>
            <video controls>
                <source src="../../PresentationB.mp4" type="video/mp4" />
            </video>
            <hr/>
            <h3>Presentation C</h3>
            <video controls>
                <source src="../../PresentationC.mp4" type="video/mp4" />
            </video>
        </Stack>
    </>
  )
}

export default VideoHolder