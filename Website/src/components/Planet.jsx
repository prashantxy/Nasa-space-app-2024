
const planets = [
  {
    name: "Mercury",
    type: "Terrestrial planet",
    distance: "57.9 million km",
    diameter: "4,879 km",
    mass: "3.285 × 10^23 kg",
    yearLength: "88 days",
    temperature: "-173 to 427°C",
    image: "/mercury.png"
  },
  {
    name: "Venus",
    type: "Terrestrial planet",
    distance: "108.2 million km",
    diameter: "12,104 km",
    mass: "4.867 × 10^24 kg",
    yearLength: "225 days",
    temperature: "462°C",
    image: "/venus.png"
  },
  {
    name: "Earth",
    type: "Terrestrial planet",
    distance: "149.6 million km",
    diameter: "12,742 km",
    mass: "5.972 × 10^24 kg",
    yearLength: "365.25 days",
    temperature: "-88 to 58°C",
    image: "/earth.png"
  },
  {
    name: "Mars",
    type: "Terrestrial planet",
    distance: "227.9 million km",
    diameter: "6,779 km",
    mass: "6.39 × 10^23 kg",
    yearLength: "687 days",
    temperature: "-87 to -5°C",
    image: "/mars.png"
  },
  {
    name: "Jupiter",
    type: "Gas giant",
    distance: "778.5 million km",
    diameter: "139,820 km",
    mass: "1.898 × 10^27 kg",
    yearLength: "12 years",
    temperature: "-108°C",
    image: "/jupiter.png"
  },
  {
    name: "Saturn",
    type: "Gas giant",
    distance: "1.43 billion km",
    diameter: "116,460 km",
    mass: "5.683 × 10^26 kg",
    yearLength: "29 years",
    temperature: "-139°C",
    image: "/saturn.png"
  },
  {
    name: "Uranus",
    type: "Ice giant",
    distance: "2.87 billion km",
    diameter: "50,724 km",
    mass: "8.681 × 10^25 kg",
    yearLength: "84 years",
    temperature: "-195°C",
   image: "/uranus.png"
  },
  {
    name: "Neptune",
    type: "Ice giant",
    distance: "4.5 billion km",
    diameter: "49,244 km",
    mass: "1.024 × 10^26 kg",
    yearLength: "165 years",
    temperature: "-200°C",
    image: "/neptune.png"
  }
]

export default function Planet() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-4xl font-bold mb-8 text-center">Our Solar System</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {planets.map((planet) => (
          <div key={planet.name} className="bg-gray-800 text-white rounded-lg shadow-lg overflow-hidden">
            <div className="p-4">
              <img
                src={planet.image}
                alt={`Image of ${planet.name}`}
                width={300}
                height={300}
                className="w-full h-48 object-contain mb-4"
              />
              <h2 className="text-2xl font-bold">{planet.name}</h2>
              <p className="text-sm text-gray-400 mb-2">{planet.type}</p>
              <ul className="space-y-1 text-sm">
                <li><strong>Distance from Sun:</strong> {planet.distance}</li>
                <li><strong>Diameter:</strong> {planet.diameter}</li>
                <li><strong>Mass:</strong> {planet.mass}</li>
                <li><strong>Year Length:</strong> {planet.yearLength}</li>
                <li><strong>Temperature:</strong> {planet.temperature}</li>
              </ul>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
