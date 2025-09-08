import React, { useState } from 'react';
import axios from 'axios';
import { motion } from 'framer-motion';
import MagicalBackground from './components/MagicalBackground';
import MagicButton from './components/MagicButton';

function App() {
  const [folderPath, setFolderPath] = useState('');
  const [historicalFigure, setHistoricalFigure] = useState('Alan Turing');
  const [analysis, setAnalysis] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [status, setStatus] = useState('');

  const historicalFigures = [
    'Alan Turing', 'Leonardo da Vinci', 'Marie Curie',
    'Albert Einstein', 'Nikola Tesla', 'Sun Tzu', 'Aristotle'
  ];

  const handleAnalyze = async () => {
    if (!folderPath) {
      setStatus('Please provide a folder path');
      return;
    }

    setIsLoading(true);
    setStatus('Summoning ancient wisdom...');
    setAnalysis('');

    try {
      const response = await axios.post('http://localhost:8000/api/v1/analyze', {
        folder_path: folderPath,
        historical_figure: historicalFigure
      });

      setAnalysis(response.data.analysis);
      setStatus('Ancient wisdom revealed!');
    } catch (error) {
      setStatus('The magic failed: ' + (error.response?.data?.detail || error.message));
      setAnalysis('');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen text-white overflow-hidden relative">
      <MagicalBackground />
      
      <div className="relative z-10 container mx-auto px-4 py-12">
        {/* Hero Section */}
        <motion.div 
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1 }}
          className="text-center mb-16"
        >
          <h1 className="text-6xl font-magic bg-gradient-to-r from-purple-300 via-yellow-400 to-emerald-400 
                        bg-clip-text text-transparent mb-4">
            🔮 Digital Necromancer
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            Conjure the wisdom of history's greatest minds from beyond the veil
          </p>

          {/* Animated Orb */}
          <motion.div
            className="w-24 h-24 bg-gradient-to-br from-purple-500 to-emerald-400 rounded-full 
                      mx-auto mb-8 shadow-2xl shadow-purple-500/50"
            animate={{
              scale: [1, 1.1, 1],
              rotate: [0, 5, 0, -5, 0]
            }}
            transition={{
              duration: 3,
              repeat: Infinity
            }}
          />
        </motion.div>

        {/* Main Content */}
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.5, duration: 1 }}
          className="max-w-4xl mx-auto bg-black/40 backdrop-blur-md rounded-2xl p-8 
                    border border-white/20 shadow-2xl shadow-purple-900/30"
        >
          {/* Input Form */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
            <div>
              <label className="block text-sm font-magic text-yellow-400 mb-3">
                Choose Your Ancient Guide
              </label>
              <select 
                value={historicalFigure}
                onChange={(e) => setHistoricalFigure(e.target.value)}
                className="w-full p-4 bg-black/50 border border-yellow-500/30 rounded-xl text-white
                         focus:border-yellow-400 focus:ring-2 focus:ring-yellow-400/50 transition-all"
              >
                {historicalFigures.map(figure => (
                  <option key={figure} value={figure} className="bg-gray-900 text-white">
                    {figure}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-sm font-magic text-yellow-400 mb-3">
                Path to Ancient Knowledge
              </label>
              <input
                type="text"
                value={folderPath}
                onChange={(e) => setFolderPath(e.target.value)}
                placeholder="C:\path\to\ancient\knowledge"
                className="w-full p-4 bg-black/50 border border-yellow-500/30 rounded-xl text-white
                         placeholder-gray-400 focus:border-yellow-400 focus:ring-2 focus:ring-yellow-400/50
                         transition-all"
              />
            </div>
          </div>

          {/* Magic Button */}
          <div className="text-center">
            <MagicButton onClick={handleAnalyze} disabled={isLoading}>
              {isLoading ? '🌀 Channeling Ancient Wisdom...' : '🔮 Summon the Oracle'}
            </MagicButton>
          </div>

          {/* Status */}
          {status && (
            <motion.div 
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              className={`mt-6 p-4 rounded-xl text-center ${
                status.includes('failed') ? 'bg-red-500/20 border-red-500/50' : 
                'bg-emerald-500/20 border-emerald-500/50'
              } border`}
            >
              {status}
            </motion.div>
          )}
        </motion.div>

        {/* Analysis Result */}
        {analysis && (
          <motion.div 
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="mt-12 bg-black/40 backdrop-blur-md rounded-2xl p-8 
                      border border-white/20 shadow-2xl shadow-purple-900/30"
          >
            <h2 className="text-3xl font-magic text-yellow-400 mb-6 text-center">
              📜 Wisdom from {historicalFigure}
            </h2>
            <div className="whitespace-pre-wrap leading-relaxed text-gray-200 text-lg">
              {analysis}
            </div>
          </motion.div>
        )}
      </div>
    </div>
  );
}

export default App;