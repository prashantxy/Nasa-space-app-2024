import { useState, useRef, Suspense } from 'react'
import './App.css'
import { Canvas } from '@react-three/fiber'
import SolarSystem from '../public/SolarSystem'
import { Environment, OrbitControls } from '@react-three/drei'
import Planet from './components/Planet'
import Models from './components/models'

function App() {
  const [count, setCount] = useState(0)

  // Create a ref for the section you want to scroll to
  const exploreSectionRef = useRef(null);

  // Example of parameters you can pass to the SolarSystem component
  const solarSystemProps = {
    position: [0, -40, -300],   // Position in the scene
    scale: 10,               // Scale of the solar system
    rotation: [10, 0, 0],    // Rotation of the solar system
  }

  // Function to handle scroll when the button is clicked
  const handleScroll = () => {
    if (exploreSectionRef.current) {
      exploreSectionRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <>
      <div className="min-h-[90%] bg-[url('/stars.jpg')] text-white">
        <header className="px-24 flex justify-between items-center">
          <img
            src="/powerranger.png"
            alt="Power Rangers Logo"
            className="w-24 h-24"
          />
          <nav>
            <ul className="flex font-bold space-x-10">
              <li><a href="#" className="hover:text-gray-300">HOME</a></li>
              <li><a href="#" className="hover:text-gray-300">PLANETS</a></li>
              <li><a href="#" className="hover:text-gray-300">ORBITS</a></li>
              <li><a href="#" className="hover:text-gray-300">HELP</a></li>
              <li><a href="#" className="hover:text-gray-300">ABOUT</a></li>
            </ul>
          </nav>
        </header>
        <main className="relative h-[calc(100vh-80px)] overflow-hidden">
          <div className="absolute inset-0 z-10">
            <div className="container mx-32 px- h-full flex flex-col justify-center">
              <h1 className="text-8xl font-bold mb-4">
                <span className="block text-10xl mb-2">NASA Space</span>
                Explore the<br /> Universe
              </h1>
              <p className="max-w-md mb-8 font-mono text-lg">
                Embark on an adventure through the vastness of space! Our app allows you to discover planets, near-Earth asteroids, comets, and other celestial bodies in real-time. Learn how to protect Earth by tracking and diverting potentially hazardous asteroids.
              </p>
              <button 
                className="bg-[url('/frame1.png')] bg-cover bg-center [#B45334] hover:bg-gray-600 font-mono text-white text-2xl font-bold py-4 px-8 rounded-full w-56"
                onClick={handleScroll}  // Attach the scroll function to the button
              >
                START EXPLORING
              </button>
            </div>
          </div>

          <div className="absolute -right-20 z-20 top-0 w-2/3 h-full">
            <img
              src="/frame1.png"
              alt="Mars"
              width={600}
              height={500}
              className="object-co h-full w-[75%]"
            />
          </div>
        </main>
      </div>

      {/* Add this section which the button will scroll down to */}
      <div ref={exploreSectionRef} className="min-h-screen bg-black text-white pt-12">
        {/* <Canvas>
          <OrbitControls />
          <Suspense fallback={null}>
            <SolarSystem {...solarSystemProps} />
          </Suspense>
          <Environment preset='sunset' />
        </Canvas> */}

        {/* Insert the Planet component here */}
        <div className="mt-6">
          <Models/>
          <Planet /> {/* Display the planet information */}
        </div>
      </div>
    </>
  )
}

export default App
