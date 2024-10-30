import React from 'react';

const Models = () => {
    const openInNewTab = (url) => {
        window.open(url, "_blank", "noopener,noreferrer");
    };

    return (
        <div className="items-center justify-center py-10 px-28">
            <h1 className="text-5xl font-bold mb-8">Our Machine Learning Models</h1>

            {/* Orbit Prediction for Celestial Bodies */}
            <div className="flex justify-between items-center w-full px-2 py-2 border-2 mb-8">
                <h1 className="font-mono text-3xl text-center">Orbit Prediction for Celestial Bodies</h1>
                <button
                    onClick={() => openInNewTab("https://orbit-ml-power-rangers.streamlit.app/")}
                    className="cursor-pointer relative group overflow-hidden rounded-xl border-2 px-8 py-2 border-slate-700"
                >
                    <span className="font-bold font-mono text-white text-xl relative z-10 group-hover:text-green-500 duration-500">Open Model</span>
                    <span className="absolute top-0 left-0 w-full bg-slate-700 duration-500 group-hover:-translate-x-full h-full"></span>
                    <span className="absolute top-0 left-0 w-full bg-slate-700 duration-500 group-hover:translate-x-full h-full"></span>
                    <span className="absolute top-0 left-0 w-full bg-slate-700 duration-500 delay-300 group-hover:-translate-y-full h-full"></span>
                    <span className="absolute delay-300 top-0 left-0 w-full bg-slate-700 duration-500 group-hover:translate-y-full h-full"></span>
                </button>
            </div>

            {/* Asteroid Detection */}
            <div className="flex justify-between items-center w-full px-2 py-2 border-2 mb-8">
                <h1 className="font-mono text-3xl text-center">Asteroid Detection</h1>
                <button
                    onClick={() => openInNewTab("https://asteroid-detection-power-rangers.streamlit.app/")}
                    className="cursor-pointer relative group overflow-hidden rounded-xl border-2 px-8 py-2 border-slate-700"
                >
                    <span className="font-bold font-mono text-white text-xl relative z-10 group-hover:text-blue-500 duration-500">Open Model</span>
                    <span className="absolute top-0 left-0 w-full bg-slate-700 duration-500 group-hover:-translate-x-full h-full"></span>
                    <span className="absolute top-0 left-0 w-full bg-slate-700 duration-500 group-hover:translate-x-full h-full"></span>
                    <span className="absolute top-0 left-0 w-full bg-slate-700 duration-500 delay-300 group-hover:-translate-y-full h-full"></span>
                    <span className="absolute delay-300 top-0 left-0 w-full bg-slate-700 duration-500 group-hover:translate-y-full h-full"></span>
                </button>
            </div>

            {/* Celestial Object Analysis */}
            <div className="flex justify-between items-center w-full px-2 py-2 border-2 mb-8">
                <h1 className="font-mono text-3xl text-center">Celestial Object Analysis</h1>
                <button
                    onClick={() => openInNewTab("https://celestial-hy5l8qp72zvhelfsdtvesv.streamlit.app/")}
                    className="cursor-pointer relative group overflow-hidden rounded-xl border-2 px-8 py-2 border-slate-700"
                >
                    <span className="font-bold font-mono text-white text-xl relative z-10 group-hover:text-red-500 duration-500">Open Model</span>
                    <span className="absolute top-0 left-0 w-full bg-slate-700 duration-500 group-hover:-translate-x-full h-full"></span>
                    <span className="absolute top-0 left-0 w-full bg-slate-700 duration-500 group-hover:translate-x-full h-full"></span>
                    <span className="absolute top-0 left-0 w-full bg-slate-700 duration-500 delay-300 group-hover:-translate-y-full h-full"></span>
                    <span className="absolute delay-300 top-0 left-0 w-full bg-slate-700 duration-500 group-hover:translate-y-full h-full"></span>
                </button>
            </div>
        </div>
    );
};

export default Models;
