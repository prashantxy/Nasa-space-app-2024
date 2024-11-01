import React from 'react'

const EarthModel = () => {
  return (
    <div className='border-t-2 border-b-2 border-slate-800'>
        <h1 className='text-center text-5xl font-semibold mt-3' >Earth Orbit Visulalization</h1>
        <iframe
                src="https://alok-2003.github.io/Earth-Model/"
                title="External Website"
                width="100%"
                height="500px"
                className="border-0 rounded-lg shadow-lg"
                allowFullScreen
            />
    </div>
  )
}

export default EarthModel