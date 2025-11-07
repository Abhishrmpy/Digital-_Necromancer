import React from 'react';
import { motion } from 'framer-motion';

const MagicalBackground = () => {
  return (
    <div className="fixed inset-0 overflow-hidden z-0">
      {/* Animated gradient background */}
      <div className="absolute inset-0 bg-gradient-to-br from-purple-900 via-black to-purple-900"></div>
      
      {/* Glowing particles */}
      {[...Array(20)].map((_, i) => (
        <motion.div
          key={i}
          className="absolute w-1 h-1 bg-emerald-400 rounded-full opacity-60"
          animate={{
            x: [0, 100, 0],
            y: [0, 50, 0],
            scale: [1, 1.5, 1],
            opacity: [0.3, 0.8, 0.3]
          }}
          transition={{
            duration: 3 + Math.random() * 4,
            repeat: Infinity,
            delay: Math.random() * 2
          }}
          style={{
            left: `${Math.random() * 100}%`,
            top: `${Math.random() * 100}%`
          }}
        />
      ))}

      {/* Floating runes */}
      {['ᚠ', 'ᚢ', 'ᚦ', 'ᚨ', 'ᚱ', 'ᚲ'].map((rune, i) => (
        <motion.div
          key={i}
          className="absolute text-2xl text-yellow-400 opacity-40"
          animate={{
            y: [0, -20, 0],
            rotate: [0, 5, 0]
          }}
          transition={{
            duration: 4 + i,
            repeat: Infinity
          }}
          style={{
            left: `${20 + i * 15}%`,
            top: `${30 + i * 5}%`
          }}
        >
          {rune}
        </motion.div>
      ))}
    </div>
  );
};

export default MagicalBackground;