import React from 'react';
import { motion } from 'framer-motion';

const MagicButton = ({ onClick, disabled, children }) => {
  return (
    <motion.button
      onClick={onClick}
      disabled={disabled}
      className={`px-8 py-4 text-lg font-bold rounded-xl transition-all duration-300 ${
        disabled
          ? 'bg-gray-600 cursor-not-allowed opacity-70'
          : 'bg-gradient-to-r from-purple-600 to-emerald-500 hover:from-purple-700 hover:to-emerald-600 shadow-lg hover:shadow-xl text-white'
      }`}
      whileHover={{ scale: disabled ? 1 : 1.05 }}
      whileTap={{ scale: disabled ? 1 : 0.95 }}
    >
      {children}
    </motion.button>
  );
};

export default MagicButton;