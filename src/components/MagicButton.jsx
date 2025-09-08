import React from 'react';
import { motion } from 'framer-motion';

const MagicButton = ({ children, onClick, disabled }) => {
  return (
    <motion.button
      onClick={onClick}
      disabled={disabled}
      className="relative overflow-hidden bg-gradient-to-r from-purple-700 via-violet-600 to-purple-700 
                 text-white font-magic text-xl px-8 py-4 rounded-full border-2 border-yellow-400"
      whileHover={{ 
        scale: 1.05,
        boxShadow: "0 0 20px 5px rgba(168, 85, 247, 0.5)"
      }}
      whileTap={{ scale: 0.95 }}
      animate={{
        backgroundPosition: ['0% 50%', '100% 50%', '0% 50%']
      }}
      transition={{
        backgroundPosition: { duration: 2, repeat: Infinity },
        scale: { duration: 0.2 }
      }}
    >
      {/* Glow effect */}
      <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent 
                      animate-pulse"></div>
      
      {/* Sparkle particles */}
      <motion.div
        className="absolute inset-0 pointer-events-none"
        initial={{ opacity: 0 }}
        whileHover={{ opacity: 1 }}
      >
        {[...Array(5)].map((_, i) => (
          <motion.div
            key={i}
            className="absolute w-1 h-1 bg-white rounded-full"
            animate={{
              y: [0, -10, 0],
              x: [0, 5, 0],
              opacity: [0, 1, 0]
            }}
            transition={{
              duration: 1,
              delay: i * 0.2
            }}
            style={{
              left: `${20 + i * 15}%`,
              top: '50%'
            }}
          />
        ))}
      </motion.div>

      {children}
    </motion.button>
  );
};

export default MagicButton;